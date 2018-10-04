import maya.cmds as cmds

class Gear(object):
    def __init__(self):
        self.teeth = 10
        self.length = 0.5
        self.name = None
    def makeGear(self, name='00'):
        self.name = name
        return 0


gearA = Gear()
gearA.makeGear()
print gearA.name
