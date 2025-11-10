'''
the setup.py file is an essential part of packaging and distributing Python projects.
it is used by setup tools (or distutils in older python  versions) to define the configuration
of your project, such as its metadata, dependencies and more
'''
from setuptools import find_packages,setup
'find_package will search for __init__.py file where ever it will be, and then the parnet folder '
'that will be having it will become the package in itself'
'setup is responsible to provide all the information regarding the project over here'
from typing import List

def get_requirements() -> List[str]:
    '''
    this function will return list of requirements
    '''
    requirement_lst:List[str]=[]


    try:

        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines = file.readlines()
            ##Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore the empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst
#print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Dipika Chandra",
    author_email="dipikachandra24@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

        

