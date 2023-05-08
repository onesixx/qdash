from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='alyxdash',
    version='0.1',
    author='onesixx',
    author_email='onesixx@nate.com',
    description='A Python package for dashboard',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/onesixx/alyxdash',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'numpy>=1.24.3',
        'pandas>=2.0.1',
        'matplotlib>=3.7.1',
        'dash>=2.9.3',
        'dash-bootstrap-components>=1.4.1'
    ],
)
