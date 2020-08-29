import bpy
import os
from bpy_extras.io_utils import ExportHelper, ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator 
     
 
class VolReq(Operator):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "vol.find"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Find approx volume of material required"
    
    def execute(self, context):
        curve = bpy.context.object
        curveLength = sum(s.calc_length() for s in curve.data.splines)
        req_vol = curveLength * 100 * 40 * 25 / 1000000
        global req_vol_str
        req_vol_str = str(req_vol)
        return {'FINISHED'}
	
def register():
    bpy.utils.register_class(VolReq)


    

def unregister():
    bpy.utils.unregister_class(VolReq)



if __name__ == "__main__":
    register()