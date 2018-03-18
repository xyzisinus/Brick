Notes:
- "subtance" really only makes sense for sensors/setpoints
- what about mechanical properties?
    - power
    - speed
    - on/off
- for mechanical properties, how much of the equipment type do we want to include?
    - supply fan speed command
    - fan speed command
    - speed command
    - probably keep it fully qualified:
        - if we have the equipment as a node, it is redundant
        - if we do *not* have equipment as node (e.g. heating valve),
          then we need the info to know
- linking equipment together
    - do we know what the link is?
    - infer that from the relationship?
