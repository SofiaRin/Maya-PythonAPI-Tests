import maya.cmds as cmds

class Gear(object):
    def __init__(self):
        self.teeth = 10
        self.length = 0.5
        self.name = 'Gear'
        self.transform = None
        self.constructor = None
        self.extrudeNode = None
        print 'gear object is created'
    def makeGear(self, teeth=10,length=0.5):
        self.removeGear(self.name)
        spin = teeth * 2
        # total side face number = teeth number * 2
        transform, constructor = cmds.polyPipe(subdivisionsAxis=spin, name=self.name)

        ##calculate sideFaceID from spin*2 to spin*3 at intervals of one
        faceNum = range(spin * 2, spin * 3, 2)

        ##clean everySelection
        cmds.select(clear=True)
        for face in faceNum:
            print face
            ##select target faces based of sideFaceID
            cmds.select("%s.f[%s]" % (transform, face), add=True) or []
        ##set  localTranslateZ flag to make the length of gear
        extrudeAttr = cmds.polyExtrudeFacet(ltz=length)[0]

        print transform, constructor, extrudeAttr
        self.transform = transform
        self.constructor = constructor
        self.extrudeNode = extrudeAttr
        return  0
        #return transform, constructor, extrudeAttr

    def removeGear(self,name='Gear'):
        exsitGear = cmds.ls(name)
        if (exsitGear):
            cmds.delete(exsitGear)
            print "delete the former one "

    def changeGear(self, teeth = 5, length = 0.2):
        spin = teeth * 2
        ##use edit flag to change target meshNode(constructor)
        cmds.polyPipe(self.constructor, edit=True, subdivisionsAxis=spin)
        faceNum = range(spin * 2, spin * 3, 2)

        cmds.select(clear=True)

        newFaceList = []
        for face in faceNum:
            # build a new extrudeFaceList to upgrade the Node
            newFaceList.append("f[%s]" % (face))
        ##ust need to edit the current extrude attr
        print newFaceList;
        ##use setAttr to specify the new list of extrude faces
        cmds.setAttr("%s.inputComponents" % (self.extrudeNode), len(newFaceList), *newFaceList, type='componentList')
        ##it seems can use cmds.xxxnode(edit = True) to change it's flag value
        cmds.polyExtrudeFacet(self.extrudeNode, edit=True, ltz=length)
        return 0


