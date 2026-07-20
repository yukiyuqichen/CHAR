from setuptools import setup, find_packages

setup(
    name='char_converter',
    version='0.51',
    author='Yuqi Chen',
    author_email='chenyuqi@hku.hk',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'msgpack',
    ],
    package_data={
        'char_converter': ['*.py', 'data/*.msgpack']
    },
    include_package_data=True,
    description='A library to convert variant Chinese characters to standard simplified or traditional characters.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)
