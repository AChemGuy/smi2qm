######
In progress...
######

#need to incorporate into docker image usage

import numpy as np
import os
import pymongo
from pymongo import MongoClient

#MongoDB client, db name and collection name
#need to get user-specified names, as done for main.py 
client=MongoClient()
db = client.smi2qm
collection = db.test

#for individual molecules, atoms and coords have corresponding numpy array rows
moldoc = collection.find_one({'smi': <'string'>}, {"opt xyz" : 1, "_id" : 0})
with open('optstruc.xyz', 'w') as w:
 w.write(moldoc["opt xyz"])
npatoms = np.genfromtxt('optstruc.xyz', dtype=str, usecols=0)
npcoords = np.genfromtxt('optstruc.xyz', dtype=float, usecols=(1,2,3))
os.remove('optstruc.xyz')

#min and max no. of atoms, av. size of molecule in data set
natomslist = collection.distinct("no. of atoms")
npnatoms = np.array(natomslist)
smallest = npatoms.min()
largest = npatoms.max()
avsize = npatoms.mean()
#more useful measures to be added

