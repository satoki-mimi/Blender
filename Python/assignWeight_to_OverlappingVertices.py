import bpy

def assignWeight_to_OverlappingVertices():
        
    obj = bpy.context.selected_objects[0]
    arm = bpy.context.selected_objects[1]
    boneNames = obj.vertex_groups.keys()
    
    for vert in obj.data.vertices:       
        for boneName in boneNames:
            tail_co = arm.data.bones[boneName].tail
            length = (vert.co - tail_co).length
            print(length)
            if length < 0.001:
                vertGroup = obj.vertex_groups[boneName]
                vertGroup.add([vert.index], 1.0, 'REPLACE')

assignWeight_to_OverlappingVertices()