# smi2qm
[![CI Pipeline](https://github.com/asimnajibi/smi2qm/actions/workflows/ci.yaml/badge.svg)](https://github.com/asimnajibi/smi2qm/actions/workflows/ci.yaml)

Limited example program that obtains quantum chemical data for large batches of molecules

Requires:
- Git (https://desktop.github.com/)
- Docker (https://www.docker.com/get-started)
- MongoDB (https://docs.mongodb.com/manual/installation/)
- MongoDB Compass (https://www.mongodb.com/try/download/compass) 

## Command line usage
1. Clone git repository

   ```git clone https://github.com/asimnajibi/smi2qm```

2. In smi2qm directory, build a Docker image

   ```docker build -t smi2qm:v1 .```

3. Run Docker image container, mounting local directory containing smiles files and specifying the client, database name and collection name. For example,

   ```docker run -it -v $(pwd)/SMILES:/smi2qm/SMILES smi2qm:v1 -c mongodb://localhost:27017 -d db_smi2qm -n coll_smi2qm```

4. Check stored data on MongoDB Compass, view insights, manipulate, visualise, make queries
