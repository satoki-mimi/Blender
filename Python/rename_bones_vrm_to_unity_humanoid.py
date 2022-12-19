import bpy

def rename_bones():
    dic = {
        'Root': 'Root', #基本のボーンにはない
        'J_Bip_C_Hips': 'Hips',
        'J_Bip_C_Spine': 'Spine',
        'J_Bip_C_Chest': 'Chest',
        'J_Bip_C_UpperChest': 'Upper_Chest',
        'J_Sec_L_Bust1': 'Bust.L',
        'J_Sec_R_Bust1': 'Bust.R',
        'J_Sec_L_Bust2': 'Bust2.L', #基本のボーンにはない
        'J_Sec_R_Bust2': 'Bust2.R', #基本のボーンにはない
        'J_Bip_C_Neck': 'Neck',
        'J_Bip_C_Head': 'Head',
        'J_Adj_L_FaceEye': 'Eye.L',
        'J_Adj_R_FaceEye': 'Eye.R',
        'J_Bip_L_Shoulder': 'Shoulder.L',
        'J_Bip_L_UpperArm': 'Upper_Arm.L',
        'J_Bip_L_LowerArm': 'Lower_Arm.L',
        'J_Bip_L_Hand': 'Hand.L',
        'J_Bip_L_Thumb1': 'Thumb_Proximal.L',
        'J_Bip_L_Thumb2': 'Thumb_Intermediate.L',
        'J_Bip_L_Thumb3': 'Thumb_Distal.L',
        'J_Bip_L_Index1': 'Index_Proximal.L',
        'J_Bip_L_Index2': 'Index_Intermediate.L',
        'J_Bip_L_Index3': 'Index_Distal.L',
        'J_Bip_L_Middle1': 'Middle_Proximal.L',
        'J_Bip_L_Middle2': 'Middle_Intermediate.L',
        'J_Bip_L_Middle3': 'Middle_Distal.L',
        'J_Bip_L_Ring1': 'Ring_Proximal.L',
        'J_Bip_L_Ring2': 'Ring_Intermediate.L',
        'J_Bip_L_Ring3': 'Ring_Distal.L',
        'J_Bip_L_Little1': 'Little_Proximal.L',
        'J_Bip_L_Little2': 'Little_Intermediate.L',
        'J_Bip_L_Little3': 'Little_Distal.L',
        'J_Bip_R_Shoulder': 'Shoulder.R',
        'J_Bip_R_UpperArm': 'Upper_Arm.R',
        'J_Bip_R_LowerArm': 'Lower_Arm.R',
        'J_Bip_R_Hand': 'Hand.R',
        'J_Bip_R_Thumb1': 'Thumb_Proximal.R',
        'J_Bip_R_Thumb2': 'Thumb_Intermediate.R',
        'J_Bip_R_Thumb3': 'Thumb_Distal.R',
        'J_Bip_R_Index1': 'Index_Proximal.R',
        'J_Bip_R_Index2': 'Index_Intermediate.R',
        'J_Bip_R_Index3': 'Index_Distal.R',
        'J_Bip_R_Middle1': 'Middle_Proximal.R',
        'J_Bip_R_Middle2': 'Middle_Intermediate.R',
        'J_Bip_R_Middle3': 'Middle_Distal.R',
        'J_Bip_R_Ring1': 'Ring_Proximal.R',
        'J_Bip_R_Ring2': 'Ring_Intermediate.R',
        'J_Bip_R_Ring3': 'Ring_Distal.R',
        'J_Bip_R_Little1': 'Little_Proximal.R',
        'J_Bip_R_Little2': 'Little_Intermediate.R',
        'J_Bip_R_Little3': 'Little_Distal.R',
        'J_Bip_L_UpperLeg': 'Upper_Leg.L',
        'J_Bip_L_LowerLeg': 'Lower_Leg.L',
        'J_Bip_L_Foot': 'Foot.L',
        'J_Bip_L_ToeBase': 'Toes.L',
        'J_Bip_R_UpperLeg': 'Upper_Leg.R',
        'J_Bip_R_LowerLeg': 'Lower_Leg.R',
        'J_Bip_R_Foot': 'Foot.R',
        'J_Bip_R_ToeBase': 'Toes.R'
    }
    for bone in bpy.context.active_object.data.bones:
        if bone.name in dic:
            bone.name = dic[bone.name]
rename_bones()
