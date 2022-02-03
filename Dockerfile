# base image
FROM conda/miniconda3
RUN apt update -y  && apt install -y build-essential && apt-get install -y  build-essential
RUN apt-get install -y vim

# work directory
RUN mkdir /app
WORKDIR /app
ADD . /app/

# Conda environment:
RUN conda env create -f environment.yaml

# run image
ENTRYPOINT ["conda", "run", "-n", "smi2qm", "python", "/app/smi2qm/main.py"]

