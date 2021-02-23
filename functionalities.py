import hashlib
import time
from shutil import copyfile
from tkinter import filedialog
import os


class Functionalities:

    def remove_extension(self):
        self.extract_filename, self.extract_extension = os.path.splitext(self.filename)

    def encrypt_file(self):
        file = open(self.filename, "rb")
        data = file.read()
        self.hash_filename = hashlib.md5(data).hexdigest()
        file.close()

        data = bytearray(data)
        for index, value in enumerate(data):
            data[index] = value ^ self.key

        file = open(f'{self.hash_filename}-{self.extract_filename}{self.extract_extension}', "wb")
        file.write(data)
        file.close()
        self.move_file_to_path_save()

    def decrypt_file(self):
        file = open(self.filename, "rb")
        data = file.read()
        file.close()

        data = bytearray(data)
        for index, value in enumerate(data):
            data[index] = value ^ self.key

        file = open(self.filename, "wb")
        file.write(data)
        file.close()
        separate_hash = self.filename[0:33]
        file_2 = self.filename.replace(f'{separate_hash}', '')
        try:
            time.sleep(1)
            os.remove(file_2)
        except:
            pass

        os.rename(self.filename, file_2)


    def open_file_path_to_choice(self):
        self.folder_name_choose = filedialog.askdirectory()
        if (len(self.folder_name_choose) > 1):
            self.error_location.config(text=self.folder_name_choose, fg=os.getenv('green'))

        else:
            self.error_location.config(text=os.getenv('text_label_6'), fg=os.getenv('red'))

    def open_file_path_to_save(self):
        self.folder_name_save = filedialog.askdirectory()
        if (len(self.folder_name_save) > 1):
            self.error_location_2.config(text=self.folder_name_save, fg=os.getenv('green'))

        else:
            self.error_location_2.config(text=os.getenv('text_label_6'), fg=os.getenv('red'))

    def move_file_to_path_save(self):
        time.sleep(3)
        copyfile(self.folder_name_choose, self.folder_name_save)


