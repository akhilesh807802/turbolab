from hashlib import md5
import os
def find_duplicates():
    hashes = []
    duplicates = {}
    duplicate_files = []
    for filename in os.listdir('data'):
        if os.path.isfile(os.path.join('data/', filename)):
            content = open(os.path.join('data/', filename))
            filehash = md5(content.read().encode()).hexdigest()
            if filehash not in hashes:
                hashes.append(filehash)
                duplicates[filehash] = [filename]
            else:
                duplicates[filehash].append(filename)
    for each in duplicates:
        temp = []
        for each in duplicates[each]:
            temp.append(each.strip('.txt'))
        duplicate_files.append(temp)
    return duplicate_files

if __name__ == '__main__':
    result = find_duplicates()
    for row in result:
        print(" ".join(str(i) for i in row))
