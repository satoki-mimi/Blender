import bpy

def add_empty_shape_keys():
    
    keys = [
        "Basis",
        "A",
        "I",
        "U",
        "E",
        "O",
        "BLINK",
        "JOY",
        "ANGRY",
        "SORROW",
        "FUN",
        "LOOKUP",
        "LOOKDOWN",
        "LOOKLEFT",
        "LOOKRIGHT",
        "BLINK_L",
        "BLINK_R",
        "vrc.v_sil",
        "vrc.v_PP",
        "vrc.v_FF",
        "vrc.v_TH",
        "vrc.v_DD",
        "vrc.v_kk",
        "vrc.v_CH",
        "vrc.v_SS",
        "vrc.v_nn",
        "vrc.v_RR",
        "vrc.v_aa",
        "vrc.v_E",
        "vrc.v_ih",
        "vrc.v_oh",
        "vrc.v_ou"
    ]

    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    for key in keys:
        bpy.context.active_object.shape_key_add(name=key)
    
add_empty_shape_keys()
