# smi2qm
Limited example program that obtains quantum chemical data for large batches of molecules
Requires:
GitHub (https://desktop.github.com/)
Docker (https://www.docker.com/get-started)
MongoDB (https://docs.mongodb.com/manual/installation/)
MongoDB Compass (https://www.mongodb.com/try/download/compass) 

## Usage
1. clone git repository
```git clone https://github.com/asimnajibi/smi2qm```
2. In smi2qm directory, build Docker image
```docker build -t smi2qm:v1 .```
3. run Docker image container
```docker run -it -v $(pwd)/SMILES:/smi2qm/SMILES smi2qm:v1
4. check stored data on MongoDB Compass, view insights, manipulate, visualise
