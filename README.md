# smi2qm
[![CI Pipeline](https://github.com/achemguy/smi2qm/actions/workflows/ci.yaml/badge.svg)](https://github.com/achemguy/smi2qm/actions/workflows/ci.yaml) [![Docker Container Push Pipeline](https://github.com/achemguy/smi2qm/actions/workflows/dockerpush.yaml/badge.svg)](https://github.com/achemguy/smi2qm/actions/workflows/dockerpush.yaml)

Docker image of limited example Python program that generates quantum chemically determined molecular geometries for large batches of molecules from SMILES strings, using tight-binding density functional theory methods. This can be used for ligand-based cheminformatics screening of drug-candidate molecules.

The Docker image builds a Conda environment to manage all Python modules.

Information for users:
- Input is a single text file with individual SMILES strings in each line (e.g from ZINC database https://zinc20.docking.org/).
- Uses Python client of Open Babel to evaluate molecular charges, generate preliminary molecular geometries, and generate molecular fingerprints; see https://open-babel.readthedocs.io/en/latest/UseTheLibrary/PythonDoc.html).
- Uses Python client of the XTB program for tight-binding density functional theory (quantum chemistry approach) calculations; see https://github.com/grimme-lab/xtb-python.
- Uses Python client of MongoDB for data caching; see https://pymongo.readthedocs.io/en/stable/.

## Requires:
- Docker (https://www.docker.com/get-started)
- MongoDB (https://docs.mongodb.com/manual/installation/)

## Command line usage

1. Pull Docker image from Docker Hub:

   ```docker pull asimnajibi/smi2qm```

2. Run Docker image container, mounting local directory containing smiles files (e.g see SMILES/examples.smi) and specifying the client, database name and collection name. For example,

   ```docker run -it -v $(pwd)/SMILES:/smi2qm/SMILES --entrypoint ["conda", "run", "-n", "smi2qm", "python", "/smi2qm/smi2qm/main.py"] smi2qm:latest -c mongodb://localhost -d db_smi2qm -n coll_smi2qm```

3. Check stored data on MongoDB, view insights, manipulate, visualise, make queries

## To be expanded: Statistics of MongoDB data with NumPy
See smi2qm/npstats.py

Use ```--entrypoint ["conda", "run", "-n", "smi2qm", "python", "/smi2qm/smi2qm/npstats.py"]``` in ```docker run```

This will include tools for the entire data set.

To obtain a numpy array of atoms and corresponding atomic coordinates for a particular molecule, add option ```-s <'SMILES string'>``` or ```--smiles <'SMILES string'>```

## Other developments to add
The absence of the following two aspects may lead to inaccuracies in rare cases, but cheminformatics-based drug screening can provide useful verification.

1. XTB calculation of Hessian matrix of optimised molecular geometry and subsequent detection of imaginary frequencies leading to dump in failed-calculations MongoDB collection. Add reason of failure to the entry inserted into the failed-calculations MongoDB collection.
2. Determination of number of unpaired electrons: Would be useful for XTB calculation but cannot always be determined from SMILES string (e.g due to various possible configurations of d-orbital electrons in transition metals due to ligands).

## Other notes
The data cached in MongoDB should be used for conformer searching and cheminformatics applications.
