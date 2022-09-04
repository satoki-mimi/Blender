import bpy

bpy.context.scene.render.image_settings.file_format = 'PNG'

#keys = bpy.data.shape_keys['Key'].key_blocks #Key名を指定する場合
keys = bpy.context.active_object.data.shape_keys.key_blocks #オブジェクトを指定する場合

for i in range(len(keys)):
    #filename = 'D:\\xxx\\xxx\\xxx\\' + keys[i].name + '.png' #日本語だとエラー
    filename = 'D:\\' + str(i) + '.png'
    if i > 0:
        keys[i-1].value = 0
    keys[i].value = 1
    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render(filepath = filename)
    
keys[len(keys)].value = 0
