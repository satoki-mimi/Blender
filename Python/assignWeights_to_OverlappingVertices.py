import bpy

def assignWeights_to_OverlappingVertices():
    
    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    if bpy.context.selected_objects[0].type == 'ARMATURE':
        obj = bpy.context.selected_objects[1]
        arm = bpy.context.selected_objects[0]
    else:
        obj = bpy.context.selected_objects[0]
        arm = bpy.context.selected_objects[1]
    
    boneNames = obj.vertex_groups.keys()
    
    for vert in obj.data.vertices:
        for boneName in boneNames:
            tail_co = arm.data.bones[boneName].tail_local
            length = (vert.co - tail_co).length
            if length < 0.00001:
                vertGroup = obj.vertex_groups[boneName]
                vertGroup.add([vert.index], 1.0, 'REPLACE')

assignWeights_to_OverlappingVertices()
