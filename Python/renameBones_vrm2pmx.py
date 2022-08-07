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
  for bone in bpy.context.active_object.data.bones:
    if bone.name == 'Root': bone.name = 'グルーブ'
    elif bone.name == 'J_Bip_C_Hips': bone.name = '下半身'
    elif bone.name == 'J_Bip_C_Spine': bone.name = '上半身'
    elif bone.name == 'J_Bip_C_Chest': bone.name = '上半身1' #後ほどDissolve
    elif bone.name == 'J_Bip_C_UpperChest': bone.name = '上半身2'
    elif bone.name == 'J_Sec_L_Bust1': bone.name = 'おっぱい.L'
    elif bone.name == 'J_Sec_R_Bust1': bone.name = 'おっぱい.R'
    elif bone.name == 'J_Sec_L_Bust2': bone.name = 'おっぱい2.L' #基本のボーンにはない
    elif bone.name == 'J_Sec_R_Bust2': bone.name = 'おっぱい2.R' #基本のボーンにはない
    elif bone.name == 'J_Bip_C_Neck': bone.name = '首'
    elif bone.name == 'J_Bip_C_Head': bone.name = '頭'
    elif bone.name == 'J_Adj_L_FaceEye': bone.name = '目.L'
    elif bone.name == 'J_Adj_R_FaceEye': bone.name = '目.R'
    elif bone.name == 'J_Bip_L_Shoulder': bone.name = '肩.L'
    elif bone.name == 'J_Bip_L_UpperArm': bone.name = '腕.L'
    elif bone.name == 'J_Bip_L_LowerArm': bone.name = 'ひじ.L'
    elif bone.name == 'J_Bip_L_Hand': bone.name = '手首.L'
    elif bone.name == 'J_Bip_L_Thumb1': bone.name = '親指０.L'
    elif bone.name == 'J_Bip_L_Thumb2': bone.name = '親指１.L'
    elif bone.name == 'J_Bip_L_Thumb3': bone.name = '親指２.L'
    elif bone.name == 'J_Bip_L_Index1': bone.name = '人指１.L'
    elif bone.name == 'J_Bip_L_Index2': bone.name = '人指２.L'
    elif bone.name == 'J_Bip_L_Index3': bone.name = '人指３.L'
    elif bone.name == 'J_Bip_L_Middle1': bone.name = '中指１.L'
    elif bone.name == 'J_Bip_L_Middle2': bone.name = '中指２.L'
    elif bone.name == 'J_Bip_L_Middle3': bone.name = '中指３.L'
    elif bone.name == 'J_Bip_L_Ring1': bone.name = '薬指１.L'
    elif bone.name == 'J_Bip_L_Ring2': bone.name = '薬指２.L'
    elif bone.name == 'J_Bip_L_Ring3': bone.name = '薬指３.L'
    elif bone.name == 'J_Bip_L_Little1': bone.name = '小指１.L'
    elif bone.name == 'J_Bip_L_Little2': bone.name = '小指２.L'
    elif bone.name == 'J_Bip_L_Little3': bone.name = '小指３.L'
    elif bone.name == 'J_Bip_R_Shoulder': bone.name = '肩.R'
    elif bone.name == 'J_Bip_R_UpperArm': bone.name = '腕.R'
    elif bone.name == 'J_Bip_R_LowerArm': bone.name = 'ひじ.R'
    elif bone.name == 'J_Bip_R_Hand': bone.name = '手首.R'
    elif bone.name == 'J_Bip_R_Thumb1': bone.name = '親指０.R'
    elif bone.name == 'J_Bip_R_Thumb2': bone.name = '親指１.R'
    elif bone.name == 'J_Bip_R_Thumb3': bone.name = '親指２.R'
    elif bone.name == 'J_Bip_R_Index1': bone.name = '人指１.R'
    elif bone.name == 'J_Bip_R_Index2': bone.name = '人指２.R'
    elif bone.name == 'J_Bip_R_Index3': bone.name = '人指３.R'
    elif bone.name == 'J_Bip_R_Middle1': bone.name = '中指１.R'
    elif bone.name == 'J_Bip_R_Middle2': bone.name = '中指２.R'
    elif bone.name == 'J_Bip_R_Middle3': bone.name = '中指３.R'
    elif bone.name == 'J_Bip_R_Ring1': bone.name = '薬指１.R'
    elif bone.name == 'J_Bip_R_Ring2': bone.name = '薬指２.R'
    elif bone.name == 'J_Bip_R_Ring3': bone.name = '薬指３.R'
    elif bone.name == 'J_Bip_R_Little1': bone.name = '小指１.R'
    elif bone.name == 'J_Bip_R_Little2': bone.name = '小指２.R'
    elif bone.name == 'J_Bip_R_Little3': bone.name = '小指３.R'
    elif bone.name == 'J_Bip_L_UpperLeg': bone.name = '足.L'
    elif bone.name == 'J_Bip_L_LowerLeg': bone.name = 'ひざ.L'
    elif bone.name == 'J_Bip_L_Foot': bone.name = '足首.L'
    elif bone.name == 'J_Bip_L_ToeBase': bone.name = 'つま先.L'
    elif bone.name == 'J_Bip_R_UpperLeg': bone.name = '足.R'
    elif bone.name == 'J_Bip_R_LowerLeg': bone.name = 'ひざ.R'
    elif bone.name == 'J_Bip_R_Foot': bone.name = '足首.R'
    elif bone.name == 'J_Bip_R_ToeBase': bone.name = 'つま先.R'
  return

rename_bones()