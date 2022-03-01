import os

def take_path ():
    while True:
        path = str(input('Введите путь: '))
        if os.path.isdir(path):
            return os.path.abspath(path)

def create_dictionary (path, dict1 = {}):
    for i in os.listdir(path):
        try:
            if os.path.isdir(path+"/"+i):
                create_dictionary(path+"/"+i)
            else:
                dict1[path+"/"+ i]= os.stat(path+"/"+ i).st_size
        except PermissionError:
            print("Недостаточно прав. Попробуйте запустить программу от имени администратора или суперпользователя")
    return dict1

def check_dictionary(d):
    result = {}
    for path, size in d.items():
        name = os.path.basename(path)
        if (name, size) in result:
            result[(name, size)].append(path)
        else:
            result[(name, size)] = [path]
    return {k: v for k, v in result.items() if len(v) > 1}

def output(dublicates):
    if len(dublicates)!=0:
        print('Найдены повторяющиеся файлы:')
        for filename in dublicates.keys():
            print('\nФайл', filename, 'в директориях:')
            for path in dublicates[filename]:
                print(path)
    else:
        print('Повторяющиеся файлы не найдены')
        
output(check_dictionary(create_dictionary(take_path())))
