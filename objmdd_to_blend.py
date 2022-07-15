"""
# SPDX-License-Identifier: GPL-2.0-or-later

# Contributors: Thomas Lefranc
"""
"""
Ce programme permet d'automatiser le passage d'une simulation sofa à une 
interface graphique unity

prérequis:
    version :
        python 3.7
        blender 3.2
    librairies :
        pip install bpy && bpy_post_install
        pip install numpy 
"""

import os
import bpy
import import_mdd_spe #Librairie modifiée d'importation du fichier mdd

def obj_mdd_to_blend(disk,location,obj_raw,mdd_raw,name_blend,first_frame_anim,last_frame_anim,fps_anim):
    
    direc = os.path.join(disk,location) #On associe le dossier
    
    file_obj = os.path.join(direc, obj_raw) #On associe le fichier objet
    file_mdd = os.path.join(direc, mdd_raw) #On associe le fichier mdd
    
    #On supprimer tout les éléments qui existent déjà 
    print("Suppresion de tout les objets présent à l'ouverture du nouveau projet ...")
    bpy.ops.object.select_all(action='DESELECT')
    for o in bpy.context.scene.objects:
        o.select_set(True)
    bpy.ops.object.delete()
    print("Tout les objets supprimés avec succès")

    #On importe le fichier objet dans blender
    print("\nImportation du fichier objet : "+file_obj)
    bpy.ops.import_scene.obj(filepath = file_obj,split_mode='OFF') 
    print("Importation du fichier objet réussie")
    
    #On importe le fichier mdd dans blender
    import_mdd_spe.load(bpy.context,file_mdd,first_frame_anim)
    
    #Permet d'exporter le projet au format blend    
    print("\nExportation du fichier .blend ...")
    bpy.ops.wm.save_as_mainfile(filepath=name_blend) 
    print("Le fichier a été exporter avec succès : "+ direc +name_blend+".blend")
    
    #bpy.ops.export_scene.fbx(filepath=name_blend, use_selection=True) #Permet d'exporter le projet au format fbx