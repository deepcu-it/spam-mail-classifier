from typing import List
from setuptools import setup,find_packages

HYPER_E_DOT = 'e .'
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file:
        packages=file.readlines()
        if HYPER_E_DOT in packages:
            packages.remove(HYPER_E_DOT)
    
    return packages

setup(
    name='Spam-mail-classifier-ML',
    version='0.0.1',
    author='Deep',
    author_email='deepghosal445@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)