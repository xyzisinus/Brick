[
{
	x:0, y:0,
	table: [
		{Tag: "location", Value: "True"},
		{Tag: "site", Value: "True"},
		{Tag: "id", Value: "hvacloop"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "vavZone", Value: "True"},
		{Tag: "HVAC", Value: "True"},
		{Tag: "variableVolume", Value: "True"},
		{Tag: "singleDuct", Value: "True"},
		{Tag: "coolsWith", Value: "chilled water"},
		{Tag: "heatsWith", Value: "hot water"},
		{Tag: "equipment", Value: "True"},
		{Tag: "AHU", Value: "True"},
		{Tag: "id", Value: "siteAHU"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "singleDuct", Value: "True"},
		{Tag: "HVAC", Value: "True"},
		{Tag: "equipment", Value: "True"},
		{Tag: "variableVolume", Value: "True"},
		{Tag: "coolsWith", Value: "chilled water"},
		{Tag: "heatsWith", Value: "hot water"},
		{Tag: "fan_powered", Value: "True"},
		{Tag: "cooling", Value: "True"},
		{Tag: "reheat", Value: "True"},
		{Tag: "VAV", Value: "True"},
		{Tag: "id", Value: "siteVAV"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "feeds", Value: ['VAV410']},
		{Tag: "type", Value: "siteAHU"},
		{Tag: "id", Value: "AHU1A"},
		{Tag: "site", Value: "hvacloop"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "site", Value: "hvacloop"},
		{Tag: "feeds", Value: "zone410"},
		{Tag: "type", Value: "siteVAV"},
		{Tag: "isFedBy", Value: "AHU1A"},
		{Tag: "id", Value: "VAV410"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "hasPart", Value: ['R410']},
		{Tag: "type", Value: "HVAC zone"},
		{Tag: "location", Value: "True"},
		{Tag: "site", Value: "hvacloop"},
		{Tag: "id", Value: "zone410"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "isPartOf", Value: "zone410"},
		{Tag: "id", Value: "R410"},
		{Tag: "location", Value: "True"},
		{Tag: "site", Value: "hvacloop"},
		{Tag: "room", Value: "True"},
	]
},
]
