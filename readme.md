# Addon
- symmetrize_two_vertices.py
  - 選択した２つの頂点に関して、x座標が正の方の頂点が、x座標が負の方の頂点と鏡合わせになるように移動させる。

# Geometry Nodes
- brushtail
  - Blender 3.1.2 で作成した、ふさふさのしっぽ。Sketchfab（以下のURL）で3Dモデルを公開している。
    - https://sketchfab.com/3d-models/brushtail-77cb8f8f9556482a8000021f187ceb9a

# Python
- add_empty_shape_keys
  - VRChatとVRMで利用する空のshape keyを作成する。
- assign_weight_to_overlapping_vertices
  - ボーンのTailと同じ座標にある頂点に、ボーンのウェイトを割り当てる
- equalize_edges_length
  - エッジの長さを揃える
- make_vrchat_shape_keys_from_aiueo
  - 「あいうえお」のshape keyをミックスして、VRChatで利用するshape keyを作成する。
- overlay_bones
  - 名前が同じボーンの位置を合わせる。
- rename_bones
  - rename_bones_unity_humanoid_to_pmx
  - rename_bones_vrm_to_pmx
  - rename_bones_vrm_to_unity_humanoid
    - 3Dモデルの規格に合わせてボーンの名前を変更する。
    - 普段は、VRoidモデル（VRM） -> UnityのHumanoid -> MMDモデル（PMX）の順にリネームしている。
- render_images_foreach_shape_key
  - シェイプキーごとに画像をレンダリングする。表情の一覧を得るために作成した。
- symmetrize_vertices
  - メッシュが左右対称となるように頂点の座標を修正する。
