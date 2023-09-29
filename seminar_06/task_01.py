# Напишите функцию, которая принимает на вход строку
#  - абсолютный путь до файла.
#  Функция возвращает кортеж из трёх элементов:
#  путь, имя файла, расширение файла.


import os

def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)

print(parse_path('C:\Pythoon_Hwp\seminar_06\task_01.py'))


# def divine_path(full_path: str):
#     def divine(abs_path: str, div: str) -> tuple:
#         abs_path = abs_path.split(div)
#         file_name, extension = abs_path[-1].split('.')
#         path = div.join(abs_path[:-1])
#         return path, file_name, extension

#     return divine(full_path, '/') if '/' in full_path else divine(full_path, '\\')


# print(divine_path('C:\Pythoon_Hwp\seminar_06\task_01.py'))