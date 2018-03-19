var data = [
{
	x:0, y:0,
	table: [
		{Tag: "type", Value: ['location', 'site']},
		{Tag: "id", Value: "small"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "heatsWith", Value: ['hot', 'water']},
		{Tag: "fans", Value: ['dualFan']},
		{Tag: "ductwork", Value: ['dualDuct']},
		{Tag: "type", Value: ['class', 'equipment', 'HVAC', 'AHU']},
		{Tag: "id", Value: "ahu_class"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "hasPart", Value: ['supplyfan1']},
		{Tag: "type", Value: ['ahu_class']},
		{Tag: "id", Value: "ahu1"},
		{Tag: "site", Value: "small"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "function", Value: ['supply']},
		{Tag: "hasPoint", Value: ['speedcmd1', 'speedstatus1']},
		{Tag: "frequency", Value: ['variable']},
		{Tag: "isPartOf", Value: "ahu1"},
		{Tag: "type", Value: ['equipment', 'HVAC', 'fan']},
		{Tag: "site", Value: "small"},
		{Tag: "id", Value: "supplyfan1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: ['supply', 'fan']},
		{Tag: "substance", Value: "speed"},
		{Tag: "type", Value: ['point', 'command']},
		{Tag: "isPointOf", Value: "supplyfan1"},
		{Tag: "site", Value: "small"},
		{Tag: "id", Value: "speedcmd1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: ['supply', 'fan']},
		{Tag: "substance", Value: "speed"},
		{Tag: "type", Value: ['point', 'status']},
		{Tag: "isPointOf", Value: "supplyfan1"},
		{Tag: "site", Value: "small"},
		{Tag: "id", Value: "speedstatus1"},
	]
},
];
