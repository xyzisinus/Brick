var data = [
{
	x:0, y:0,
	table: [
		{Tag: "type", Value: ['location', 'site']},
		{Tag: "id", Value: "ashrae_ahu"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "hasPart", Value: ['supplyfan1', 'supplyfan2']},
		{Tag: "heatsWith", Value: ['hot', 'water']},
		{Tag: "type", Value: ['equipment', 'HVAC', 'AHU', 'dualDuct', 'dualFan']},
		{Tag: "id", Value: "ahu1"},
		{Tag: "site", Value: "ashrae_ahu"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "isPartOf", Value: "ahu1"},
		{Tag: "hasPoint", Value: ['startstop1', 'alarmreset1', 'speedcmd1', 'speedstatus1']},
		{Tag: "type", Value: ['equipment', 'HVAC', 'fan variable supply']},
		{Tag: "id", Value: "supplyfan1"},
		{Tag: "site", Value: "ashrae_ahu"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: ['supply', 'fan']},
		{Tag: "substance", Value: "start/stop"},
		{Tag: "type", Value: ['point', 'command']},
		{Tag: "isPointOf", Value: "supplyfan1"},
		{Tag: "site", Value: "ashrae_ahu"},
		{Tag: "id", Value: "startstop1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: ['supply', 'fan']},
		{Tag: "substance", Value: ['static', 'air', 'pressure', 'alarm', 'reset']},
		{Tag: "type", Value: ['point', 'command']},
		{Tag: "isPointOf", Value: "supplyfan1"},
		{Tag: "site", Value: "ashrae_ahu"},
		{Tag: "id", Value: "alarmreset1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: ['supply', 'fan']},
		{Tag: "substance", Value: "speed"},
		{Tag: "type", Value: ['point', 'command']},
		{Tag: "isPointOf", Value: "supplyfan1"},
		{Tag: "site", Value: "ashrae_ahu"},
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
		{Tag: "site", Value: "ashrae_ahu"},
		{Tag: "id", Value: "speedstatus1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: ['supply', 'fan']},
		{Tag: "substance", Value: ['supply', 'air', 'temperature']},
		{Tag: "type", Value: ['point', 'sensor']},
		{Tag: "isPointOf", Value: "ahu1"},
		{Tag: "site", Value: "ashrae_ahu"},
		{Tag: "id", Value: "sat1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "isPartOf", Value: "ahu1"},
		{Tag: "type", Value: ['equipment', 'HVAC', 'heating', 'valve']},
		{Tag: "id", Value: "hw_vlv1"},
		{Tag: "site", Value: "ashrae_ahu"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: ['hot', 'water', 'valve']},
		{Tag: "substance", Value: ['hot', 'water', 'valve', 'open%']},
		{Tag: "type", Value: ['point', 'sensor']},
		{Tag: "isPointOf", Value: "hw_vlv1"},
		{Tag: "site", Value: "ashrae_ahu"},
		{Tag: "id", Value: "hw_vlv_cmd1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: "AHU"},
		{Tag: "substance", Value: ['static', 'air', 'pressure']},
		{Tag: "type", Value: ['point', 'sensor']},
		{Tag: "isPointOf", Value: "ahu1"},
		{Tag: "site", Value: "ashrae_ahu"},
		{Tag: "id", Value: "ductpressure1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: "AHU"},
		{Tag: "substance", Value: ['differential', 'air', 'pressure']},
		{Tag: "type", Value: ['point', 'sensor']},
		{Tag: "isPointOf", Value: "ahu1"},
		{Tag: "site", Value: "ashrae_ahu"},
		{Tag: "id", Value: "filterpressure1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: "AHU"},
		{Tag: "substance", Value: ['return', 'air', 'temperature']},
		{Tag: "type", Value: ['point', 'sensor']},
		{Tag: "isPointOf", Value: "ahu1"},
		{Tag: "site", Value: "ashrae_ahu"},
		{Tag: "id", Value: "rat1"},
	]
},
{
	x:0, y:0,
	table: [
		{Tag: "equipment", Value: "AHU"},
		{Tag: "hasPoint", Value: ['startstop2', 'alarmreset2', 'speedcmd2', 'speedstatus2']},
		{Tag: "isPartOf", Value: "ahu1"},
		{Tag: "type", Value: ['equipment', 'HVAC', 'variable supply fan']},
		{Tag: "site", Value: "ashrae_ahu"},
		{Tag: "id", Value: "supplyfan2"},
	]
},
];
