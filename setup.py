from distutils.core import setup

setup(
    name='Couched',
    version='0.1.0',
    author='Andrey Upadyshev',
    author_email='oliora@gmail.com',
    packages=['couched'],
    #scripts=['bin/couch-load.py','bin/couch-save.py'],
    #url='http://pypi.python.org/pypi/couched/',
    license='LICENSE.txt',
    description='CouchDB related command-line utils.',
    long_description=open('README.txt').read(),
    entry_points={
            'console_scripts': [
                'couch-load = couched.load:main',
                'couch-save = couched.save:main',
            ],
    },
    install_requires=[
        "couchdb >= 0.7.0",
    ],
)
