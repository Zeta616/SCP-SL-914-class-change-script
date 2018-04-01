"""

SCP914_rough_change_class = 1:6,6:9,9: ;
SCP914_very_fine_change_class = 9:1, :5,5:3,3:8,8:12,12:11,11:1 ,1 :1,6:1,1:12;
SCP914_1_to_1_change_class = 8:1,6:4,12:6,11:12,1:8,4:6,1 :5,5:1 ;
SCP914_fine_change_class = 6:2,1:2, :2;

"""

classes = {}
classes[0] = "SCP 173"
classes[1] = "Class D"
classes[2] = "Spectator"
classes[3] = "SCP 106"
classes[4] = "Nine tailed fox scientist"
classes[5] = "SCP 049"
classes[6] = "Scientist"
classes[7] = "SCP 079"
classes[8] = "Chaos Insurgency"
classes[9] = "SCP 096"
classes[10] = "SCP 049-2"
classes[11] = "Nine Tailed Fox lieutenant"
classes[12] = "Nine Tailed Fox Commander"
classes[13] = "Nine Tailed Fox Guard"

entrylist = []
output = []

def listclasses():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("List of classes:")
    print("  0 SCP 173\n  1 Class D\n  2 Spectator\n  3 SCP 106\n  4 Nine tailed fox scientist\n  5 SCP 049\n  6 Scientist\n  7 SCP 079\n  8 Chaos Insurgency\n  9 SCP 096\n 10 SCP 049-2\n 11 Nine Tailed Fox lieutenant\n 12 Nine Tailed Fox Commander\n 13 Nine Tailed Fox Guard")
    print("\n\n\n\n\n\n\n\n")

def firstclass():
    listclasses()
    print("press CTRL C to exit")
    print("enter first class as a number:")
    class1 = int(input())
    return class1

def secondclass():
    listclasses()
    print("press CTRL C to exit")
    print("enter second class as a number:")
    class2 = int(input())
    return class2

def combine():
    class1 = firstclass()
    class2 = secondclass()
    entrylist.append((class1,class2))
    

def createentries():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for i in entrylist:
        print("creating config for %s to %s" % (classes[i[0]], classes[i[1]]))
        output.append("%s:%s" % (i[0], i[1]))
    
def outputprint():
    for i in output:
        print(i, end=",")
    print("2:2;")

print("SMOD 914 class changer config creator")
try:
    while True: 
        combine()
except KeyboardInterrupt:
    createentries()

outputprint()


print("\n\n\n\n\n\n\n\n")
print("usage:")
print("in your config add another entry \n\ne.g.\n SCP914_rough_change_class = \n\nthen paste in your ouput at the end of the equal sign")
print("\ne.g.\n SCP914_rough_change_class = " ,end="")
outputprint()
print("\n\n\n\n")
print("possible config entries:")


print("SCP914_rough_change_class = ", end="")
outputprint()

print("SCP914_coarse_change_class = ", end="")
outputprint()

print("SCP914_1_to_1_change_class = ", end="")
outputprint()

print("SCP914_fine_change_class = ", end="")
outputprint()

print("SCP914_very_fine_change_class = ", end="")
outputprint()

end = input()

