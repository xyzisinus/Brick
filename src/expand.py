import yaml
import sys
from pprint import pprint
from collections import defaultdict

d = yaml.load(open(sys.argv[1]))

#### BRICK part
from rdflib import Graph, Namespace, URIRef, Literal
import rdflib
RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
OWL = Namespace('http://www.w3.org/2002/07/owl#')
BRICK = Namespace('https://brickschema.org/schema/1.0.1/Brick#')
BF = Namespace('https://brickschema.org/schema/1.0.1/BrickFrame#')
BRICKTAG = Namespace('https://brickschema.org/schema/1.0.1/BrickTag#')
g = rdflib.Graph()
g.bind('rdf', RDF)
g.bind('rdfs', RDFS)
g.bind('brick', BRICK)
g.bind('bf', BF)
g.bind('btag', BRICKTAG)

def fix_name(name):
    name = name.replace(' ','_')
    return name

def emit_class(name):
    name = fix_name(name)
    g.add((BRICK[name], RDF.type, OWL.Class))
    #for tag in name.split('_'):
    #    g.add((BRICKTAG[tag], RDF.type, BF["Tag"]))
    #    g.add((BRICK[name], BF.usesTag, BRICKTAG[tag]))
    pass

def emit_subclass(name, parentname):
    name = fix_name(name)
    parentname = fix_name(parentname)
    emit_class(name)
    emit_class(parentname)
    g.add((BRICK[name], RDFS.subClassOf, BRICK[parentname]))

def emit_synonym(name, synonym):
    name = fix_name(name)
    synonym = fix_name(synonym)
    if name == synonym:
        return
    print 'SYNONYM',name,synonym
    emit_class(name)
    emit_class(synonym)
    g.add((BRICK[name], BF.equivalentTagSet, BRICK[synonym]))

##########################################

def list_keys(d):
    things = d if isinstance(d, list) else d.keys()
    newthings = []
    for thing in things:
        if isinstance(thing, dict):
            newthings.extend(thing.keys())
        else:
            newthings.append(thing)
    return newthings

def get_key(d, key):
    if isinstance(d, dict):
        return d.get(key)
    if isinstance(d, list):
        for i in d:
            val = get_key(i,key)
            if val is not None:
                return val
    return

def subclass_expand(d, superclass):
    subclasses = []
    for subclass, defn in d.items():
        print 'se',superclass,'->',subclass
        emit_subclass(subclass, superclass)
        subclasses.append(subclass)
        subclasses.extend(expand(defn, subclass))
    return subclasses

def media_expand(d, superclass):
    if superclass is None:
        return []
    subclasses = []

    mediaclasses = list_keys(d)

    for medium in mediaclasses:
        tagsuperclass = '{0} {1}'.format(medium, superclass)
        subclasses.append(tagsuperclass)
        print '1',superclass,'->',tagsuperclass
        emit_subclass(tagsuperclass, superclass)
        if get_key(d, medium) is not None:
            subclasses.extend(expand(get_key(d, medium), tagsuperclass))
    print 

    return subclasses

def type_expand(d, tagclasses=None, superclass=None):
    types = list_keys(d)
    print types
    subclasses = []
    type_to_subclasses = defaultdict(list)
    if tagclasses is not None:
        for typeclass in types:
            for tagclass in tagclasses:
                _newclass = '{0} {1}'.format(typeclass, tagclass)
                type_to_subclasses[typeclass].append(_newclass)
                print 'tt',superclass,'->',_newclass
                emit_subclass(_newclass, superclass)
                subclasses.append(_newclass)

    if superclass is not None:
        for typeclass in types:
            _newclass = '{0} {1}'.format(typeclass, superclass)
            print 'st',superclass,'->',_newclass
            emit_subclass(_newclass, superclass)
            type_to_subclasses[typeclass].append(_newclass)
            subclasses.append(_newclass)

    for typeclass in types:
        print 'typeclass',typeclass, 'superclass', superclass
        #TODO: handle the subclassing here
        print 'tagclasses', type_to_subclasses[typeclass], 'supertag',typeclass
        for tt in type_to_subclasses[typeclass]:
            subclasses.extend(expand(get_key(d, typeclass), supertag=typeclass, superclass=tt))
        #subclasses.extend(expand(get_key(d, typeclass), tagclasses=type_to_subclasses[typeclass], supertag=typeclass, superclass=superclass))

    return subclasses

def synonym_expand(synonyms, tag, tagclasses):
    newtagclasses = []
    for synonym in synonyms:
        if len(tagclasses) == 0:
            emit_synonym(tag, synonym)
        for tagclass in tagclasses:
            synonymclass = tagclass.replace(tag, synonym)
            newtagclasses.append(synonymclass)
            emit_synonym(tagclass, synonymclass)
    return newtagclasses

def expand(d, superclass=None, tagclasses=None, supertag=None):
    #print 'expand({0}, superclass={1}, tagclasses={2}, supertag={3}'.format(d, superclass, tagclasses, supertag)
    subclasses = []
    if supertag is None:
        supertag = superclass

    if tagclasses is None:
        tagclasses = []

    if d is None:
        return subclasses
    if 'subclasses' in d:
        print 'asdfasfd',superclass
        subclasses.extend(subclass_expand(d['subclasses'], superclass))
    if 'media' in d:
        tagclasses.extend(media_expand(d['media'], superclass))
    if 'types' in d:
        tagclasses.extend(type_expand(d['types'], tagclasses=tagclasses, superclass=superclass))
        tagclasses.extend(type_expand(d['types'], superclass=superclass))
    if 'synonyms' in d:
        tagclasses.extend(synonym_expand(d['synonyms'], supertag, tagclasses))
        tagclasses.extend(synonym_expand(d['synonyms'], supertag, subclasses))

    subclasses.extend(tagclasses)

    return subclasses

for r, defn in d.items():
    print '-'*10
    print r
    pprint(expand(defn, r))

g.serialize(destination='Brick.ttl',format='turtle')
print len(g)
