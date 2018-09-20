import maya.cmds as cmds

##use sys.path.append() to add a path, so that maya could import module
##import sys
##sys.path.append it seems need run everyTime before import your module
def makeGear(teeth = 10, length = 0.5):
    removeGear()
    spin = teeth * 2
    transform, constructor = cmds.polyPipe(subdivisionsAxis=spin, name='Gear')

    ##calcute sideFace number
    faceNum = range(spin * 2, spin * 3, 2)
    #print faceNum

    ##clean everySelection
    cmds.select(clear=True)
    for face in faceNum:
        print face
        ##select target faces
        cmds.select("%s.f[%s]" % (transform, face), add=True) or []

    extrudeAttr = cmds.polyExtrudeFacet(ltz = length)[0]
    print extrudeAttr
    print transform, constructor
    return  transform,constructor,extrudeAttr

def removeGear(name='Gear'):
    exsitGear = cmds.ls(name)
    if (exsitGear):
        cmds.delete(exsitGear)
        print "delete the former one "

def changeGear(transform,constructor,extrudeAttr,teeth = 5, length = 0.2):
    spin = teeth*2
    cmds.polyPipe(constructor, edit = True, subdivisionsAxis=spin)
    faceNum = range(spin * 2, spin * 3, 2)

    cmds.select(clear=True)
    for face in faceNum:
        print face
        ##select target faces
        cmds.select("%s.f[%s]" % (transform, face), add=True) or []
    ##attention this will create another extrude
    ##we just need to edit the current extrude attr
    extrudeAttr = cmds.polyExtrudeFacet(ltz = length)[0]
    return 0
