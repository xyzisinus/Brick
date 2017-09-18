# Subsystem Definitions

I decided to make a little tool for writing YAML specifications of a subsystem, and having that automatically append the rows onto the `TagSets.csv` file.

Take a look at `Electrical.yaml` for an example.

The tool gets invoked like:

```
$ python yaml2csv.py Electrical.yaml
```

## Structuring Subsystem Definitions

This is how to write a YAML file defining the set of classes making up a subsystem hierarchy.

The structure is a nested set of key-value pairs. Class definitions are keyed by the name of that class. Supported keys describing each class are:

- `classes`: nested classname -> class definition structures here for subclasses of this class
- `Definition`: a textual definition of this class
- `Reference`: link to external deocumentation
- `hasSynonyms`: list of alternative names for this class

Example:


```yaml
Bus:                    # define the 'Bus' class
    classes:            # define the set of 'Bus' subclasses
        Circuit:        # 'Circuit' is a subclass of 'Bus'
            Definition: specific supply from distribution panel
        Distribution Board: # 'Distribution Board' is also a subclasses of 'Bus', but it has some synonyms too
            hasSynonyms: [Circuit Panel, Consumer Unit]
        Panel Board:
            hasSynonyms: [Switch Board]
            classes:                # subclasses of Panel Board
                High Voltage Switch Board:
                    Definition: high voltage switch board

```
