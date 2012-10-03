import os
from os import path
import argparse
import json
import couchdb
import shutil
import traceback
import codecs
from .util import DocFilter


def getCommandLineOptions():
    parser = argparse.ArgumentParser(description="Save CouchDB documents from DB")
    parser.add_argument('docs', help="Documents directory")
    parser.add_argument('db', help="Database name")
    parser.add_argument('server', help="Server URL. Default is: 'http://localhost:5984/'", default="http://localhost:5984/", nargs="?")

    parser.add_argument("-f", "--filter", help="Save only documents of type: d - design, u - user", choices='du')
    parser.add_argument("-o", "--overwrite", action="store_true", help="Owerwrite existing documents (skip otherwise)")

    return parser.parse_args()


def getDocPath(id):
    return path.join(*id.split('/'))+'.json'


def saveDocs(db, docsDir, overwrite=False, docFilter=DocFilter()):
	for docId in db:
		docPath = getDocPath(docId)
		print "Saving document '{0}' into '{1}'...".format(docId, docPath),

		if not docFilter(docId):
			print "filtered, SKIPPED"
			continue		

		docPath = path.join(docsDir, docPath)
		try:
			if path.exists(docPath):
				if not overwrite:
					print "already exists, SKIPPED"
					continue
				print "overwriting,",

			docDir = path.dirname(docPath)
			if not path.exists(docDir):
				os.makedirs(docDir)

			doc = db[docId]
			with codecs.open(docPath, 'w', 'utf-8') as docFile:
				json.dump(doc, docFile, ensure_ascii=False, indent=2)
			print "SAVED"
		except Exception:
			print "error, SKIPPED"
			traceback.print_exc()


def main():
    options = getCommandLineOptions()
    #print "Options:", options

    serverUrl = options.server
    dbName = options.db

    couch = couchdb.Server(serverUrl)

    print "Saving documents from '{0}' at '{1}' into '{2}'".format(serverUrl, dbName, path.abspath(options.docs))

    saveDocs(couch[dbName], options.docs, options.overwrite, DocFilter(options.filter))

    print
    print "All is OK"


if __name__ == "__main__":
    main()