import bpy

def assign_weight_to_overlapping_vertices():
    
    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    if bpy.context.selected_objects[0].type == 'ARMATURE':
        obj = bpy.context.selected_objects[1]
        arm = bpy.context.selected_objects[0]
    else:
        obj = bpy.context.selected_objects[0]
        arm = bpy.context.selected_objects[1]
    
    bone_names = obj.vertex_groups.keys()
    
    for vert in obj.data.vertices:
        for bone_name in bone_names:
            tail_co = arm.data.bones[bone_name].tail_local
            length = (vert.co - tail_co).length
            if length < 0.0001:
                vert_group = obj.vertex_groups[bone_name]
                vert_group.add([vert.index], 1.0, 'REPLACE')

assign_weight_to_overlapping_vertices()
