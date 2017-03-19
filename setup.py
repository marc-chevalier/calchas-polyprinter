#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='calchas_polyprinter',
    version='0.1',
    description='A collection of printer for Calchas',
    url='https://github.com/ProjetPP',
    author='Marc Chevalier',
    author_email='calchas@marc.chevalier',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'calchas_datamodel',
    ],
    packages=[
        'calchas_polyprinter',
    ],
)
