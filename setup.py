from setuptools import find_packages, setup

setup(name='dlvpy',
      version='1.0.0',
      description='Python library that map json/dictionary python to dlv solver and create results from dlv solver output to Python json/dictionary',
      author='Andrea Chiera',
      author_email='dlvpy@outlook.it',
      packages=find_packages(),
      install_requires=['antlr4-python3-runtime==4.9.3']
)