import hashlib
import os
import time
from shutil import copy2






def encrypt_file(choose_filename, key):
    extract_filename, extract_extension = os.path.splitext(choose_filename)
    time.sleep(1)
    file = open(choose_filename, "rb")
    data = file.read()
    hash_filename = hashlib.md5(data).hexdigest()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(f'{hash_filename}-{extract_filename}{extract_extension}', "wb")
    file.write(data)
    file.close()
    time.sleep(3)
    copy2(f'{hash_filename}-{extract_filename}{extract_extension}', folder_name_save)


def decrypt_file(choose_filename, key):
    file = open(choose_filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(choose_filename, "wb")
    file.write(data)
    file.close()
    separate_hash = choose_filename[0:33]
    file_2 = choose_filename.replace(f'{separate_hash}', '')
    try:
        time.sleep(1)
        os.remove(file_2)
    except:
        pass

    os.rename(choose_filename, file_2)



if __name__ == '__main__':
    key = 25
    print(key)
    time.sleep(2)

    choose_filename = 'test.txt'
    print(choose_filename)
    time.sleep(2)

    folder_name_save = r'C:\Users\caiom\Documents\GitHub\Cryptosome\tests\encrypt_test\save_here'
    print(folder_name_save)
    time.sleep(2)

    encrypt_file(choose_filename, key)