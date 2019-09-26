from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef

BRICK_VERSION = '1.1.0'

BRICK = Namespace(f"https://brickschema.org/schema/{BRICK_VERSION}/Brick#")
TAG = Namespace(f"https://brickschema.org/schema/{BRICK_VERSION}/BrickTag#")
#BLDG = Namespace(f"https://brickschema.org/schema/{BRICK_VERSION}/ExampleBuilding#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
DCTERMS = Namespace("http://purl.org/dc/terms#")
SDO = Namespace("http://schema.org#")
SOSA = Namespace("http://www.w3.org/ns/sosa#")
A = RDF.type

def bind_prefixes(g):
    g.bind('rdf', RDF)
    g.bind('owl', OWL)
    g.bind('dcterms', DCTERMS)
    g.bind('sdo', SDO)
    g.bind('rdfs', RDFS)
    g.bind('skos', SKOS)
    g.bind('sosa', SOSA)
    g.bind('brick', BRICK)
    g.bind('tag', TAG)