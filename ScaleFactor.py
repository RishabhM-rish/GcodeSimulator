import bpy
import os
from bpy_extras.io_utils import ExportHelper, ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator       
 
class Variables(bpy.types.PropertyGroup):
    X_Dim = bpy.props.FloatProperty(
        name="X dimension",
        description="scaling factor along x",
        default = 1000,
        min = 100,
        max = 10000
    )
    Y_Dim = bpy.props.FloatProperty(
        name="Y dimension",
        description="scaling factor along y",
        default = 1000,
        min = 100,
        max = 10000
    )
    Z_Dim = bpy.props.IntProperty(
        name="Z dimension",
        description="scaling factor along z",
        default = 1000,
        min = 100,
        max = 5000
    )
    L_height = bpy.props.FloatProperty(
        name="layer height",
        description="height of each layer",
        default = 25
    )
    Thick = bpy.props.FloatProperty(
        name="thickness",
        description="thickness of filament",
        default = 40
    )

def register():
    bpy.utils.register_class(Variables)
    bpy.types.Scene.sample_vars = bpy.props.PointerProperty(type=Variables)


    

def unregister():
    del bpy.types.Scene.sample_vars
    bpy.utils.unregister_class(Variables)



if __name__ == "__main__":
    register()