from setuptools import setup
import sys


if sys.version < "2.7":
    raise Exception("Couched needs Python 2.7 or above")


LONG_DESCRIPTION = open('README.txt').read()

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Database :: Front-Ends',
]


setup(
    name='Couched',
    version='0.1.0',
    author='Andrey Upadyshev',
    author_email='oliora@gmail.com',
    packages=['couched'],
    url='https://github.com/oliora/couched/',
    license='MIT',
    description='CouchDB related command-line utils.',
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    platforms=['any'],
    entry_points={
            'console_scripts': [
                'couch-load = couched.load:main',
                'couch-save = couched.save:main',
            ],
    },
    install_requires=[
        "couchdb >= 0.7.0",
    ],
    zip_safe = True,
)