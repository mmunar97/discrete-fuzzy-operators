from codecs import open
from os import path
from setuptools import setup

try:
    import pypandoc
    # Depend on pypandoc for turning markdown readme into RST because
    # PyPI doesn't yet support this.
    long_description = pypandoc.convert_file(r'PROJECT_DESCRIPTION.md', "rst", format='md')

except ImportError:
    here = path.abspath(path.dirname(__file__))

    # Get the long description from the relevant file
    with open(path.join(here, r'PROJECT_DESCRIPTION.md'), encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='discrete_fuzzy_operators',
    version='1.13.2',
    packages=['discrete_fuzzy_operators'],
    url='https://github.com/mmunar97/discrete-fuzzy-operators',
    license='mit',

    author='marcmunar',
    author_email='marc.munar@uib.es',

    description='Pure Python implementation of the main fuzzy discrete operators defined in a finite chain',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='discrete fuzzy operators, discrete connectives, discrete fuzzy numbers, ordinal decision making',

    include_package_data=True,
    install_requires=[
        "pypandoc",
        "numpy",
        "plotly",
        "pandas",
        "numba"
    ]
)
