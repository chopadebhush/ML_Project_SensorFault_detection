from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e."


def get_requirements(file_path: str) -> List[str]:
    """
    Get requirement function is use to install all 
    requirement which are present in requirements.txt file
    through setup function. 

    Args:
        file_path (str): requirements.txt file path

    Returns:
        List[str]: all requirements in list form  
    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if (HYPEN_E_DOT in requirements):
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="Sensor_fault_detection",
    version="0.0.1",
    author="Bhushan",
    author_email="chopadebhush@gmail.com",
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)
