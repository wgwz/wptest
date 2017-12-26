""""""
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('backend/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='wptest',
    version=version,
    url='https://github.com/wgwz/wptest/',
    license='MIT',
    author='wgwz',
    author_email='klawlor419@gmail.com',
    description='flask/js app',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[],
    # entry_points='''
    #     [console_scripts]
    #     flask=flask.cli:main
    # '''
)
