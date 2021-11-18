# Base this container on the Python slim container image available from ACI.
# See Image Variants at https://hub.docker.com/_/python for information about different flavors of Python containers.
FROM python:3.7.4-slim

WORKDIR /src

# Copy connector and sample files to image
COPY ./connector ./connector
COPY ./samples/[SampleName] ./samples/[SampleName]

# Install simulator dependencies
RUN pip3 install -r ./connector/requirements.txt

# This will be the command to run the simulator
CMD python3 samples/ContosoUseCase/main.py
