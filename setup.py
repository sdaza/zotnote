from setuptools import setup, find_packages

setup(name='zotnote',
      version='0.1.0',
      description='Export Zotero notes to a CSV file',
      url='http://github.com/sdaza/zotnote',
      author='Sebastian Daza',
      author_email='sebastian.daza@gmail.com',
      license='MIT',
      packages=['zotnote'],
      install_requires=['pyzotero', 'pandas', 'numpy'],
      zip_safe=False)