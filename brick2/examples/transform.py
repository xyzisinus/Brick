import yaml
import sys

docs = list(yaml.load_all(open(sys.argv[1])))
print "var data = ["
for doc in docs:
    print "{\n\tx:0, y:0,\n\ttable: ["
    for k,v in doc.items():
        if isinstance(v,list):
            print '\t\t{Tag: "%s", Value: %s},' % (k,v)
        else:
            print '\t\t{Tag: "%s", Value: "%s"},' % (k,v)
    print "\t]\n},"
print "];"
