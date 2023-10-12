try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(description = 'My Project',
      author = 'turtle',
      version = '0.1',
      install_requires = ['nose'],
      packages = ['NAME'],
      scripts = [],
      name = 'projectname'
      )


