# Subsystem Definitions

I decided to make a little tool for writing YAML specifications of a subsystem, and having that automatically append the rows onto the `TagSets.csv` file.

Take a look at `Electrical.yaml` for an example.

The tool gets invoked like:

```
$ python yaml2csv.py Electrical.yaml
```
