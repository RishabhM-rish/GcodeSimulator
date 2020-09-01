# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Gcodes Simulator",
    "author": "Rishabh Mathur",
    "version": (1, 0, 0),
    "blender": (2, 80, 2),
    "location": "File > Import> Gcode (.gcode) ",
    "description": "Simulating Gcodes for 3D concrete printing",
    "wiki_url": "https://github.com/RishabhM-rish/GcodeSimulator/blob/master/README.md",
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
