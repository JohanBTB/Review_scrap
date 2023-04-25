# -*- coding: utf-8 -*-
import os
import json
def merge(paths , filename, key, unique=False):
    """
    recupera los archivos json

    En caso de querer ser unicos, se creara un set con los "key"
    En caso haya un "objeto" que su "key" no este en el set de "keys", no sera agregado. En caso contrario, se agregara en la lista de "objetos" y el "key" del objeto se agregara al set de "keys".

    En caso de no querer ser unicos, se creara una lista global en el que se agregaran los dicts
    """
    list_dicts = []
    current_directory = os.getcwd()
    json_directory = "json_processing\\json_files"
    set_keys = set()
    for path in paths:
        
        path = os.path.join(current_directory, path)
        list_dir = os.listdir(path)
        for file in list_dir:
            try:
                with open(os.path.join(path,file)) as f:
                    data = json.load(f)
                    if unique and key:
                        for d in data:
    
                            if (d[key] in set_keys):
                                continue
                            set_keys.add(d[key])
                            list_dicts.append(d)
                    else:
                        list_dicts.extend(data)
                    
                    
            except FileNotFoundError:
                    return print("The file does not exist.")
    
    if not os.path.exists(os.path.join(current_directory, json_directory)):
        os.mkdir(os.path.join(current_directory, json_directory))
        
    with open(os.path.join(current_directory, json_directory,filename ),"w") as json_dir:
        json.dump(list_dicts, json_dir, indent=4)


            
