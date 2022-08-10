import bpy
import os

bpy.context.scene.render.image_settings.file_format = 'PNG'
keys = bpy.data.shape_keys["Key"].key_blocks #"Key.001"かもしれない

for i in range(len(keys)):
    #filename = "D:\\xxx\\xxx\\xxx\\" + keys[i].name + ".png" #日本語だとエラー
    filename = "C:\xxx\\xxx\\xxx\\" + str(i) + ".png"
    if i > 0:
        keys[i-1].value = 0
    keys[i].value = 1
    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render(filepath = filename)
keys[len(keys)].value = 0
