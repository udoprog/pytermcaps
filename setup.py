from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='py-termcaps',
      version=version,
      description="Python OO wrapper for detecting terminal capabilities",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='John-John Tedro',
      author_email='johnjohn.tedro@gmail.com',
      url='http://github.com/udoprog/py-termcaps',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
