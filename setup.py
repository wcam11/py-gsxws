from setuptools import setup, find_packages
from gsxws.core import VERSION

setup(
    name="gsxws",
    version=VERSION,
    description="Library for communicating with GSX Web Services API.",
    long_description=open('README.rst', encoding='utf-8').read(),
    install_requires=['PyYAML', 'lxml'],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="gsx, python",
    author="Filipp Lepalaan",
    author_email="filipp@fps.ee",
    url="https://github.com/filipp/py-gsxws",
    download_url="https://github.com/filipp/py-gsxws/tarball/0.55",
    license="BSD",
    packages=find_packages(),
    package_data={'gsxws': ['products.yaml', 'langs.json']}
)
