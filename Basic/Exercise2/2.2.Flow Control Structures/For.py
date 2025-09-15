for x in [1, 2, 3, 4]:
    msg = "Hello World"
    print(str(x) + " " + msg)

print("range(4) produces:")
for x in range(4):
    msg = "Hello World"
    print(str(x) + " " + msg)
    
featclasses = ["geology", "landuse", "publands"]
flds = ["TYPE-ID", "LU-CODE", "PUBCODE"]
for f in featclasses: print(f)
for j in range(len(featclasses)):
    print(j, featclasses[j], flds[j])
    

import os
print(os.getcwd())
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
ws = "data"
ilist=os.listdir(ws)
txtfiles = [] # Start with an empty list
for i in ilist:
    if i.endswith(".txt"):
        txtfiles.append(i)
print(txtfiles)
for f in txtfiles:
    print(f)