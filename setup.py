from setuptools import find_packages
from setuptools import setup
import subprocess

REQUIRED_PACKAGES = ['nltk','tqdm','numpy','configparser']
#,'pickle','json','pprint'

setup(
    name='hadan',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='My trainer application package.'
)


cmd = ['/usr/bin/python' ,'-m', 'nltk.downloader','punkt']
subprocess.Popen(cmd)
print(cmd,'ok')

