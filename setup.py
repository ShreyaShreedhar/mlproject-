from setuptools import find_packages,setup
from typing import List
hypen_e_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requiremnets=file_obj.readlines()
        [req.replace("\n"," ")for req in requirements]

        if hypen_e_dot in requiremnets:
            requirements.remove(hypen_e_dot)

setup(
    name='mlproject',
    version='0.0.1',
    author="shreya",
    author_email='shreyakatti650@gmail.com',
    packages=find_packages(),
    install_required=get_requirements('requirements.txt')

)