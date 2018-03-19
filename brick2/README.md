## Tags

- tag definitions are grouped. These groups have names, and can be thought of as broad classes:
    - currently, these are:
        - equipment: physical equipment in the building
        - location: describing the spatial breakdown of the building
        - point: sensors, statuses, setpoints, commands, alarms
        - substances: anything that is processed, measured or controlled
- Cliff has pointed out several of the benefits of this approach:
    > By using tag groups, there is less need for rules for individual tags and thus much more manageable complexity.
    > By using tag groups, it is easier to extend the tag dictionary by adding tags that fall into existing groups.
    > By using tag groups, it is easier to extend tagged items by having a more generic structure than is provided by rules on individual tags.


## Types

- has `class` tag:
    ```yaml
    id: ahu_class
    type: [equipment, HVAC, AHU]
    ductwork: [dualDuct]
    fans: [dualFan]
    heatsWith: [hot, water]
    coolsWith: [condensed, water]
    heats: [air]
    cools: [air]
    ```
- the value of the `class` tag acts as an alias
- entities inherit the tags from all classes listed in their `type` field (minus the `class` tag):
    ```yaml
    id: AHU1A
    type: ahu_class
    hasPart: [supplyfan1, supplyfan2]
    ```

    becomes

    ```yaml
    id: AHU1A
    type: [equipment, HVAC, AHU]
    ductwork: [dualDuct]
    fans: [dualFan]
    heatsWith: [hot, water]
    coolsWith: [condensed, water]
    heats: [air]
    cools: [air]
    hasPart: [supplyfan1, supplyfan2]
    ```

    alternatively, we could just treet `AHU1A` as if it had the tags.
- for any key in the entity (e.g. `type`) we take the UNION with the inherited tags. No tags are lost under this policy
- this can recurse as many times as you want (e.g. classes can be defined in terms of other classes)
    ```yaml
    id: hot_water_ahu
    type: [class, equipment, HVAC, AHU]
    heatsWith: [hot, water]

    ---

    id: cold_water_ahu
    type: [class, equipment, HVAC, AHU]
    coolsWith: [condensed, water]

    ---

    id: AHU1A
    type: [hot_water_ahu, cold_water_ahu]
    ```
- classes can additionally refer to specific pices of equipment
    ```yaml
    id: AHU1A
    type: [equipment, HVAC, AHU]
    heatsWith: [hot, water]
    coolsWith: [condensed, water]

    ---

    id: supplyfan_class
    type: [class, equipment, HVAC, fan, variable, supply]
    isPartOf: [AHU1A]

    ---

    id: sf1
    type: [supplyfan_class]

    ---

    id: sf2
    type: [supplyfan_class]
    ```

    The resulting document will create 2 supply fans each pointing to `AHU1A`

## Relationships

- for relationships with reverse edges, only one of them needs to be populated
    - query engine or model compiler should populate the reverse edges
- there has been discussion on whether or not relationships should have 'tags'
    - I think it simplifies the design for relationships/scopes to be simple and flat
    - otherwise we hit the issue: "is this tag part of relship or part of entity?"
    
## Querying

- can support multiple models of querying
- tag queries:
    - Haystack-style
- graph queries:
    - tags are scoped by relationships and/or context
        - relationships: listen in relationships file
        - contexts: e.g. type, equipment
    - refer to entities by their tags:
        1. "contains <tag>"
        2. more structured: "type contains <tag>"
    - connect entities using relationships
        ```yaml
        x=(supply fan) isPartOf a=(AHU)
        a=(AHU) site (test site)
        ```
