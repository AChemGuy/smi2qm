# smi2qm
[![CI Pipeline](https://github.com/asimnajibi/smi2qm/actions/workflows/ci.yaml/badge.svg)](https://github.com/asimnajibi/smi2qm/actions/workflows/ci.yaml)

Limited example program that obtains quantum chemical data for large batches of molecules, from SMILES strings

Requires:
- Git (https://desktop.github.com/)
- Docker (https://www.docker.com/get-started)
- MongoDB (https://docs.mongodb.com/manual/installation/)

## Command line usage
1. Clone git repository

   ```git clone https://github.com/asimnajibi/smi2qm```

2. In smi2qm directory, build a Docker image from the Dockerfile (1.5 GB, XTB program in Docker build requires Linux x86 64 bit architecture)

   ```docker build -t smi2qm:v1 .```

3. Run Docker image container, mounting local directory containing smiles files and specifying the client, database name and collection name. For example,

   ```docker run -it -v $(pwd)/SMILES:/smi2qm/SMILES --entrypoint ["conda", "run", "-n", "smi2qm", "python", "/smi2qm/smi2qm/main.py"] smi2qm:v1 -c mongodb://localhost -d db_smi2qm -n coll_smi2qm```

4. Check stored data on MongoDB Compass, view insights, manipulate, visualise, make queries

## In progress: statistics of MongoDB data with numpy
See smi2qm/npstats.py

Use ```--entrypoint ["conda", "run", "-n", "smi2qm", "python", "/smi2qm/smi2qm/npstats.py"]``` in ```docker run```

To obtain a numpy array of atoms and corresponding atomic coordinates for a particular molecule, specify add option ```-s <'SMILES string'>``` or ```--smiles <'SMILES string'>```
