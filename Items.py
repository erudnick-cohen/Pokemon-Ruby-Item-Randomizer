import yaml

def makeItemCodeDict():
	#hardcoding key item lookups for now, pass as parameter in future
	keyItemMap = {'Rock Smash': 'ITEM_HM06_ROCK_SMASH','Surf': 'ITEM_HM03_SURF','Dive': 'ITEM_HM08_DIVE','Cut':'ITEM_HM01_CUT', 'Strength':'ITEM_HM04_STRENGTH', 'Letter':'ITEM_LETTER','Pokeblock Case' : 'ITEM_POKEBLOCK_CASE','S.S. Ticket':'ITEM_SS_TICKET',  'Orb' :'ITEM_RED_OR_BLUE_ORB', 'Devon Goods':'ITEM_DEVON_GOODS', 'Devon Scope':'ITEM_DEVON_SCOPE', 'Basement Key':'ITEM_BASEMENT_KEY', 'Flash':'ITEM_HM05_FLASH','Acro Bike':'ITEM_ACRO_BIKE', 'Mach Bike' : 'ITEM_MACH_BIKE','Meteorite':'ITEM_METEORITE','Go-Goggles':'ITEM_GO_GOGGLES', 'Storage Key':'ITEM_STORAGE_KEY','Scanner':'ITEM_SCANNER', 'Room 1 Key' : 'ITEM_ROOM_1_KEY', 'Room 2 Key' : 'ITEM_ROOM_2_KEY', 'Room 4 Key' : 'ITEM_ROOM_4_KEY', 'Room 6 Key' : 'ITEM_ROOM_6_KEY'}
	itemCodeDict = {}
	
	#progress items
	filestream = open('ItemData/ProgressItems.yml')
	data = filestream.read()
	yamlTree = yaml.load(data)
	if not yamlTree["Items"] is None:
		for i in yamlTree["Items"]:
			itemCodeDict[i["Name"]] = i["Output"]
	
	#trash items
	filestream = open('ItemData/trashItems.yml')
	data = filestream.read()
	yamlTree = yaml.load(data)
	if not yamlTree["Items"] is None:
		for i in yamlTree["Items"]:
			itemCodeDict[i["Name"]] = i["Output"]
		
	#define lookup function
	def lookupItem(item,isBall,isSpecial):
		if item not in itemCodeDict:
			if item in keyItemMap:
				item = keyItemMap[item]
			return item
		else:
			return itemCodeDict[item]
	return lookupItem

def makeItemTextDict():
	itemCodeDict = {}
	
	#progress items
	filestream = open('ItemData/ProgressItems.yml')
	data = filestream.read()
	yamlTree = yaml.load(data)
	if not yamlTree["Items"] is None:
		for i in yamlTree["Items"]:
			itemCodeDict[i["Name"]] = i["Name"]
			
	#trash items
	filestream = open('ItemData/trashItems.yml')
	data = filestream.read()
	yamlTree = yaml.load(data)
	if not yamlTree["Items"] is None:
		for i in yamlTree["Items"]:
			itemCodeDict[i["Name"]] = i["Name"].upper()
		
	#define lookup function
	def lookupItem(item):
		if item not in itemCodeDict:
			return item.replace("TM_","").replace("_", " ")
		else:
			return itemCodeDict[item]
	return lookupItem
			