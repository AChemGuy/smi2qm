import os
import re
import subprocess

#import Open Babel molecular tools
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
collection_failed = db.coll_failed

######
class XTB():
 
  def __init__(self):
      self = self

 def execute(self):
     command = 'xtb geom.xyz --opt normal >xtb.out'
     subprocess.check_call(command, shell=True)

 def read_results(self):

###### 



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

# execute quantum chem calcs, add all data from loop iteration to MongoDB
   try:
    energy = atoms.get_potential_energy()
    entry = {"calculator": "GFN2-xTB", "smiles": smi, "xyz": struc, "charge": molcharge, "energy": energy, "fingerprint" : fp}
    collection.insert_one(entry)
   except: 
    entry_failed = {"calculator": "GFN2-xTB", "smiles": smi, "xyz": struc, "charge": molcharge, "fingerprint" : fp}
    collection_failed.insert_one(entry_failed)

   files = [] 
   for file in files:
    if os.path.exists(file):
     os.remove(file)
