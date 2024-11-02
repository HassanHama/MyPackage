from setuptools import setup, find_packages

setup(
    name='MyPackage',
    version='0.1',
    packages=find_packages(exclude=['Tests']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('readme.md').read(),
    install_requires=['numpy'],
    url='https://github.come/HassanHama/MyPackage',
    author='Mohammed Alhassan',
    author_email='malhassan8430@gmail.com'
)