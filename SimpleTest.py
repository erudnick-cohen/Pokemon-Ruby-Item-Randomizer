import LoadLocationData
import RandomizeItems
import Badge
import RandomizerRom
from collections import defaultdict

res = LoadLocationData.LoadDataFromFolder(".")
trashItems = res[1]
LocationList = res[0]
progressItems = ['Cut','Surf','Dive','Waterfall','Letter','S.S. Ticket','Pokeblock Case', 'Orb','Devon Goods', 'Strength', 'Basement Key','Rock Smash', 'Flash','Devon Scope','Acro Bike','Mach Bike', 'Meteorite', 'Go-Goggles', 'Storage Key', 'Scanner','Room 1 Key','Room 2 Key','Room 4 Key','Room 6 Key']
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
Balance = Badge.Badge()
Balance.isTrash = False
Balance.Name = 'Balance Badge'
Balance.Flag = 'FLAG_BADGE05_GET';
Heat = Badge.Badge()
Heat.isTrash = False
Heat.Name = 'Heat Badge'
Heat.Flag = 'FLAG_BADGE04_GET';
Mind = Badge.Badge()
Mind.isTrash = False
Mind.Name = 'Mind Badge'
Mind.Flag = 'FLAG_BADGE07_GET';
Rain = Badge.Badge()
Rain.isTrash = False
Rain.Name = 'Rain Badge'
Rain.Flag = 'FLAG_BADGE08_GET';
Wing = Badge.Badge()
Wing.isTrash = True
Wing.Name = 'Wing Badge'
Wing.Flag = 'FLAG_BADGE06_GET';
BadgeDict = {'Stone Badge' : Stone, 'Dynamo Badge' : Dynamo, 'Knuckle Badge': Knuckle, 'Balance Badge': Balance, 'Heat Badge':Heat,'Mind Badge':Mind,'Rain Badge':Rain, 'Wing Badge':Wing}
result = RandomizeItems.RandomizeItems('None',LocationList,progressItems,trashItems,BadgeDict,inputFlags = ['Kanto Mode'])

RandomizerRom.ResetRom()
RandomizerRom.WriteItemLocations(result[0].values())

print(result[2])
print(result[1])