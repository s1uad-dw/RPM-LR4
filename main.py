import os

def f1 (age = (str(input("Укажите путь:")))):
    while True:
        if os.path.exists(age):
            a = os.path.abspath(age)
            print("Путь указан верно")
            return os.path.abspath(age)
        else:
            print("Путь указан неверно")

def size(path,level=1, dict1 = {}):
    for i in os.listdir(path):
        if os.path.isdir(path+"/"+i):
            size(path+"/"+i,level+1)
        else:
            dict1[path+"/"+ i]= os.stat(path+"/"+ i).st_size
    return dict1
gi
def get_duplicates(d):
    result = {}
    for path, size in d.items():
        name = os.path.basename(path)
        if (name, size) in result:
            result[(name, size)].append(path)
        else:
            result[(name, size)] = [path]
    return {k: v for k, v in result.items() if len(v) > 1}


