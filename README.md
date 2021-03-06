# Couched Python Library

This package provides a (very limited) set of command-line utils to manipulate [CouchDB](http://couchdb.apache.org/) database.

Author & maintainer: Andrey Upadyshev <<oliora@gmail.com>>.

## What's Included

### couch-save

Save documents from CouchDB instance to the disk. 

Usage: `couch-save [options] <target_dir> <db_name> [<db_server>]`

Documents are saved in UTF-8 encoded JSON files.

### couch-load

Load a set of documents from the disk to CouchDB instance.

Simple usage: `couch-load [options] <docs_dir> <db_name> [<db_server>]`

Documents should be UTF-8 encoded JSON files with **json** extension.

**Run any tool with `-h` parameter to get all possible options.**


## Installation

Use [pip](http://www.pip-installer.org/en/latest/installing.html) for installation:

`pip install git+git://github.com/oliora/couched.git@v0.1`


## Prerequisites

* Python >= 2.7
* [couchdb-python](http://code.google.com/p/couchdb-python/) >= 0.7 (will be installed automatically by _pip_)


## Bug Reporting

Use [issue tracker](https://github.com/oliora/couched/issues).


## Contributing

Fork it, commit changes and create a pull request. Thank you!
