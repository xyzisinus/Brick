import yaml
import sys
from pprint import pprint
from collections import defaultdict

d = yaml.load(open(sys.argv[1]))

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
        print superclass,'->',subclass
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
        print superclass,'->',tagsuperclass
        if get_key(d, medium) is not None:
            subclasses.extend(expand(get_key(d, medium), tagsuperclass))
    print 

    return subclasses

def type_expand(d, tagclasses=None, superclass=None):
    types = list_keys(d)
    subclasses = []
    type_to_subclasses = defaultdict(list)
    if tagclasses is not None:
        for typeclass in types:
            for tagclass in tagclasses:
                _newclass = '{0} {1}'.format(typeclass, tagclass)
                type_to_subclasses[typeclass].append(_newclass)
                print 'tt',superclass,'->',_newclass
                subclasses.append(_newclass)

    if superclass is not None:
        for typeclass in types:
            _newclass = '{0} {1}'.format(typeclass, superclass)
            print superclass,'->',_newclass
            type_to_subclasses[typeclass].append(_newclass)
            subclasses.append(_newclass)

    for typeclass in types:
        print 'typeclass',typeclass
        #TODO: handle the subclassing here
        subclasses.extend(expand(get_key(d, typeclass), tagclasses=type_to_subclasses[typeclass], supertag=typeclass))

    return subclasses

def synonym_expand(synonyms, tag, tagclasses):
    newtagclasses = []
    for synonym in synonyms:
        for tagclass in tagclasses:
            newtagclasses.append(tagclass.replace(tag, synonym))
    return newtagclasses

def expand(d, superclass=None, tagclasses=None, supertag=None):
    #print 'expand({0}, superclass={1}, tagclasses={2}, supertag={3}'.format(d, superclass, tagclasses, supertag)
    subclasses = []

    if tagclasses is None:
        tagclasses = []

    if d is None:
        return subclasses
    if 'subclasses' in d:
        subclasses.extend(subclass_expand(d['subclasses'], superclass))
    if 'media' in d:
        tagclasses.extend(media_expand(d['media'], superclass))
    if 'types' in d:
        tagclasses.extend(type_expand(d['types'], tagclasses=tagclasses))
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
