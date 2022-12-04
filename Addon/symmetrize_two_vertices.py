import bpy
import bmesh

bl_info = {
    "name": "Symmetrize Two Vertices",
    "author": "Satoki",
    "blender": (3, 0, 0),
    "support": "TESTING",
    "category": "User"
}

class SymmetrizeTwoVertices(bpy.types.Operator):

    bl_idname = "mesh_vertices.symmetrize_two_vertices"
    bl_label = "SymmetrizeTwoVertices"
    bl_description = "Right to Left"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        me = context.active_object.data
        bm = bmesh.from_edit_mesh(me)
        bm.verts.ensure_lookup_table()
        v_L = bm.verts[0]
        v_R = bm.verts[0]
        for v in bm.verts:
            if v.hide == False:
                if v.select == True:
                    if v.co.x < 0:
                        v_L = v
                    else:
                        v_R = v
        v_L.co.x = v_R.co.x * (-1)
        v_L.co.y = v_R.co.y
        v_L.co.z = v_R.co.z
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.mode_set(mode = 'EDIT')
        return {'FINISHED'}
    
def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(SymmetrizeTwoVertices.bl_idname)

def register():
    bpy.utils.register_class(SymmetrizeTwoVertices)
    bpy.types.VIEW3D_MT_edit_mesh_vertices.append(menu_fn)

def unregister():
    bpy.types.VIEW3D_MT_edit_mesh_vertices.remove(menu_fn)
    bpy.utils.unregister_class(SymmetrizeTwoVertices)

if __name__ == "__main__":
    register()
