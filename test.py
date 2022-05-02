import os
datainfo = []
print(datainfo)
for a in os.listdir('data'):
    datainfo.append(a)
    
datainfo.sort()
print(datainfo)