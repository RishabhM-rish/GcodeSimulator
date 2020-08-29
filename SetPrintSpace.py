import bpy
import os
from bpy_extras.io_utils import ExportHelper, ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator       
 
class PrintSpace(Operator):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "scale.plane"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Set 3D print workspace"

   

    

    def execute(self, context):
        xfac = bpy.context.scene.sample_vars.X_Dim
        yfac = bpy.context.scene.sample_vars.Y_Dim
        zfac = bpy.context.scene.sample_vars.Z_Dim
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects["Plane"].select_set(True)
        bpy.ops.object.scale_clear(clear_delta=False)
        bpy.ops.transform.resize(value =( xfac/100, yfac/100, zfac/100))
        bpy.ops.object.select_all(action='DESELECT')

        
        
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(PrintSpace)

    

def unregister():
    
    bpy.utils.unregister_class(PrintSpace)


if __name__ == "__main__":
    register()



if __name__ == "__main__":
    register()