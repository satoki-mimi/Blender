import bpy
import bmesh

def equalize_edges_length():
    
    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)

    edges = []
    edges_length = []

    for edge in bm.edges:
        if edge.select == True:
            edges.append(edge)
            edges_length.append(edge.calc_length())
            
    average_length = sum(edges_length) / len(edges)

    for edge, edge_length in zip(edges, edges_length):
        mag = average_length / edge_length
        vert0 = edge.verts[0].co
        vert1 = edge.verts[1].co
        Lx = vert0.x - vert1.x
        Ly = vert0.y - vert1.y
        Lz = vert0.z - vert1.z
        vert0.x += Lx / 2 * (mag - 1)
        vert1.x -= Lx / 2 * (mag - 1)
        vert0.y += Ly / 2 * (mag - 1)
        vert1.y -= Ly / 2 * (mag - 1)
        vert0.z += Lz / 2 * (mag - 1)
        vert1.z -= Lz / 2 * (mag - 1)
            
    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.object.mode_set(mode = 'EDIT')

equalize_edges_length()
