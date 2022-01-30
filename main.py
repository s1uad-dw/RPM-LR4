import os


def get_duplicates(d):
    result = {}
    for path, size in d.items():
        name = os.path.basename(path)
        if (name, size) in result:
            result[(name, size)].append(path)
        else:
            result[(name, size)] = [path]
    return {k: v for k, v in result.items() if len(v) > 1}

#print(get_duplicates({'C:\\Users\\Admin\\folder1\\file1.txt':'100 Кб',
#   'C:\\Users\\Admin\\file1.txt':'100 Кб',
#   'C:\\Users\\Admin\\folder2\\file1.txt':'100 Кб',
#   'C:\\Users\\Admin\\folder3\\folder4\\file1.txt':'100 Кб',
#   'C:\\Users\\Admin\\folder1\\file2.txt':'100 Кб',
#   'C:\\Users\\Admin\\file2.txt':'100 Кб',
#   'C:\\Users\\Admin\\folder2\\file2.txt':'100 Кб',
#   'C:\\Users\\Admin\\folder3\\folder4\\file2.txt':'100 Кб',
#   'C:\\Users\\Admin\\folder8\\file1.txt':'109 Кб',
#   'C:\\Users\\Admin\\folder7\\file1.txt':'109 Кб',
#   'C:\\Users\\Admin\\folder9\\file1.txt':'109 Кб',
#   'C:\\Users\\Admin\\folder6\\folder4\\file1.txt':'109 Кб',
#   'C:\\Users\\Admin\\folder7\\file3.txt':'109 Кб',
#   'C:\\Users\\Admin\\folder9\\file4.txt':'109 Кб',
#   'C:\\Users\\Admin\\folder6\\folder4\\file5.txt':'109 Кб',
#  }))
