# ##### BEGIN GPL LICENSE BLOCK #####
#
#  
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Gcodes Simulator",
    "author": "Rishabh Mathur",
    "version": (1, 0, 0),
    "blender": (2, 80, 2),
    "location": "File > Import> Gcode (.gcode) ",
    "description": "Simulating Gcodes for 3D concrete printing",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View",
}

import bpy
import os

from . import Import_GcodeToSim
from . import PlatformSetPanel
from . import ScaleFactor
from . import SetPrintSpace
from . import VolumeFind

# =========================================================================
# Registration:
# =========================================================================

def register():

    Import_GcodeToSim.register()
    PlatformSetPanel.register()
    ScaleFactor.register()
    SetPrintSpace.register()   
    VolumeFind.register()


def unregister():
    Import_GcodeToSim.unregister()
    PlatformSetPanel.unregister()
    ScaleFactor.unregister()
    SetPrintSpace.unregister() 
    VolumeFind.unregister()

    


if __name__ == "__main__":
    register()
