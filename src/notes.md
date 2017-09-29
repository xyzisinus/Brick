Goal is to have a declarative specification that generates a consistent collection of tagsets

Example from keith:

    Zone_air_temperature:
      setpoint_states:[[occupied,unoccupied],[heating,cooling]]
        alarms: true

Some issues with the hierarchy:

- really two things we want to communicate:
    1. what kind of system is a tagset *associated* with:
        - use "is Part Of"; maybe as part of the Brick definition?
    2. increasing levels of specificity/functionality:
        - this is really what classes are for. Valve -> Heating Valve, for example

- the class hierarchy is co-opting the structure to do the former. This is BAD!:
    - for example, subclasses of an AHU include a "preheat valve VFD"
- going to need to switch to some other kind of relationship for this:
    - maybe "usesEquipment"; this gets inherited DOWN the hierarchy
    - the "compiler" throws an exception/error if the target of "usesEquipment" is
      not defined elsewhere in Brick


How to do the declarative specification:

## subclasses

```yaml
    Point:
        subclasses:
            Alarm:
            Command:
            Meter:
            Sensor:
```

This is straightforward. We can carry this method all the way down through classes like "Medium Temperature Hot Water Discharge Temperature Sensor".
Problems with this:
- hierarchy could get unmanageable rather quickly. Large amounts of nesting, etc
- this is not explicit about the tags:
    - tags could be "inferred" by doing whitespace delimiting, and then cross-referencing
      with the standard set of tags defined elsewhere.

Could we adopt a more principled approach?

Case Study: CO2 sensors

```
Point>Sensor,CO2 Differential Sensor,
Point>Sensor,CO2 Level Sensor,
Point>Sensor,CO2 Sensor,
Point>Sensor>CO2 Sensor,Outside Air CO2 Sensor,
Point>Sensor>CO2 Sensor,Return Air CO2 Sensor,
```

So far we have:

```yaml
Point:
    subclasses:
        Sensor:
            types:
                CO2:
                    media: [Air]
                    types: [Outside, Return]
                    subclasses:
                        CO2 Differential Sensor:
                        CO2 Level Sensor:
```

This is exploring the possibility of parameterizing the construction of tagsets. For CO2 sensor,
the produced tagsets would be the cross product of "media" and "types":
- Outside Air CO2 Sensor
- Return Air CO2 Sensor

Augemented by the further subclasses:
- CO2 Differential Sensor
- CO2 Level Sensor
- Return Air CO2 Differential Sensor
- Outside Air CO2 Differential Sensor
- Return Air CO2 Level Sensor
- Outside Air CO2 Level Sensor

it might be more consistent to describe the above using:

```yaml
Point:
    subclasses:
        Sensor:
            types:
                CO2:
                    media: [Air]
                    types: [Outside, Return]
                    subtypes: [Differential, Level]
```

If one of our subtypes has additional subtypes, we could do

```yaml
Point:
    subclasses:
        Sensor:
            types:
                CO2:
                    media: [Air]
                    types: [Outside, Return]
                    subtypes:
                        - Differential
                            types: Inverse # i dunno maybe this exists
                        - Level
```

which would then produce:
- Outside Air CO2 Sensor
- Return Air CO2 Sensor
- Return Air CO2 Differential Sensor
- Return Air CO2 Inverse Differential Sensor  **<--- new**
- Outside Air CO2 Differential Sensor
- Outside Air CO2 Inverse Differential Sensor  **<--- new**
- Return Air CO2 Level Sensor
- Outside Air CO2 Level Sensor

This is all well and good until we run into a scenario where we have subtypes for only one of our types.
Luckily, we can use YAML's flexible syntax to expand out the "types" list and give subtypes to only
one element of that list.

```yaml
Point:
    subclasses:
        Sensor:
            types:
                CO2:
                    media: [Air]
                    types:
                        - Outside
                        - Return
                            subtypes:
                                - Differential
                                    types: Inverse # i dunno maybe this exists
                                - Level
```

which would then produce:
- Outside Air CO2 Sensor
- Return Air CO2 Sensor
- Return Air CO2 Differential Sensor
- Return Air CO2 Inverse Differential Sensor
- Return Air CO2 Level Sensor

---

At this point, we have the following issues:
1. what are the keys we use to enumerate the tag dimensions (e.g. media, types, etc?)
2. what is the relationship between tag-generated tagsets and explicit subclasses


What are the keys we use to enumerate the tag dimensions (e.g. media, types, etc?)

------


What is the relationship between tag-generated tagsets and explicit subclasses?

Classes and subclasses contain full names.
Various tags can be associated with a class. So far there are two dimensions of tags:
- media: air, water, etc
- types: additional modifiers for the above: outside, return, supply, etc

Per the YAML format, we can specify tags like this

```yaml
types: [Outside, Return, Supply]
```

which is helpful if there's no extra information about those types.

However, we may want to attach certain properties to specific tags.
In that case, we can use an alternate YAML format to present the list of tags
as a list of dictionaries. We can have subclasses OR other tags (types and media)
here. Its basically just like writing classes, but you can be a little more succinct,
and its easier to see the structure. Its best to specify the classes directly if they
are super specific and you want to compress the nesting of tags it would take to generate that name.

```yaml
Temperature Sensor:
    media:
        - Air:
            types:
                - Discharge
                - Zone
                - Exhaust
    subclasses:
        Outside Air Lockout Temperature Differential Sensor:
```

generates the following:

```
Temperature Sensor
Air Temperature Sensor
Discharge Air Temperature Sensor
Zone Air Temperature Sensor
Exhaust Air Temperature Sensor
Outside Air Lockout Temperature Differential Sensor:
```

Now all together:

```
Sensor:         # <--- class name; standalone (i.e. this is the name in brick)
    subclasses:  # <-- list of subclasses
        CO2 Sensor:     # <--- class name; standalone name
            media: [Air]  # <--- media name. This is a tag that gets placed before the subclass name
            types: [Outside, Return]  # <---  cross product of these names with media types gives additional subclasses
            subclasses:                     # <-- these subclasses are specified explicitly and in addition to those
                CO2 Differential Sensor:    #     created by the cross product of media and types
                CO2 Level Sensor:
```
