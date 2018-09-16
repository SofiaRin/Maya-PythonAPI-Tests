import maya.cmds as cmds


SUFFIX = {
    "mesh": "geo",
    "joint": "jot",
    "camera": None
}

DEF_SUFFIX = "grp"

def rename(isSelected = False):
    """
    this function will rename dagObject with suffixs, if you selected some object in the sence, those obj'sname will change, if you don't make a selection, all dagObj will
    be renamed
    Args:
        isSelected: wheather the selection is made or not

    Returns:
        selectedList: the selectedList after the renaming
    """

    selectedList = cmds.ls(sl=isSelected, long=True, dag=True)
    if isSelected and not selectedList:
        raise RuntimeError ("No selected object, didn't you forget it ?")

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

        suffix = SUFFIX.get(itsType, DEF_SUFFIX)
        if not suffix:
            print "skip"
            continue

        newName = itsName + "_" + suffix
        print 'currentOBJ  ', obj
        print 'NewName  ' + newName
        cmds.rename(obj, newName)
        currentIndex = selectedList.index(obj)
        selectedList[currentIndex] = obj.replace(itsName,newName)


    return selectedList