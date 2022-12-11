import bpy

def rename_bones():
    dic = {
        'Root': 'グルーブ',
        'Hips': '下半身',
        'Spine': '上半身',
        'Chest': '上半身1', #MMDの標準ボーンにはない
        'UpperChest': '上半身2',
        'Bust.L': 'おっぱい.L',
        'Bust.R': 'おっぱい.R',
        'Bust2.L': 'おっぱい2.L', #MMDの標準ボーンにはない
        'Bust2.R': 'おっぱい2.R', #MMDの標準ボーンにはない
        'Neck': '首',
        'Head': '頭',
        'Eye.L': '目.L',
        'Eye.R': '目.R',
        'Jaw': '口.R', #若干異なる
        'Shoulder.L': '肩.L',
        'Upper_Arm.L': '腕.L',
        'Lower_Arm.L': 'ひじ.L',
        'Hand.L': '手首.L',
        'Thumb_Proximal.L': '親指０.L',
        'Thumb_Intermediate.L': '親指１.L',
        'Thumb_Distal.L': '親指２.L',
        'Index_Proximal.L': '人指１.L',
        'Index_Intermediate.L': '人指２.L',
        'Index_Distal.L': '人指３.L',
        'Middle_Proximal.L': '中指１.L',
        'Middle_Intermediate.L': '中指２.L',
        'Middle_Distal.L': '中指３.L',
        'Ring_Proximal.L': '薬指１.L',
        'Ring_Intermediate.L': '薬指２.L',
        'Ring_Distal.L': '薬指３.L',
        'Little_Proximal.L': '小指１.L',
        'Little_Intermediate.L': '小指２.L',
        'Little_Distal.L': '小指３.L',
        'Shoulder.R' : '肩.R',
        'Upper_Arm.R' : '腕.R',
        'Lower_Arm.R' : 'ひじ.R',
        'Hand.R' : '手首.R',
        'Thumb_Proximal.R' : '親指０.R',
        'Thumb_Intermediate.R' : '親指１.R',
        'Thumb_Distal.R' : '親指２.R',
        'Index_Proximal.R' : '人指１.R',
        'Index_Intermediate.R' : '人指２.R',
        'Index_Distal.R' : '人指３.R',
        'Middle_Proximal.R' : '中指１.R',
        'Middle_Intermediate.R' : '中指２.R',
        'Middle_Distal.R' : '中指３.R',
        'Ring_Proximal.R' : '薬指１.R',
        'Ring_Intermediate.R' : '薬指２.R',
        'Ring_Distal.R' : '薬指３.R',
        'Little_Proximal.R' : '小指１.R',
        'Little_Intermediate.R' : '小指２.R',
        'Little_Distal.R' : '小指３.R',
        'Upper_Leg.L': '足.L',
        'Lower_Leg.L': 'ひざ.L',
        'Foot.L': '足首.L',
        'Toes.L': 'つま先.L',
        'Upper_Leg.R': '足.R',
        'Lower_Leg.R': 'ひざ.R',
        'Foot.R': '足首.R',
        'Toes.R': 'つま先.R'
    }
    for bone in bpy.context.active_object.data.bones:
        if bone.name in dic:
            bone.name = dic[bone.name]
rename_bones()
