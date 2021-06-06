#print("SHIP NAME      CLASS          DEPLOYMENT IN SERVICE\nN2 Bomber      Heavy Fighter  Limited    21        \nJ-Type 327     Light Combat   Unlimited  1         \nNX Cruiser     Medium Fighter Limited    18        \nN1 Starfighter Medium Fighter Unlimited  25        \nRoyal Cruiser  Light Combat   Limited    4          ")

titles = ['ship name', 'class', 'deployment', 'in service']
a = ['N2 Bomber', 'Heavy Fighter', 'Limited', 21]
b = ['J-Type 327', 'Light Combat', 'Unlimited', 1]
c = ['NX Cruiser', 'Medium Fighter', 'Limited', 18]
d = ['N1 Starfighter', 'Medium Fighter', 'Unlimited', 25]
e = ['Royal Cruiser', 'Light Combat', 'Limited', 4]

width = ["%-15s", "%-15s", "%-11s", "%-10s"]
planes = [a,b,c,d,e]

for idx, val in enumerate(titles):
  w = width[idx]
  print(w % val.upper(), end='')

print()
for idx2, val2 in enumerate(planes):
  for idx, val in enumerate(planes[idx2]):
    w = width[idx]
    print(w % val, end='')
  print()
