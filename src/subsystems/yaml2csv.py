"""
Converts yaml file like Electrical.yaml into the CSV file we use for BuildBrick
"""
import yaml
import sys
import pandas as pd

d = yaml.load(open(sys.argv[1]))

tagsets = pd.read_csv('../TagSets.csv')

def expand(d, prefix=""):
    for classname, defn in d.items():
        name = prefix+">"+classname if prefix else classname
        if defn is None:
            yield {'Dimension': prefix, 'TagSet': classname}
            continue
        subclasses = defn.pop('classes', None)
        entry = defn.copy()
        entry['Dimension'] = prefix
        entry['TagSet'] = classname
        if 'hasSynonyms' in entry:
            entry['hasSynonym'] = ', '.join(entry.pop('hasSynonyms'))
        if prefix:
            yield entry
        if subclasses:
             for r in expand(subclasses, name):
                yield r

for r in expand(d):
    tagsets = tagsets.append(r, ignore_index=True)
    print r
tagsets.to_csv('TagSets.csv',index=False)
