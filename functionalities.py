#-*- coding: utf-8 -*-
import hashlib
import sys
import time
from shutil import copy2
from tkinter import filedialog
import os


class Functionalities:
    def quit(self):
        sys.exit(1)
    def open_file_path_to_choice(self):
        self.folder_name_choose = filedialog.askopenfilename(initialdir="Desktop", title=os.getenv('text_label_9'),
                                                             filetypes=(("all files", "*.*"), ("all files", "*.*")))
        self.remove_path_from_filename = os.path.basename(self.folder_name_choose)

        if len(self.folder_name_choose) > 1:
            self.error_location.config(text=self.folder_name_choose, fg=os.getenv('green'))

        else:
            self.error_location.config(text=os.getenv('text_label_6'), fg=os.getenv('red'))

    def open_file_path_to_save(self):
        self.folder_name_save = filedialog.askdirectory()
        if len(self.folder_name_save) > 1:
            self.error_location_2.config(text=self.folder_name_save, fg=os.getenv('green'))

        else:
            self.error_location_2.config(text=os.getenv('text_label_6'), fg=os.getenv('red'))

    def clear_screen(self):
        self.error_location.config(text='')
        self.error_location_2.config(text='')

    def encrypt_file(self):
        extract_filename, extract_extension = os.path.splitext(self.remove_path_from_filename)
        time.sleep(1)
        file = open(self.folder_name_choose, "rb")
        data = file.read()
        hash_filename = hashlib.md5(data).hexdigest()
        file.close()

        data = bytearray(data)
        for index, value in enumerate(data):
            data[index] = value ^ int(self.key_entry.get())

        file = open(f'{hash_filename}-{extract_filename}{extract_extension}', "wb")
        file.write(data)
        file.close()
        time.sleep(1)
        copy2(f'{hash_filename}-{extract_filename}{extract_extension}', self.folder_name_save)
        self.sucess_label.config(text=os.getenv('text_label_10'), fg=os.getenv('green'))
        time.sleep(0.5)
        self.clear_screen()

    def decrypt_file(self):
        file = open(self.folder_name_choose, "rb")
        data = file.read()
        file.close()

        data = bytearray(data)
        for index, value in enumerate(data):
            data[index] = value ^ int(self.key_entry.get())

        file = open(self.folder_name_choose, "wb")
        file.write(data)
        file.close()
        separate_hash = self.folder_name_choose[0:33]
        file_2 = self.folder_name_choose.replace(f'{separate_hash}', '')
        try:
            time.sleep(1)
            os.remove(file_2)
        except:
            pass

        self.renamed = os.rename(self.folder_name_choose, file_2)
        copy2(str(self.renamed), self.folder_name_save)
        self.sucess_label.config(text=os.getenv('text_label_11'), fg=os.getenv('green'))
        time.sleep(0.5)
        self.clear_screen()
