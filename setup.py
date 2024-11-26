from setuptools import setup, find_packages

setup(
    name='drone_simulation',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'control',
        'sympy',
    ],
)
