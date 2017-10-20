# Declarative Specification of Brick Hierarchy

## Dimensions

When we have a tag or a class in the specification, we can "subclass" it along several dimensions.


#### Media

The physical medium a point or piece of equipment operates over.

Common values are `Water`,`Air`,`Electricity`,`CO2`.

---

Quick Discussion:  what's the difference between types and modifiers?

As Keith proposed:
modifiers: [Hot, Chilled, Condenser]
types: [Discharge, Return]

but what's the distinction here?

Gabe proposal:

How do we qualify a sensor or a piece of equipment?

- along which media it is concerned with:
    - water, air, electricity, co2, etc
- what 'flavor' of media it is concerned with: (keith calls this modifier)
    - condensed, chilled, hot (water)
    - outside, high, low (air)
- something about how that point/equipment is positioned in the operational flow:
    - discharge, zone, supply, return
    - can we call this the "function"? the "type"?

Questions:
- Is it worth making a distinction betwen 'modifier' and 'type'?
    - could it be more generic? 'dimension1, dimension2, etc'
    - What if we had 'TagDimension'? Capture it generically
- Do these tag modifiers need to be more than 1 level deep?
    - empirical study of the brick tags
    - potential tags causing issues are stuff like:
        - `Zone_Heating_Temperature_Dead_Band_Setpoint`
        - `Zone_Cooling_Temperature_Dead_Band_Setpoint`
        - `Water_System_Discharge_Water_Temperature_Setpoint`
        - `Water_System_Deionised_Water_Conductivity_Sensor`
        - `Water_System_Cooling_Tower_Fan_Speed_Setpoint`
        - `VAV_Occupied_Heating_Min_Supply_Air_Flow_Setpoint`
        - `Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint`
        - `Thumbwheel_Temperature_High_Limit_Setpoint`
        - `Supply_Water_Differential_Pressure_Proportional_Band_Setpoint`
        - `Return_Discharge_Fan_Differential_Speed_Setpoint`
        - `Occupied_Heating_Min_Supply_Air_Flow_Setpoint`
        - `Medium_Temperature_Hot_Water_Supply_Temperature_Low_Reset_Setpoint`
        - `Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint`
        - `HWS_Medium_Temperature_Hot_Water_Supply_Temperature_Low_Reset_Setpoint`
        - `HWS_Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint`
        - `AHU_Discharge_Air_Static_Pressure_Increase_Decrease_Step_Setpoint`
        - `AHU_Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint`

What is the hierarchy of specificity?
1. equipment type
2. media
3. equipment media (hot chilled condenser etc)
4. operational types (discharge return outside zone)

Maybe we don't need to make a decision about this now; instead, just carry it through

---

#### Types



#### Modifiers

#### Subclasses

These are explicit names of subclasses; useful for special cases and rare points for which
its not necessary or possible to fully describe the class using the other dimensions.

Likely this is the most useful for equipment names e.g. `Variable Air Volume Box With Reheat`.

#### Synonyms

## Class-based view

```yaml
Equipment:
    subclasses:
        HVAC:
            subclasses:
                Pump:
                    - media: Water
                      modifiers: [Chilled, Condenser, Hot]
                Terminal Unit:
                    subclasses:
                        Fan Coil Unit:
                            synonyms: [FCU]
                        Variable Air Volume Box:
                            synonyms: [VAV]
                            usesEquipment: [Damper]
                            subclasses:
                                Variable Air Volume Box With Reheat:
                                    synonyms: [RVAV]
                                    usesEquipment: [Heating Coil]
```
