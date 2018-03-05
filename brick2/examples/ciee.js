[
{
	x:0, y:0,
	table: [
		{Tag: "location", Value: "True"},
		{Tag: "site", Value: "True"},
		{Tag: "id", Value: "ciee"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "id", Value: "floor1"},
		{Tag: "type", Value: "floor"},
		{Tag: "location", Value: "True"},
		{Tag: "site", Value: "ciee"},
		{Tag: "floor", Value: "True"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "isPartOf", Value: ['floor1', 'zone1']},
		{Tag: "id", Value: "R207"},
		{Tag: "location", Value: "True"},
		{Tag: "site", Value: "ciee"},
		{Tag: "room", Value: "True"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "isPartOf", Value: ['floor1', 'zone1']},
		{Tag: "id", Value: "R209"},
		{Tag: "location", Value: "True"},
		{Tag: "site", Value: "ciee"},
		{Tag: "room", Value: "True"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "hasPart", Value: ['R207', 'R209']},
		{Tag: "type", Value: "HVAC zone"},
		{Tag: "location", Value: "True"},
		{Tag: "site", Value: "ciee"},
		{Tag: "id", Value: "zone1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "site", Value: "ciee"},
		{Tag: "type", Value: "floor"},
		{Tag: "location", Value: "True"},
		{Tag: "id", Value: "Roof"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "heatsWith", Value: "gas"},
		{Tag: "RTU", Value: "True"},
		{Tag: "multiZone", Value: "True"},
		{Tag: "HVAC", Value: "True"},
		{Tag: "equipment", Value: "True"},
		{Tag: "class", Value: "True"},
		{Tag: "id", Value: "CIEE_RTU"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "site", Value: "ciee"},
		{Tag: "feeds", Value: "zone1"},
		{Tag: "type", Value: "CIEE_RTU"},
		{Tag: "location", Value: "Roof"},
		{Tag: "id", Value: "RTU1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: "True"},
		{Tag: "singleStageHeat", Value: "True"},
		{Tag: "thermostat", Value: "True"},
		{Tag: "HVAC", Value: "True"},
		{Tag: "singleStageCool", Value: "True"},
		{Tag: "class", Value: "True"},
		{Tag: "id", Value: "Venstar_thermostat"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "substance", Value: "air temperature"},
		{Tag: "sensor", Value: "True"},
		{Tag: "id", Value: "temperature_sensor"},
		{Tag: "unit", Value: "Celsius"},
		{Tag: "class", Value: "True"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "type", Value: "Venstar_thermostat"},
		{Tag: "id", Value: "tstat_1"},
		{Tag: "controls", Value: "RTU1"},
		{Tag: "location", Value: ['R209', 'zone1']},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "site", Value: "ciee"},
		{Tag: "type", Value: "temperature_sensor"},
		{Tag: "location", Value: "R207"},
		{Tag: "id", Value: "Hamilton002c"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "site", Value: "ciee"},
		{Tag: "type", Value: "temperature_sensor"},
		{Tag: "location", Value: "R209"},
		{Tag: "id", Value: "Hamilton0055"},
	]
},
]
