import bpy
import os
from bpy_extras.io_utils import ExportHelper, ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator       
 
       
class ImportGcode(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "importgtosim.gcode"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Gcode to simulate"

    # ImportHelper mixin class uses this
    filename_ext = ".gcode"

    filter_glob: StringProperty(
        default="*.gcode",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    

    def execute(self, context):
        Impfile = self.filepath
        bpy.ops.mesh.primitive_circle_add()
        bpy.ops.transform.resize(value=(0.163573, 0.163573, 0.163573))
        bpy.ops.object.convert(target='CURVE')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.merge(type='CENTER')
        f = open(Impfile,'r', encoding='utf-8') # opening imported file
        lines = f.readlines()
        X_cord_old = 0.0
        Y_cord_old = 0.0
        Z_cord_old = 0.0
        F_cord_old = 0.0
        
        X_cord_str = "0.0"
        Y_cord_str = "0.0"
        Z_cord_str = "0.0"
        F_cord_str = "0.0"
        
        for line in lines:
            if line[0:3] == "G0 " or line[0:3] == "G1 ":
                indF = line.find('F')
                indX = line.find('X')
                indY = line.find('Y')
                indZ = line.find('Z')
                strlen = len(line)
                
                if indF != -1:
                    F_cord_str = ''
                    for count in range(0, strlen - indF -1):
                        if indF + count + 1 <= strlen - 1 and line[indF + count + 1] != ' ':
                            F_cord_str = F_cord_str + line[indF + count + 1]
                        else:
                            break
                if indX != -1:
                    X_cord_str = ''
                    for count in range(0, strlen - indX -1):
                        if indX + count + 1 <= strlen - 1 and line[indX + count + 1] != ' ':
                            X_cord_str = X_cord_str + line[indX + count + 1]
                        else:
                            break
                if indY != -1:
                    Y_cord_str = ''
                    for count in range(0, strlen - indY -1):
                        if indY + count + 1 <= strlen - 1 and line[indY + count + 1] != ' ':
                            Y_cord_str = Y_cord_str + line[indY + count + 1]
                        else:
                            break
                if indZ != -1:
                    Z_cord_str = ''
                    for count in range(0, strlen - indZ -1):
                        if indZ + count + 1 <= strlen - 1 and line[indZ + count + 1] != ' ':
                            Z_cord_str = Z_cord_str + line[indZ + count + 1]
                        else:
                            break
                
                
                X_cord = 0.01 * float(X_cord_str)
                Y_cord = 0.01 * float(Y_cord_str)
                Z_cord = 0.01 * float(Z_cord_str)
                F_cord = 0.01 * float(F_cord_str)
                
                
                bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region=None, TRANSFORM_OT_translate={"value":(X_cord - X_cord_old, Y_cord - Y_cord_old, Z_cord - Z_cord_old)})
  
                
                X_cord_old = X_cord
                Y_cord_old = Y_cord
                Z_cord_old = Z_cord
                F_cord_old = F_cord
                
        f.close()   
        bpy.ops.object.mode_set(mode='OBJECT') 
        bpy.ops.object.convert(target='CURVE')
        bpy.context.object.data.bevel_object = bpy.data.objects["Circle"]
        bpy.context.scene.frame_set(1)
        bpy.context.object.data.bevel_factor_end = 0
        bpy.context.object.data.keyframe_insert("bevel_factor_end",frame=1)
        bpy.context.object.data.bevel_factor_end = 1
        bpy.context.object.data.keyframe_insert("bevel_factor_end",frame=500)
        

        
        return {'FINISHED'}
    
def menu_func_import(self, context):
    self.layout.operator(ImportGcode.bl_idname, text="Gcode (.gcode) ")

    
    
def register():
    bpy.utils.register_class(ImportGcode)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

    

def unregister():
    bpy.utils.unregister_class(ImportGcode)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)



if __name__ == "__main__":
    register()