from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = None

# Read version from package.
from flow.__version__ import __version__

setup(name='flow',
      version=__version__,
      author='Lewis A. Marshall',
      author_email='lewis.a.marshall@gmail.com',
      url="http://lewisamarshall.github.io/flow/",
      classifiers=[
          "Programming Language :: Python",
          "Environment :: Console",
          "Intended Audience :: Science/Research",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],
      use_2to3=False,
      license='LICENSE',
      description='A package for calculating electrolyte properties.',
      long_description=long_description,
      packages=find_packages(),
      requires=['numpy', 'scipy', 'pint', 'click'],
      entry_points={'console_scripts': ['flow = flow.__main__:cli']},
      test_suite="flow.tests",
      )
