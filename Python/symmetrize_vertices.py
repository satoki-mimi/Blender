import bpy
import bmesh

def symmetrize_vertices(LR, margin):
    
    if LR != "left" and LR != "right":
        print('Type "left" or "right".')
        return
    
    if type(margin) != float and type(margin) != int:
        print('Margin value must be a number.')
        return

    def calc_length(v1, v2):
        lx = (v1.co.x + v2.co.x)**2
        ly = (v1.co.y - v2.co.y)**2
        lz = (v1.co.z - v2.co.z)**2
        return (lx + ly + lz)**0.5

    mesh = bpy.context.selected_objects[0].data
    bm = bmesh.from_edit_mesh(mesh)
    bm.verts.ensure_lookup_table()

    verts_L = []
    verts_R = []

    for v in bm.verts:
        if v.hide == False and v.select == True:
            if abs(v.co.x) < margin:
                v.co.x = 0
            elif v.co.x < 0:
                verts_L.append(v)
            elif v.co.x > 0:
                verts_R.append(v)

    for v_L in verts_L:
        for v_R in verts_R:
            length = calc_length(v_L, v_R)
            if length != 0.0 and length < margin:
                if LR == "left":
                    v_L.co.x = v_R.co.x * (-1)
                    v_L.co.y = v_R.co.y
                    v_L.co.z = v_R.co.z
                else:
                    v_R.co.x = v_L.co.x * (-1)
                    v_R.co.y = v_L.co.y
                    v_R.co.z = v_L.co.z

    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.object.mode_set(mode = 'EDIT')

symmetrize_vertices("left", 0.2)
