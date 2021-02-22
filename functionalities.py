import os
import hashlib
import time


class Functionalities:

    def remove_extension(self, filename):
        self.extract_filename, self.extract_extension = os.path.splitext(filename)

    def encrypt_file(self, filename, key):
        file = open(filename, "rb")
        data = file.read()
        self.hash_filename = hashlib.md5(data).hexdigest()
        file.close()

        data = bytearray(data)
        for index, value in enumerate(data):
            data[index] = value ^ key

        file = open(f'{self.hash_filename}-{self.extract_filename}{self.extract_extension}', "wb")
        file.write(data)
        file.close()

    def decrypt_file(self, filename, key):
        file = open(filename, "rb")
        data = file.read()
        file.close()

        data = bytearray(data)
        for index, value in enumerate(data):
            data[index] = value ^ key

        file = open(filename, "wb")
        file.write(data)
        file.close()
        separate_hash = filename[0:33]
        file_2 = filename.replace(f'{separate_hash}', '')
        try:
            time.sleep(1)
            os.remove(file_2)
        except:
            pass

        os.rename(filename, file_2)

