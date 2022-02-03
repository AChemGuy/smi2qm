import os
import re
import subprocess
import argparse
parser = argparse.ArgumentParser(description='smi2qm limited example program')
parser.add_argument('-v', '--version', action='version', version='smi2qm limited example program v0.0.1', help='version')
args = parser.parse_args()

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

#####################
class XTB():
 
  def __init__(self):
      self = self

 def execute(self):
     command = 'xtb geom.xyz --opt normal >xtb.out'
     subprocess.check_call(command, shell=True)

 def get_energy(self):
     with open('xtb.out, 'r') as fd:
      for line in fd.readlines():
       if 'TOTAL ENERGY' in line:
        energy = line.split()[4]
     return energy
               
 def get_optimised_geometry(self):
     with open('xtbopt.xyz', 'r') as fd:
      struc = fd.read()          

##################### 



#directory containing relevant smiles strings
path = '/smi2qm/SMILES'
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
   xtb = XTB()
   try:
    xtb.execute()
    xtb.get_energy()
    xtb.get_optimised_geometry()           
    entry = {"calculator": "GFN2-xTB", "smiles": smi, "xyz": struc, "charge": molcharge, "energy": energy, "fingerprint" : fp}
    collection.insert_one(entry)
   except: 
    entry_failed = {"calculator": "GFN2-xTB", "smiles": smi, "xyz": struc, "charge": molcharge, "fingerprint" : fp}
    collection_failed.insert_one(entry_failed)

   files = ['charges', 'wbo', 'xtbopt.log', 'xtbrestart', 'xtb.out', 'xtbopt.xyz',	'xtbtopo.mol', '.xtboptok', '.NOT_CONVERGED', '.CHRG'] 
   for file in files:
    if os.path.exists(file):
     os.remove(file)
