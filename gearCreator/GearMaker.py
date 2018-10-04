import maya.cmds as cmds

##use sys.path.append() to add a path, so that maya could import module
##import sys
##sys.path.append it seems need run everyTime before import your module
def makeGear(teeth = 10, length = 0.5):
    '''
    this function will create a gear according to specified number of teeth and length
    :param teeth: number of teeth that gear has
    :param length: number of teeth length
    :return: 1.transform node 2. meshconstructor 3. extrudeNode
    '''
    removeGear()
    spin = teeth * 2
    #total side face number = teeth number * 2
    transform, constructor = cmds.polyPipe(subdivisionsAxis=spin, name='Gear')

    ##calculate sideFaceID from spin*2 to spin*3 at intervals of one
    faceNum = range(spin * 2, spin * 3, 2)


    ##clean everySelection
    cmds.select(clear=True)
    for face in faceNum:
        print face
        ##select target faces based of sideFaceID
        cmds.select("%s.f[%s]" % (transform, face), add=True) or []
    ##set  localTranslateZ flag to make the length of gear
    extrudeAttr = cmds.polyExtrudeFacet(ltz = length)[0]

    print extrudeAttr
    print transform, constructor
    return  transform,constructor,extrudeAttr

def removeGear(name='Gear'):
    exsitGear = cmds.ls(name)
    if (exsitGear):
        cmds.delete(exsitGear)
        print "delete the former one "

def changeGear(transform, constructor, extrudeNode, teeth = 5, length = 0.2):
    '''
    this function will change target gearlike geo's teeth number and teeth length
    :param transform: transform node
    :param constructor: mesh constructor
    :param extrudeNode: extrudenode
    :param teeth: new number of teeth
    :param length: new number of teeth length
    :return: 0
    '''
    spin = teeth*2
    ##use edit flag to change target meshNode(constructor)
    cmds.polyPipe(constructor, edit = True, subdivisionsAxis=spin)
    faceNum = range(spin * 2, spin * 3, 2)

    cmds.select(clear=True)

    newFaceList = []
    for face in faceNum:
        #build a new extrudeFaceList to upgrade the Node
        newFaceList.append("f[%s]" % (face))
    ##ust need to edit the current extrude attr
    print newFaceList;
    ##use setAttr to specify the new list of extrude faces
    cmds.setAttr("%s.inputComponents" % (extrudeNode), len(newFaceList), *newFaceList, type ='componentList')
    ##it seems can use cmds.xxxnode(edit = True) to change it's flag value
    cmds.polyExtrudeFacet(extrudeNode, edit=True, ltz=length)
    return 0
