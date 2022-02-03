# base image
FROM conda/miniconda3
RUN apt update -y  && apt install -y build-essential && apt-get install -y  build-essential
RUN apt-get install -y vim

# work directory
RUN mkdir /app
WORKDIR /app
ADD . /app/

# install XTB
RUN wget https://github.com/grimme-lab/xtb/releases/tag/v6.4.1/xtb-6.4.1-linux-x86_64.tar.xz
RUN tar xfv xtb-6.4.1-linux-x86_64.tar.xz
ENV xtb = /app/xtb-6.4.1/bin/xtb
RUN rm -f xtb-6.4.1-linux-x86_64.tar.xz

# create Conda environment from yaml file listing all relevant packages:
RUN conda env create -f environment.yaml

# run image
ENTRYPOINT ["conda", "run", "-n", "smi2qm", "python", "/app/smi2qm/main.py"]

