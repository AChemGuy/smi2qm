######
In progress...
######

import numpy as np
import os
from pymongo.cursor import Cursor
from pymongo.collection import Collection

parser = argparse.ArgumentParser(description='smi2qm limited example program numpy statistics tools')
parser.add_argument('-v', '--version', action='version', version='smi2qm limited example program v0.0.1 - statistics tools', help='version')
parser.add_argument('-c', '--client', required=True, help='MongoDB client e.g mongodb://localhost')
parser.add_argument('-d', '--dbname', required=True, help='MongoDB database name')
parser.add_argument('-n', '--collname', required=True, help='MongoDB collection name')
parser.add_argument('-s', '--smiles', required=False, help='SMILES string for investigating single molecule')
args = parser.parse_args()

argcli = args.client
argdb = args.dbname
argcoll = args.collname
argcollf = args.collname+'_failed'
argsmi = args.smiles
client = MongoClient(argcli)
db = client[argdb]
collection = db[argcoll]
collection_failed = db[argcollf]

#for individual molecules, atoms and coords have corresponding numpy array rows
moldoc = collection.find_one({'smi': }, {"opt xyz" : 1, "_id" : 0})
with open('optstruc.xyz', 'w') as w:
 w.write(moldoc["opt xyz"])
npatoms = np.genfromtxt('optstruc.xyz', dtype=str, usecols=0)
npcoords = np.genfromtxt('optstruc.xyz', dtype=float, usecols=(1,2,3))
os.remove('optstruc.xyz')
print("atoms: "+npatoms"
print("coordinates: "+npcoords)

#min and max no. of atoms, av. size of molecule in data set
natomslist = collection.distinct("no. of atoms")
npnatoms = np.array(natomslist)
smallest = npatoms.min()
largest = npatoms.max()
avsize = npatoms.mean()
print("smallest molecule: "+smallest+" atoms")
print("largest molecule: "+largest+" atoms")
print("average size of molecule: "+avsize+" atoms")
 
#more useful measures to be added

