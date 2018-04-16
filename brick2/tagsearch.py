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
    tagdocs = {doc['id']: flatten(doc) for doc in docs.values()}
    results = {}
    s = set(tags)
    for k, doc in tagdocs.items():
        if s.issubset(doc):
            results[k] = docs[k]
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
            if isinstance(val, list) and include:
                include = all((v in doc.get(key,[]) for v in val))
            elif include:
                include = (val == doc.get(key,'') or val in doc.get(key,[]))
        if include:
            results[kid] = doc
    return results

def pull_tags(tags, docs=_docs):
    ret = []
    for kid, doc in docs.items():
        ret.append({k: doc.get(k) for k in tags if k in doc})
    return ret

def get_scoped_tag_path(kvpairs, docs=_docs):
    """
    Keys can now be paths (isPartOf/isPartOf) etc. No wildcards yet
    """
    pass

from lark import Lark
from lark import Transformer

parser = Lark(r"""
    query: statement (";" statement)*
    statement: list
        | dict
        | extract
    tag: CNAME
    taglist: tag [tag*]
    list: "|" taglist
    dict: tag ":" taglist
    extract: ">" taglist

    %import common.CNAME
    %import common.WS
    %ignore WS

""",start='query')
class QueryTransformer(Transformer):
    def __init__(self):
        self._use = _docs
        Transformer.__init__(self)

    def list(self, (l,)):
        self._use = get_tags(l, docs=self._use)
        return l

    def taglist(self, t):
        return list(t)

    def dict(self, items):
        key = items[0]
        values = items[1]
        self._use = get_scoped_tag({key: values}, docs=self._use)
        return {key: values}

    def statement(self, (s,)):
        return s

    def extract(self, (tl,)):
        self._use = pull_tags(tl, docs=self._use)
        return tl

    def tag(self, (t,)):
        return t.value

def query(q):
    t = parser.parse(q)
    qt=  QueryTransformer()
    qt.transform(t)
    return qt._use

def queryp(q):
    printdoc(query(q))

#print query("| air temperature")
#
#print query("substance: air return")
#
#print query("""
#| air temperature
#substance: air return
#""")

IPython.embed()
