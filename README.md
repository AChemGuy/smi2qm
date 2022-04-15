# smi2qm
[![CI Pipeline](https://github.com/asimnajibi/smi2qm/actions/workflows/ci.yaml/badge.svg)](https://github.com/asimnajibi/smi2qm/actions/workflows/ci.yaml) [![Docker Container Push Pipeline](https://github.com/asimnajibi/smi2qm/actions/workflows/dockerpush.yaml/badge.svg)](https://github.com/asimnajibi/smi2qm/actions/workflows/dockerpush.yaml)

Limited example program that obtains quantum chemical data for large batches of molecules, from SMILES strings.

Requires:
- Docker (https://www.docker.com/get-started)
- MongoDB (https://docs.mongodb.com/manual/installation/)

## Command line usage

1. Pull Docker image from Docker Hub:

```docker pull asimnajibi/smi2qm```

2. Run Docker image container, mounting local directory containing smiles files and specifying the client, database name and collection name. For example,

   ```docker run -it -v $(pwd)/SMILES:/smi2qm/SMILES --entrypoint ["conda", "run", "-n", "smi2qm", "python", "/smi2qm/smi2qm/main.py"] smi2qm:latest -c mongodb://localhost -d db_smi2qm -n coll_smi2qm```

3. Check stored data on MongoDB, view insights, manipulate, visualise, make queries

## In progress: statistics of MongoDB data with numpy
See smi2qm/npstats.py

Use ```--entrypoint ["conda", "run", "-n", "smi2qm", "python", "/smi2qm/smi2qm/npstats.py"]``` in ```docker run```

This will include tools for the entire data set.

To obtain a numpy array of atoms and corresponding atomic coordinates for a particular molecule, add option ```-s <'SMILES string'>``` or ```--smiles <'SMILES string'>```
