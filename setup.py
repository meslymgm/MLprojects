from setuptools import find_packages,setup
from typing import List

hypenedot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''This fn will return the list of requirements'''
    requirements = []
    with open(file_path) as fileobject:
        requirements = fileobject.readlines()
        [req.replace("\n","") for req in requirements]

        if hypenedot in requirements:
            requirements.remove(hypenedot)
    return requirements




setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Mesly',
    author_email='meslymathews@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)