import bpy

def make_vrchat_shape_keys_from_aiueo():
    
    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    shape_keys = bpy.context.active_object.data.shape_keys.key_blocks
    
    key_dic = {}
    for shape_key in shape_keys:
        if shape_key.name == "A":
            key_dic["A"] = shape_key
        elif shape_key.name == "I":
            key_dic["I"] = shape_key
        elif shape_key.name == "U":
            key_dic["U"] = shape_key
        elif shape_key.name == "E":
            key_dic["E"] = shape_key
        elif shape_key.name == "O":
            key_dic["O"] = shape_key
    
    vrc_keys = {
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
    
    for vrc_key in vrc_keys.keys():
        bpy.ops.object.shape_key_clear()
        aiueo_keys = vrc_keys[vrc_key]
        for aiueo_key in aiueo_keys.keys():
            key_dic[aiueo_key].value = aiueo_keys[aiueo_key]
        bpy.context.active_object.shape_key_add(name=vrc_key,from_mix=True)
    bpy.ops.object.shape_key_clear()
    
make_vrchat_shape_keys_from_aiueo()
