import bpy

def make_vrc_shape_keys_from_AIUEO():
    
    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    shapeKeys = bpy.context.active_object.data.shape_keys.key_blocks
    
    keyDic = {}
    for shapeKey in shapeKeys:
        if shapeKey.name == "A":
            keyDic["A"] = shapeKey
        elif shapeKey.name == "I":
            keyDic["I"] = shapeKey
        elif shapeKey.name == "U":
            keyDic["U"] = shapeKey
        elif shapeKey.name == "E":
            keyDic["E"] = shapeKey
        elif shapeKey.name == "O":
            keyDic["O"] = shapeKey
    
    vrcKeys = {
        "vrc.v_sil":{},
        "vrc.v_PP":{"I":0.1},
        "vrc.v_FF":{"I":0.4,"U":0.1},
        "vrc.v_TH":{"I":0.2,"U":0.5},
        "vrc.v_DD":{"I":0.3,"U":0.5},
        "vrc.v_kk":{"I":0.8,"U":0.4},
        "vrc.v_CH":{"I":0.7,"U":0.6},
        "vrc.v_SS":{"I":0.8,"U":0.2},
        "vrc.v_nn":{"I":0.7,"U":0.5},
        "vrc.v_RR":{"I":0.8,"U":0.5},
        "vrc.v_aa":{"A":1.0},
        "vrc.v_E":{"E":1.0},
        "vrc.v_ih":{"I":1.0},
        "vrc.v_oh":{"O":1.0},
        "vrc.v_ou":{"U":1.0}
    }
    
    for vrcKey in vrcKeys.keys():
        bpy.ops.object.shape_key_clear()

        aiueoKeys = vrcKeys[vrcKey]

        for aiueoKey in aiueoKeys.keys():
            keyDic[aiueoKey].value = aiueoKeys[aiueoKey]


        bpy.context.active_object.shape_key_add(name=vrcKey,from_mix=True)
    
    bpy.ops.object.shape_key_clear()
    
make_vrc_shape_keys_from_AIUEO()
