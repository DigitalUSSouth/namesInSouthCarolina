# Names of SC
## A website that tells the stories of odd names in SC

README.md updated on 04.21.2019, for older versions, use [the old README.md](link)

### Prerequisites
- [Docker](https://docs.docker.com/) 
  - tested with version 18.09.0
- [docker-compose](https://docs.docker.com/compose/)
  - tested with version 1.23.2

### Quick Start
Run the following module to get a quickstart to the application

```bash
# Basic Git Clone and Download
git clone https://github.com/DigitalUSSouth/namesInSouthCarolina
cd namesInSouthCarolina

# Given you've installed Docker on your local machine, this command will
# a) Build the Docker Chain to the local machine
# b) Launch the Docker containers in detached mode, or without standard input
docker-compose up --build -d

# The following is a utilities command to load the database with the latest
# working data
# UNIX/Linux/Mac users only
./utils/loaddatabase.sh
```
If these steps don't introduce error, then you should be able to open your
web browser to [localhost](http://localhost:2019) and see the current working
version.

### Utilities
The Utils folder contains a couple of simple functions for ease of access.
```bash
# Load whatever is in the Database (outside of Users)
# using Django's fixtures feature
./utils/loaddatabase.sh

# Dump whatever is in the Database (outside of Users)
# using Django's fixtures feature
./utils/dumpdatabase.sh
```