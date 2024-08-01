from setuptools import setup, find_packages

setup(
    name='char_converter',
    version='0.38',
    author='Yuqi Chen',
    author_email='cyq0722@pku.edu.cn',
    packages=find_packages(),
    install_requires=[
        'msgpack',
        'setuptools',
    ],
    package_data={
        'char_converter': ['*.py', 'data/*.msgpack']
    },
    include_package_data=True,
    description='A library to convert variant Chinese characters to standard simplified or traditional characters.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)
