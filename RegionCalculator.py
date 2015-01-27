import math
chunkfiles = set()
print("!! IMPORTANT !! Do a backup before removing or replacing ANY files in the region folder! I will not be liable if you mess up your world! Please don't use this tool unless you get what chunks are about.")
x1 = int(input("After you've taken a backup, put in the x coord for your first CHUNK (NOT block!): "))
z1 = int(input("Now the z coord for that same chunk: "))
x2 = int(input("Alright, now the z coord for the second chunk: "))
z2 = int(input("Finally, second chunk coord for the second region: "))

xh = max(x1, x2)
xl = min(x1, x2)
zh = max(z1, z2)
zl = min(z1, z2)

def calcRegions(xh, xl, zh, zl):
    for x in range(xl, xh+1):
        for z in range(zl, zh+1):
            chunkfiles.add("r.%d.%d.mca" % (math.floor(x / 32), math.floor(z / 32)))
             
                
calcRegions(xh, xl, zh, zl)

print("Okay, files to remove/replace:")

for file in chunkfiles:
    print(file)

