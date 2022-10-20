# Geometry Nodes
- brushtail
  - Blender 3.1.2 で作成した、ふさふさのしっぽ。Sketchfab（以下のURL）で3Dモデルを公開している。
    - https://sketchfab.com/3d-models/brushtail-77cb8f8f9556482a8000021f187ceb9a

# Python
- addEmptyShapeKeys
  - VRChatとVRMで利用する空のshape keyを作成する。
- assignWeight_to_OverlappingVertices
  - ボーンのTailと同じ座標にある頂点に、ボーンのウェイトを割り当てる
- makeVRChatShapeKeysFromAIUEO
  - 「あいうえお」のshape keyをミックスして、VRChatで利用するshape keyを作成する。
- overlayBones
  - 名前が同じボーンの位置を合わせる。
- renameBones
  - renameBones_unityHumanoid2pmx
  - renameBones_vrm2pmx
  - renameBones_vrm2unityHumanoid
    - 3Dモデルの規格に合わせてボーンの名前を変更する。
    - 普段は、VRoidモデル（VRM） -> UnityのHumanoid -> MMDモデル（PMX）の順にリネームしている。
- renderImagesForeachShapeKey
  - シェイプキーごとに画像をレンダリングする。表情の一覧を得るために作成した。
