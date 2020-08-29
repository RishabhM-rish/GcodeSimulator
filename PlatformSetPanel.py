import bpy
import os
from bpy_extras.io_utils import ExportHelper, ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator 
from . import VolumeFind

     
 
class Workspace(bpy.types.Panel):
    """Creates a Panel in the 3D screen"""
    bl_label = "Edit print workspace"
    bl_idname = "OBJECT_PT_WS"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Printing Workspace Setup"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Printing workspace", icon='WORLD_DATA')
        
        self.layout.prop(bpy.context.scene.sample_vars, 'X_Dim')
        self.layout.prop(bpy.context.scene.sample_vars, 'Y_Dim')      
        self.layout.prop(bpy.context.scene.sample_vars, 'Z_Dim')
        
        row = layout.row()
        row.operator("scale.plane")
    
        
        self.layout.label(text="")
        self.layout.prop(bpy.context.scene.sample_vars, 'L_height')
        self.layout.prop(bpy.context.scene.sample_vars, 'Thick')
        row = layout.row()
        row.operator("vol.find")
        self.layout.label(text=" Required Volume in liters:")
        
        row = layout.row()
        row.label(text= VolumeFind.req_vol_str)
        row.label(text= " L")
        

def register():
    bpy.utils.register_class(Workspace)


    

def unregister():
    bpy.utils.unregister_class(Workspace)



if __name__ == "__main__":
    register()