######
In progress...
######

import numpy as np
import os
from pymongo.cursor import Cursor

class NPSTATS():

#for individual molecules, atoms and coords have corresponding numpy array rows
 def atomcoords():
  moldoc = collection.find_one({'smi': <'string'>}, {"opt xyz" : 1, "_id" : 0})
  with open('optstruc.xyz', 'w') as w:
   w.write(moldoc["opt xyz"])
  npatoms = np.genfromtxt('optstruc.xyz', dtype=str, usecols=0)
  npcoords = np.genfromtxt('optstruc.xyz', dtype=float, usecols=(1,2,3))
  os.remove('optstruc.xyz')
  return "atoms: "+npatoms, "coordinates: "+npcoords

#min and max no. of atoms, av. size of molecule in data set
 def npnatoms():
  natomslist = collection.distinct("no. of atoms")
  npnatoms = np.array(natomslist)
  smallest = npatoms.min()
  largest = npatoms.max()
  avsize = npatoms.mean()
  return "smallest molecule: "+smallest+" atoms", "largest molecule: "+largest+" atoms", "average size of molecule: "+avsize+" atoms"
 
#more useful measures to be added

