import bpy

""" メモ
1. 「全ての親」「センター」「腰」を手作業で追加する必要がある
    ⇒ 階層も変える必要がある
2. 「腰」にウェイトはない。「J_Bip_C_Hips」は「下半身」に割り当てる
    ⇒ 階層も変える必要がある
3. 「上半身2」は「J_Bip_C_Chest」と「J_Bip_C_UpperChest」の2つに相当する
    ⇒ 2つを Dissolve（ Ctrl + X ）する必要がある
"""

def rename_bones():
    dic = {
        'Root': 'グルーブ',
        'J_Bip_C_Hips': '下半身',
        'J_Bip_C_Spine': '上半身',
        'J_Bip_C_Chest': '上半身1', #MMDの標準ボーンにはない
        'J_Bip_C_UpperChest': '上半身2',
        'J_Sec_L_Bust1': 'おっぱい.L',
        'J_Sec_R_Bust1': 'おっぱい.R',
        'J_Sec_L_Bust2': 'おっぱい2.L', #MMDの標準ボーンにはない
        'J_Sec_R_Bust2': 'おっぱい2.R', #MMDの標準ボーンにはない
        'J_Bip_C_Neck': '首',
        'J_Bip_C_Head': '頭',
        'J_Adj_L_FaceEye': '目.L',
        'J_Adj_R_FaceEye': '目.R',
        'J_Bip_L_Shoulder': '肩.L',
        'J_Bip_L_UpperArm': '腕.L',
        'J_Bip_L_LowerArm': 'ひじ.L',
        'J_Bip_L_Hand': '手首.L',
        'J_Bip_L_Thumb1': '親指０.L',
        'J_Bip_L_Thumb2': '親指１.L',
        'J_Bip_L_Thumb3': '親指２.L',
        'J_Bip_L_Index1': '人指１.L',
        'J_Bip_L_Index2': '人指２.L',
        'J_Bip_L_Index3': '人指３.L',
        'J_Bip_L_Middle1': '中指１.L',
        'J_Bip_L_Middle2': '中指２.L',
        'J_Bip_L_Middle3': '中指３.L',
        'J_Bip_L_Ring1': '薬指１.L',
        'J_Bip_L_Ring2': '薬指２.L',
        'J_Bip_L_Ring3': '薬指３.L',
        'J_Bip_L_Little1': '小指１.L',
        'J_Bip_L_Little2': '小指２.L',
        'J_Bip_L_Little3': '小指３.L',
        'J_Bip_R_Shoulder': '肩.R',
        'J_Bip_R_UpperArm': '腕.R',
        'J_Bip_R_LowerArm': 'ひじ.R',
        'J_Bip_R_Hand': '手首.R',
        'J_Bip_R_Thumb1': '親指０.R',
        'J_Bip_R_Thumb2': '親指１.R',
        'J_Bip_R_Thumb3': '親指２.R',
        'J_Bip_R_Index1': '人指１.R',
        'J_Bip_R_Index2': '人指２.R',
        'J_Bip_R_Index3': '人指３.R',
        'J_Bip_R_Middle1': '中指１.R',
        'J_Bip_R_Middle2': '中指２.R',
        'J_Bip_R_Middle3': '中指３.R',
        'J_Bip_R_Ring1': '薬指１.R',
        'J_Bip_R_Ring2': '薬指２.R',
        'J_Bip_R_Ring3': '薬指３.R',
        'J_Bip_R_Little1': '小指１.R',
        'J_Bip_R_Little2': '小指２.R',
        'J_Bip_R_Little3': '小指３.R',
        'J_Bip_L_UpperLeg': '足.L',
        'J_Bip_L_LowerLeg': 'ひざ.L',
        'J_Bip_L_Foot': '足首.L',
        'J_Bip_L_ToeBase': 'つま先.L',
        'J_Bip_R_UpperLeg': '足.R',
        'J_Bip_R_LowerLeg': 'ひざ.R',
        'J_Bip_R_Foot': '足首.R',
        'J_Bip_R_ToeBase': 'つま先.R'
    }
    for bone in bpy.context.active_object.data.bones:
        if bone.name in dic:
            bone.name = dic[bone.name]
rename_bones()
