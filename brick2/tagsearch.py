import IPython
import json
import yaml
import sys

def flatten(doc):
    tags = set()
    for key, taglist in doc.items():
        if isinstance(taglist, str):
            tags.add(taglist)
        else:
            tags = tags.union(taglist)
    return tags

__docs = list(yaml.load_all(open(sys.argv[1])))
_docs = {doc['id']: doc for doc in __docs}
_tagdocs = {doc['id']: flatten(doc) for doc in _docs.values()}

def printdoc(doc):
    print json.dumps(doc, indent=2)

def get_tags(tags, docs=_docs):
    """
    Return documents that contain the provided set of tags; set intersection
    """
    tagdocs = {doc['id']: flatten(doc) for doc in _docs.values()}
    results = {}
    s = set(tags)
    for k, doc in tagdocs.items():
        if s.issubset(doc):
            results[k] = _docs[k]
    return results

def get_scoped_tag(kvpairs, docs=_docs):
    """
    Returns documents which contains values for the provided keys:
    get_scoped_tag({'type': ['point','command']})
    """
    results = {}
    for kid, doc in docs.items():
        include = True
        for key, val in kvpairs.items():
            if include: include = (val == doc.get(key,'') or val in doc.get(key,[]))
        if include:
            results[kid] = doc
    return results

def get_scoped_tag_path(kvpairs, docs=_docs):
    """
    Keys can now be paths (isPartOf/isPartOf) etc. No wildcards yet
    """
    pass

#get_tags(['fan'])
IPython.embed()
