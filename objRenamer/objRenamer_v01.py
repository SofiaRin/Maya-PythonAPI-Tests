import maya.cmds as cmds


selectedList = cmds.ls(sl=True,long=True)


if len(selectedList) == 0:
    print 'nothing Selected'
    selectedList = cmds.ls(dag=True, l=True)
    
selectedList.sort(key=len, reverse=True) 

print 'objList ',selectedList

for obj in selectedList:
    itsName = obj.split("|")[-1]
    childrenList = cmds.listRelatives(obj, children=True, fullPath=True) or []
    if len(childrenList) == 1:
        itsType = cmds.objectType(childrenList[0])
    else:
        itsType = cmds.objectType(obj)
    
    print "obj: " + itsName
    print childrenList
    
    if itsType == 'mesh':
        suffix = 'geo'
    elif itsType == 'joint':
        suffix = 'jot'
    elif itsType == 'camera':
        print 'skiping'
        continue
    else:
        suffix = 'grp'
    if itsName.endswith('_'+suffix):
        continue
    newName = itsName + "_" + suffix
    print 'currentOBJ  ', obj 
    print 'NewName  ' + newName
    cmds.rename(obj, newName)
    
    