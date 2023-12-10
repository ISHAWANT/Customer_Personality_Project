import os 
import logging 
from pathlib import Path 


while True:
    project_name = input('Enter your project name: ') 
    if project_name !='':
        break 
    
list_of_files=[
    f"src/{project_name}/__init__,py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "demo.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) 
    filedir,filename = os.path.split(filepath) 
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating a new directory at : {filedir} for file : {filename}") 
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass 
            logging.info(f"Creating a new file{filename} for path: {filepath}") 
    else:
        logging.info(f"file is already present at : {filepath}") 