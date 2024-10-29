from setuptools import find_packages, setup
#automaticaaly find out all the packages in my ml app(our directory)
from typing import List

HYPEN_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements 

  
#consider it(parametrs in setup) as a metadata info
setup(
    name='mlProject',
    version='0.0.1', #keep on updating with the next versions
    author='Naira',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  #mention all req u want

)

#how it will find all the packeges in this project?
#find package will see in how many folders u have __init__.py file
# # and will consider the src(in our case) as a package
# and it will try to build this 
# so that we can import it anywhere in the project