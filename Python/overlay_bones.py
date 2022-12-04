import bpy

def overlay_bones():

    if bpy.context.mode != 'EDIT':
        bpy.ops.object.mode_set(mode='EDIT')
        
    ref_bones = bpy.context.selected_objects[0].data.edit_bones
    bones = bpy.context.selected_objects[1].data.edit_bones

    for bone in bones:
        try:
            ref_bone = ref_bones[bone.name]
            bone.head = ref_bone.head
            bone.tail = ref_bone.tail
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
            ref_bone = ref_bones['頭']
            bone.head.x = 0
            bone.head.y = ref_bone.tail.y - length
            bone.head.z = ref_bone.tail.z + length * 6
            bone.tail.xz = bone.head.xz
            bone.tail.y = bone.head.y - length
        elif '足ＩＫ.L' == bone.name:
            ref_bone = ref_bones['ひざ.L']
            bone.head = ref_bone.tail
            bone.tail.xz = bone.head.xz
            bone.tail.y = bone.head.y + length
        elif '足ＩＫ.R' == bone.name:
            ref_bone = ref_bones['ひざ.R']
            bone.head = ref_bone.tail
            bone.tail.xz = bone.head.xz
            bone.tail.y = bone.head.y + length
        elif 'つま先ＩＫ.L' == bone.name:
            ref_bone = ref_bones['足首.L']
            bone.head = ref_bone.tail
            bone.tail.xy = bone.head.xy
            bone.tail.z = bone.head.z - length
        elif 'つま先ＩＫ.R' == bone.name:
            ref_bone = ref_bones['足首.R']
            bone.head = ref_bone.tail
            bone.tail.xy = bone.head.xy
            bone.tail.z = bone.head.z - length
        elif '腕捩先.L' == bone.name:
            ref_bone = ref_bones['腕.L']
            bone.head = ref_bone.tail
            bone.tail.xy = ref_bone.tail.xy
            bone.tail.z = ref_bone.head.z + length
        elif '腕捩先.R' == bone.name:
            ref_bone = ref_bones['腕.R']
            bone.head = ref_bone.tail
            bone.tail.xy = ref_bone.tail.xy
            bone.tail.z = ref_bone.tail.z + length
        elif '手捩先.L' == bone.name:
            ref_bone = ref_bones['ひじ.L']
            bone.head = ref_bone.tail
            bone.tail.xy = ref_bone.tail.xy
            bone.tail.z = ref_bone.head.z + length
        elif '手捩先.R' == bone.name:
            ref_bone = ref_bones['ひじ.R']
            bone.head = ref_bone.tail
            bone.tail.xy = ref_bone.tail.xy
            bone.tail.z = ref_bone.tail.z + length
        elif '先' in bone.name:
            bone.tail.xy = bone.head.xy
            bone.tail.z = bone.head.z + length
        elif '腕捩.L' == bone.name:
            ref_bone = ref_bones['腕.L']
            bone.head = ref_bone.head * 2 / 3 + ref_bone.tail / 3
            bone.tail = ref_bone.head / 3 + ref_bone.tail * 2 / 3
        elif '腕捩.R' == bone.name:
            ref_bone = ref_bones['腕.R']
            bone.head = ref_bone.head * 2 / 3 + ref_bone.tail / 3
            bone.tail = ref_bone.head / 3 + ref_bone.tail * 2 / 3
        elif '手捩.L' == bone.name:
            ref_bone = ref_bones['ひじ.L']
            bone.head = ref_bone.head * 2 / 3 + ref_bone.tail / 3
            bone.tail = ref_bone.head / 3 + ref_bone.tail * 2 / 3
        elif '手捩.R' == bone.name:
            ref_bone = ref_bones['ひじ.R']
            bone.head = ref_bone.head * 2 / 3 + ref_bone.tail / 3
            bone.tail = ref_bone.head / 3 + ref_bone.tail * 2 / 3
        elif '腕捩' in bone.name and '.L' in bone.name:
            ref_bone = ref_bones['腕.L']
            bone.head = ref_bone.head * 2 / 3 + ref_bone.tail / 3
            bone.tail.xy = bone.head.xy
            bone.tail.z = bone.head.z + length
        elif '腕捩' in bone.name and '.R' in bone.name:
            ref_bone = ref_bones['腕.R']
            bone.head = ref_bone.head * 2 / 3 + ref_bone.tail / 3
            bone.tail.xy = bone.head.xy
            bone.tail.z = bone.head.z + length
            
    bpy.ops.object.mode_set(mode='OBJECT')

overlay_bones()
