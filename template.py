import os
from pathlib import Path
import logging

# basic logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# setting a variable for project name
project_name = "text_summarizer"


# setting up the filr structure
list_of_files = [
    # in .github we setup the YAML file. 
    # This is used for CI/CD deployment automatically(take code from github and upload to cloud)

    ".github/workflows/.gitkeep",
    # init constructor file is needed to setup the project name folder as local package
    # helps you import functionalities from differect folders
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "reseach/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating emmpty file: {filename}")
    else:
        logging.info(f"{filename} already exists")