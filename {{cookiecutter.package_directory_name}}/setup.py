# import multiprocessing to avoid this bug (http://bugs.python.org/issue15881#msg170215)
import multiprocessing
assert multiprocessing
import re
from setuptools import setup, find_packages


def get_version():
    """
    Extracts the version number from the version.py file.
    """
    VERSION_FILE = '{{cookiecutter.package_name}}/version.py'
    mo = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', open(VERSION_FILE, 'rt').read(), re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError('Unable to find version string in {0}.'.format(VERSION_FILE))


install_requires = [
]

tests_require = [
]

docs_require = [
]

extras_require = {
    'dev': tests_require + docs_require,
}

setup(
    name='{{cookiecutter.package_name}}',
    version=get_version(),
    description='{{cookiecutter.description}}',
    long_description='{{cookiecutter.description}}',
    url='{{cookiecutter.github_url}}',
    author='{{cookiecutter.name}}',
    author_email='{{cookiecutter.email}}',
    keywords='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    zip_safe=False,
)
