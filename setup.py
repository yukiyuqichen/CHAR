from setuptools import setup, find_packages

setup(
    name='char_converter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'os',
        'msgpack',
    ],
    author='Yuqi Chen',
    description='A library to convert variant Chinese characters to standard simplified or traditional characters.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
