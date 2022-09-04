import bpy

dir = bpy.context.scene.render.filepath
#keys = bpy.data.shape_keys['Key'].key_blocks #Key名を指定する場合
keys = bpy.context.active_object.data.shape_keys.key_blocks #オブジェクトを指定する場合

for i in range(len(keys)):
    #filename = keys[i].name + '.png' #日本語だとエラー
    filename = str(i) + '.png'
    path = dir + filename
    if i > 0:
        keys[i-1].value = 0
    keys[i].value = 1
    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render(filepath = path)
    
keys[len(keys)-1].value = 0
