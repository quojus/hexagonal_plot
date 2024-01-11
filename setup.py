from setuptools import setup, find_packages

setup(
    name='hexagonal_plot',
    version='1.1.4',
    packages=find_packages(),
    description='Dieses Skript enthält eine Funktion plot_hexagonal_grid, die es ermöglicht, Daten in einem sechseckigen Gitter mit Matplotlib zu visualisieren.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Falk mit gpt',
    url='https://github.com/quojus/hexagonal_plot',
        install_requires=[
        'matplotlib',
        'numpy'
    ],
    python_requires='>=3.6',
)
