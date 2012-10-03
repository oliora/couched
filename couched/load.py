import os
from os import path
import argparse
import json
import couchdb
import fnmatch
import traceback
import codecs
from .util import DocFilter


def getCommandLineOptions():
    parser = argparse.ArgumentParser(description="Load CouchDB documents into DB")
    parser.add_argument('docs', help="Documents directory")
    parser.add_argument('db', help="Database name")
    parser.add_argument('server', help="Server URL. Default is: 'http://localhost:5984/'", default="http://localhost:5984/", nargs="?")

    parser.add_argument("-d", "--drop-db", action="store_true", help="Drop database before loading documents")
    parser.add_argument("-f", "--filter", help="Load only documents of type: d - design, u - user", choices='du')
    parser.add_argument("-o", "--overwrite", action="store_true", help="Owerwrite existing documents (skip otherwise)")

    return parser.parse_args()


def getDocId(p):
    res = os.path.splitext(p)[0]
    if os.sep != "/":
        res = res.replace(os.sep, "/")
    return res


def loadDocs(db, docsDir, overwrite=False, docFilter=DocFilter()):
    for root, dirs, files in os.walk(docsDir):
        for f in files:
            if fnmatch.fnmatch(f, "*.json"):
                fname = path.join(root, f)
                relfname = path.relpath(fname, docsDir)
                print "* Load '{0}'".format(relfname),
                try:
                    with codecs.open(fname, 'r', 'utf-8') as docFile:
                        doc = json.load(docFile)
                    if "_rev" in doc:
                        del doc["_rev"]
                    id = doc.get("_id", getDocId(relfname))
                    print "with id '{0}'...".format(id),

                    if not docFilter(id):
                        print "filtered, SKIPPED"
                        continue

                    if id in db:
                        if not overwrite:
                            print "already exists, SKIPPED"
                            continue
                        doc["_rev"] = db[id]["_rev"]
                        print "overwtiting,",
                    db[id] = doc
                    print "LOADED"
                except Exception:
                    print "error, SKIPPED"
                    traceback.print_exc()


def main():
    options = getCommandLineOptions()
    #print "Options:", options

    serverUrl = options.server
    dbName = options.db

    couch = couchdb.Server(serverUrl)

    print "Loading documents from '{0}' into '{2}' at '{1}'".format(path.abspath(options.docs), serverUrl, dbName)

    if options.drop_db and dbName in couch:
        print "Deleting database...",
        del couch[dbName]
        print "OK"        

    if dbName not in couch:
        print "Creating database...",
        couch.create(dbName)
        print "OK"

    loadDocs(couch[dbName], options.docs, options.overwrite, DocFilter(options.filter))

    print
    print "All is OK"


if __name__ == "__main__":
    main()