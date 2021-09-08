from codecs import open
from os import path
from setuptools import setup

try:
    # Depend on pypandoc for turning markdown readme into RST because
    # PyPI doesn't yet support this.
    import pypandoc

    here = path.abspath(path.dirname(__file__))
    long_description = pypandoc.convert("README.md", "rst")

except ImportError:
    here = path.abspath(path.dirname(__file__))

    # Get the long description from the relevant file
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='discrete_fuzzy_operators',
    version='1.8',
    packages=['discrete_fuzzy_operators'],
    url='https://github.com/mmunar97/discrete-fuzzy-operators',
    license='mit',

    author='marcmunar',
    author_email='marc.munar@uib.es',

    description='Pure Python implementation of the main fuzzy discrete operators defined in a finite chain',
    long_description=long_description,
    keywords='discrete fuzzy operators, discrete connectives, discrete fuzzy numbers, ordinal decision making',

    include_package_data=True,
    install_requires=[
        "numpy",
        "plotly",
        "pandas",
        "numba"
    ]
)
