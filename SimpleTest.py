import LoadLocationData
import RandomizeItems
import Badge
import RandomizerRom
from collections import defaultdict

res = LoadLocationData.LoadDataFromFolder(".")
trashItems = res[1]
LocationList = res[0]
progressItems = ['Cut','Surf','Letter', 'Devon Goods', 'Strength', 'Basement Key','Rock Smash', 'Flash']
print(res)
Stone = Badge.Badge()
Stone.isTrash = False
Stone.Name = 'Stone Badge'
Stone.Flag = 'FLAG_BADGE01_GET';
Dynamo = Badge.Badge()
Dynamo.isTrash = False
Dynamo.Name = 'Dynamo Badge'
Dynamo.Flag = 'FLAG_BADGE03_GET';
Knuckle = Badge.Badge()
Knuckle.isTrash = False
Knuckle.Name = 'Dynamo Badge'
Knuckle.Flag = 'FLAG_BADGE02_GET';
BadgeDict = {'Stone Badge' : Stone, 'Dynamo Badge' : Dynamo, 'Knuckle Badge': Knuckle}

result = RandomizeItems.RandomizeItems('None',LocationList,progressItems,trashItems,BadgeDict,inputFlags = ['Kanto Mode'])

RandomizerRom.ResetRom()
RandomizerRom.WriteItemLocations(result[0].values())

print(result[2])
print(result[1])