import os
import shutil
import re
import sys
from pathlib import Path
import pathlib
from shutil import unpack_archive

#отримання списку файлів
def get_file_list(folder):
#перетворюємо шлях до папки в об'єкт
    try:
        folder = Path(folder)
    except FileNotFoundError:
        print(f"file {folder} is not found")
    finally:
        print(folder)
    file_list = sorted(folder.glob("**/*"))  # знаходимо список всіх файлів
    return file_list # повертаємо список файлів

#перекладає папки,для перекладу кирилиці

JPEG_IMAGES=[]
MP4_VIDEO=[]
TXT_DOCUMENTS=[]
ZIP_ARCHIVES=[]
MP3_MUSIC=[]
OTHER = []

REGISTER_EXTENSIONS = {
    "JPEG": "images",
    "JPG": "images",
    "PNG": "images",
    "SVG": "images",
    "GIF": "images",
    "MP3": "audio",
    "OGG": "audio",
    "WAV": "audio",
    "AMR": "audio",
    "MP4": "video",
    "AVI": "video",
    "MOV": "video",
    "MKV": "video",
    "DOC": "document",
    "DOCX": "document",
    "TXT": "document",
    "PDF": "document",
    "XLSX": "document",
    "XLS": "document",
    "CSV": "document",
    "PPTX": "document",
    "ZIP": "archives",
    "GZ": "archives",
    "TAR": "archives",
    "RAR": "archives",
    "ARJ": "archives",
    "APP": "programs",
    "PY": "programs",
    "HTML": "programs",
    "BIN": "programs",
    "DAT": "programs",
    "JSON": "programs",
    "XLM": "programs",
    "PKG": "programs",
    "JS": "programs",
    "YML": "programs",
    "YAML": "programs",
    "MD": "programs",
    "": "other",
} 

FOLDERS = []
EXTENTIONS = set()
UNKNOWN = set()


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
    
def normalize(name: str) -> str:
    t_name = name.translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    return t_name

def get_extention(filename:str)-> str:
    return Path(filename).suffix[:1].upper()

#сортує папки

def sorter(folder):
    file_list = get_file_list(folder)
    result_dict = {}
    for file in [files for files in file_list if files.is_file()]:
        ext = file.suffix[1:].upper()
        file_type = REGISTER_EXTENSIONS.get(ext,"other")
        if result_dict.get((ext,file_type)):
            result_dict[(ext,file_type)].append(file)
        else:
            result_dict[(ext,file_type)]=[file] #список файлів
    return result_dict


#видаляє папки
def remove_folders():
    folders = sorted(Path('.').glob('*'))
    for i in FOLDERS:
        if FOLDERS == "_":
            return folders, FOLDERS.delete

#перевіряє чи є другий параметр
def paramether(first_argument, second_argument):
    while first_argument == True and second_argument == True:
        return paramether
    
    try:
        first_argument == True and second_argument == False
    except TypeError:
        return "We do not finde yout paramether"
        
#розпаковку архівів за допомогою shutil.unpack_archive()
def delete_folder(folder: str):
    folder = "C:/Users/Anwender/Desktop/so_much/resume.zip"
    extract_dir = "C:/Users/Anwender/Desktop/so_much"
    format = "zip"
    shutil.unpack_archive(folder[ extract_dir[ format]])
    unpack_archive("resume.zip", './sample', "zip")

#Функція file_parser() - це головна функція."""
def file_parser(folder_for_scan):

    try:
        sorted_file_dict = sorter(folder_for_scan)
    except FileNotFoundError:
        return (
            f"Not able to find ,{folder_for_scan}, folder. Please enter a correct folder name."
        )
    except IndexError:
        return "Please enter a folder name."
    except IsADirectoryError:
        return "Unknown file"
    for file_types, files in sorted_file_dict.items():
        for file in files:
            if not(folder_for_scan / file_types[1]).exists():
                 (folder_for_scan / file_types[1]).mkdir()
            if not (folder_for_scan / file_types[1] / file_types[0]).exists():
                (folder_for_scan / file_types[1] / file_types[0]).mkdir()
            file.replace(folder_for_scan / file_types[1] / file_types[0] / file.name)


# 2 конструкція if name == main
if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    file_parser(Path(folder_for_scan))
    print(f"Start in folder {folder_for_scan}")