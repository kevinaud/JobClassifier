from setuptools import setup

setup(name='classifier',
	  version='1.0',
	  description='Job Listing Classifier',
	  author='Kevin Aud',
	  author_email='Kevin_Aud@baylor.edu',
	  packages=['classifier'],
	  setup_requires=['pytest-runner'],
	  tests_require=['pytest'],
)
