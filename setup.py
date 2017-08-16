from setuptools import setup
import setuptools

long = '''
A python wrapper for the Vidme API

Currently at the very start
'''

setup(name="vidme.py",
	  version="0.1.0.dev1",
	  description="A python wrapper for the Vidme API",
	  long_description=long,
	  url="https://github.com/Zakru/vidme.py",
	  author="Zakru",
	  author_email="sakari.leukkunen@gmail.com",
	  license="MIT",
	  classifiers=[
	      "Development Status :: 1 - Planning",
		  "Intended Audience :: Developers",
		  "Topic :: Software Development",
		  "License :: OSI Approved :: MIT License",
		  "Programming Language :: Python :: 3"
	  ],
	  keywords="vidme api wrapper",
	  packages=setuptools.find_packages(),
	  install_requires=["requests"],
	  python_requires=">=3")