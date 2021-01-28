from setuptools import setup

setup(
    name='discrete_fuzzy_operators',
    version='1.0',
    packages=['discrete_fuzzy_operators'],
    url='',
    license='mit',
    author='marcmunar',
    author_email='marc.munar@uib.es',
    description='Set of algorithms for generating fuzzy operators in a finite chain',
    include_package_data=True,
    install_requires=[
        "numpy"
    ]
)
