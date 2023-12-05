#things to add:
#-change sorting dictionary
#-add logging space into gui
import os
import json
from tkinter import *
from tkinter import filedialog as fd

main_path = ''
with open('C:\\allprojects\\python\\filesortutilit\\src\\ext.json') as f:
    extensions = json.loads(f.read())
'''extensions = {

"video": ["mp4", "mov", "avi", "mkv", "wmv", "3gp", "3g2", "mpg", "mpeg", "m4v",
              "h264", "flv", "rm", "swf", "vob"],

    "data": ["sql", "sqlite", "sqlite3", "csv", "dat", "db", "log", "mdb", "sav",
             "tar", "xml", "json", "accdb"],

    "audio": ["mp3", "wav", "ogg", "flac", "aif", "mid", "midi", "mpa", "wma", "wpl",
              "cda", "m4a"],

    "image": ["jpg", "png", "bmp", "ai", "psd", "ico", "jpeg", "ps", "svg", "tif",
              "tiff", "webp", "jfif"],

    "archive": ["zip", "rar", "7z", "z", "gz", "rpm", "arj", "pkg", "deb"],

    "text": ["pdf", "txt", "doc", "docx", "rtf", "tex", "wpd", "odt", "fb2", "djvu"],

    "3d": ["stl", "obj", "fbx", "dae", "3ds", "iges", "step", "blend"],

    "presentation": ["pptx", "ppt", "pps", "key", "odp", "ppsx"],

    "spreadsheet": ["xlsx", "xls", "xlsm", "ods"],

    "font": ["otf", "ttf", "fon", "fnt"],

    "gif": ["gif"],

    "exe": ["exe"],

    "iso": ["iso"],

    "ova": ["ova"],

    "msi": ["msi"],

    "bat": ["bat"],

    "apk": ["apk"],

    "sourcecode": ["py", "js", "cpp", "css", "html", "php", "asm", "c"],

    "torrents": ["torrent"]
}'''

def create_folders_from_list(folder_path, folder_name):
    for folder in folder_name:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')

def get_subfolder_paths(folder_path):
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    return subfolder_paths

def get_subfolders_paths(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)
    subfolder_names = [f.split('\\')[-1] for f in subfolder_paths]

    return subfolder_names

def get_file_paths(folder_path):
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths

def get_file_names(folder_path):
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
    file_names = [f.split('\\')[-1] for f in file_paths]

    return file_names

def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())
    # checking if file extension and existans in ext_folder
    # if not moving to this folder
    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]
        for dict_key_int in range(len(ext_list)):
            movto_path = folder_path + '\\' + ext_list[dict_key_int][0]
            #print(movto_path + '\\' + file_name)
            if extension in ext_list[dict_key_int][1]:
                print(os.path.exists(movto_path + '\\' + file_name))
                if not os.path.exists(movto_path + '\\' + file_name):
                    print(f"Moving {file_name} to {ext_list[dict_key_int][0]} folder")
                    os.rename(file_path, f'{movto_path}\\{file_name}')
                else:
                    print(f"Removing {file_path}, because it has dublicate in {movto_path}")
                    os.remove(file_path)

def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)

def set_main_path():
    main_path = fd.askdirectory().replace('/', '\\')
    print('Sorting files in folder ' + main_path)
    create_folders_from_list(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)

if __name__ == '__main__':
    window = Tk()
    window.title("Сортировщик файлов")
    window.resizable(False, False)
    window.geometry('300x100')
    ask_btn = Button(window, text ="choose directory", command=set_main_path)
    ask_btn.pack(fill = BOTH, expand = True, anchor='center')
    window.mainloop()



