from setuptools import setup,find_packages
from typing import List

Hypen_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hypen_E_DOT in requirements:
            requirements.remove(Hypen_E_DOT)
    
    return requirements

setup(
    name='RegressionProject',
    version='0.0.1',
    author='Animesh',
    author_email='animesh.sharma0406@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)