from setuptools import setup,find_packages
from typing import List 

PROJECT_NAME = 'Machine Learning Project' 
VERSION = '0.0.1' 
AUTHOR = 'ISHAWANT KUMAR'
DESCRIPTION  = "This is our machine learning customer personality project"
HYPHEN_E_DOT = "-e ." 
REQUIREMENT_FILE_NAME = "requirements.txt" 

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines() 
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list] 
        
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
    
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires = get_requirements_list()
)