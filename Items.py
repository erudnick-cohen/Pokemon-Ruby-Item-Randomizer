import yaml

def makeItemCodeDict():
	#hardcoding key item lookups for now, pass as parameter in future
	keyItemMap = {'Rock Smash': 'ITEM_HM06_ROCK_SMASH','Surf': 'ITEM_HM03_SURF','Cut':'ITEM_HM01_CUT', 'Strength':'ITEM_HM04_STRENGTH', 'Letter':'ITEM_LETTER', 'Devon Goods':'ITEM_DEVON_GOODS', 'Basement Key':'ITEM_BASEMENT_KEY', 'Flash':'ITEM_HM05_FLASH'}
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
			