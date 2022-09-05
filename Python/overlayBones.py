import bpy

def overlay_bones():

    if bpy.context.mode != 'EDIT':
        bpy.ops.object.mode_set(mode='EDIT')
        
    refBones = bpy.context.selected_objects[0].data.edit_bones
    bones = bpy.context.selected_objects[1].data.edit_bones

    for bone in bones:
        try:
            refBone = refBones[bone.name]
            bone.head = refBone.head
            bone.tail = refBone.tail
        except:
            pass

    #腕の長さをボーンの長さの基準とする
    length = bones['腕.R'].length / 3

    for bone in bones:
        if 'センター' == bone.name:
            bone.head = (0,0,0)
            bone.tail = (0,0,0)
            bone.head.z = length * 7
        elif '両目' == bone.name:
            refBone = refBones['頭']
            bone.head.x = 0
            bone.head.y = refBone.tail.y - length
            bone.head.z = refBone.tail.z + length * 6
            bone.tail.xz = bone.head.xz
            bone.tail.y = bone.head.y - length
        elif '足ＩＫ.L' == bone.name:
            refBone = refBones['ひざ.L']
            bone.head = refBone.tail
            bone.tail.xz = bone.head.xz
            bone.tail.y = bone.head.y + length
        elif '足ＩＫ.R' == bone.name:
            refBone = refBones['ひざ.R']
            bone.head = refBone.tail
            bone.tail.xz = bone.head.xz
            bone.tail.y = bone.head.y + length
        elif 'つま先ＩＫ.L' == bone.name:
            refBone = refBones['足首.L']
            bone.head = refBone.tail
            bone.tail.xy = bone.head.xy
            bone.tail.z = bone.head.z - length
        elif 'つま先ＩＫ.R' == bone.name:
            refBone = refBones['足首.R']
            bone.head = refBone.tail
            bone.tail.xy = bone.head.xy
            bone.tail.z = bone.head.z - length
        elif '腕捩先.L' == bone.name:
            refBone = refBones['腕.L']
            bone.head = refBone.tail
            bone.tail.xy = refBone.tail.xy
            bone.tail.z = refBone.head.z + length
        elif '腕捩先.R' == bone.name:
            refBone = refBones['腕.R']
            bone.head = refBone.tail
            bone.tail.xy = refBone.tail.xy
            bone.tail.z = refBone.tail.z + length
        elif '手捩先.L' == bone.name:
            refBone = refBones['ひじ.L']
            bone.head = refBone.tail
            bone.tail.xy = refBone.tail.xy
            bone.tail.z = refBone.head.z + length
        elif '手捩先.R' == bone.name:
            refBone = refBones['ひじ.R']
            bone.head = refBone.tail
            bone.tail.xy = refBone.tail.xy
            bone.tail.z = refBone.tail.z + length
        elif '先' in bone.name:
            bone.tail.xy = bone.head.xy
            bone.tail.z = bone.head.z + length
        elif '腕捩.L' == bone.name:
            refBone = refBones['腕.L']
            bone.head = refBone.head * 2 / 3 + refBone.tail / 3
            bone.tail = refBone.head / 3 + refBone.tail * 2 / 3
        elif '腕捩.R' == bone.name:
            refBone = refBones['腕.R']
            bone.head = refBone.head * 2 / 3 + refBone.tail / 3
            bone.tail = refBone.head / 3 + refBone.tail * 2 / 3
        elif '手捩.L' == bone.name:
            refBone = refBones['ひじ.L']
            bone.head = refBone.head * 2 / 3 + refBone.tail / 3
            bone.tail = refBone.head / 3 + refBone.tail * 2 / 3
        elif '手捩.R' == bone.name:
            refBone = refBones['ひじ.R']
            bone.head = refBone.head * 2 / 3 + refBone.tail / 3
            bone.tail = refBone.head / 3 + refBone.tail * 2 / 3
        elif '腕捩' in bone.name and '.L' in bone.name:
            refBone = refBones['腕.L']
            bone.head = refBone.head * 2 / 3 + refBone.tail / 3
            bone.tail.xy = bone.head.xy
            bone.tail.z = bone.head.z + length
        elif '腕捩' in bone.name and '.R' in bone.name:
            refBone = refBones['腕.R']
            bone.head = refBone.head * 2 / 3 + refBone.tail / 3
            bone.tail.xy = bone.head.xy
            bone.tail.z = bone.head.z + length
            
    bpy.ops.object.mode_set(mode='OBJECT')

overlay_bones()
