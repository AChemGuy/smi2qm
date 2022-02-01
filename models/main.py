import os
import re

#import Atomic Simulation Environment, XTB quantum chemistry software and Open Babel molecular tools
import ase
from ase import io
from ase import Atoms
from xtb.ase.calculator import XTB
from openbabel import openbabel
from openbabel import pybel

#import tqdm to monitor progress of batch of calculations
from tqdm import tqdm

#import PyMongo, an interface to MongoDB
import pymongo
from pymongo import MongoClient
#use local client, name database and collection
client = MongoClient()
db = client.db
collection = db.coll

#directory containing relevant smiles strings
path = '/app/SMILES'
os.chdir(path)

for file in os.listdir(path):

 #get smi
 with open(file, "r") as f:
  for line in tqdm(f.readlines()):
   smi = line

 # smi->xyz
   mol = pybel.readstring("smi", smi)
   mol.OBMol.AddHydrogens()
   mol.make3D()
   mol.write("xyz", "geom.xyz")
   with open('geom.xyz', 'r') as strucf:
    struc = strucf.readlines()

# smi->chrg
   molcharge = mol.OBMol.GetTotalCharge()

#calc molecular fingerprint
   fp = str(mol.calcfp())

# add data from current iteration of for loop to MongoDB collection
   atoms = ase.io.read('geom.xyz',format='xyz')
   atoms.charge = molcharge
   atoms.calc = XTB(method="GFN2-xTB")
   energy = atoms.get_potential_energy()

   entry = {"calculator": "GFN2-xTB", "smiles": smi, "xyz": struc, "charge": molcharge, "energy": energy, "fingerprint" : fp}
   collection.insert_one(entry)


   os.remove("geom.xyz") 
