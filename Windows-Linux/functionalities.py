import hashlib
import time
from shutil import copy2
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *
from strings.pt_br import text_credits_2
import os
import dotenv

dotenv.find_dotenv()
dotenv.load_dotenv()


class Functionalities:
    def quit(self):
        sys.exit(1)

    def credits(self):
        self.credits_screen = tk.Tk()
        self.credits_screen.attributes('-alpha', 0.0)
        self.credits_screen.iconify()
        self.window = tk.Toplevel(self.credits_screen)
        w = self.window.winfo_reqwidth()
        h = self.window.winfo_reqheight()
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.window.geometry('+%d+%d' % (x, y))
        self.window.overrideredirect(1)
        close = tk.Button(self.window,
                          text=text_credits_2,
                          bg=os.getenv('blue_light'),
                          fg=os.getenv('white'),
                          command=lambda: self.credits_screen.destroy())
        close.pack(fill=tk.BOTH, expand=1)
        self.window.mainloop()

        self.credits_screen.mainloop()

    def dark_mode(self):

        self.root.configure(background=os.getenv('black_dark'))

        self.credits_btn.config(bg=os.getenv('blue_dark'),
                                fg=os.getenv('blue_1_dark'))

        self.quit_btn.config(bg=os.getenv('blue_dark'),
                             fg=os.getenv('blue_1_dark'))

        self.frame_encrypt.configure(background=os.getenv('blue_dark'))

        self.panel.configure(image=self.pic2)
        self.panel.image = self.pic2

        self.key_label.config(bg=os.getenv('blue_dark'),
                              fg=os.getenv('blue_1_dark'))

        self.error_key.config(bg=os.getenv('blue_dark'),
                              fg=os.getenv('blue_1_dark'))

        self.error_location.config(bg=os.getenv('blue_dark'),
                                   fg=os.getenv('blue_1_dark'))

        self.choose_path_button.config(bg=os.getenv('blue_dark'),
                                       fg=os.getenv('blue_1_dark'))

        self.error_location_2.config(bg=os.getenv('blue_dark'),
                                     fg=os.getenv('blue_1_dark'))

        self.choose_path_button_2.config(bg=os.getenv('blue_dark'),
                                         fg=os.getenv('blue_1_dark'))

        self.encrypt_button.config(bg=os.getenv('blue_dark'),
                                   fg=os.getenv('blue_1_dark'))

        self.decrypt_button.config(bg=os.getenv('blue_dark'),
                                   fg=os.getenv('blue_1_dark'))

        self.sucess_label.config(bg=os.getenv('blue_dark'),
                                 fg=os.getenv('blue_1_dark'))

    def light_mode(self):

        self.root.configure(background=os.getenv('gray_light'))

        self.credits_btn.config(bg=os.getenv('blue_2_light'),
                                fg=os.getenv('black'))

        self.quit_btn.config(bg=os.getenv('blue_2_light'),
                             fg=os.getenv('black'))

        self.frame_encrypt.configure(background=os.getenv('blue_light'))

        self.panel.configure(image=self.pic)
        self.panel.image = self.pic

        self.key_label.config(bg=os.getenv('blue_light'),
                              fg=os.getenv('blue_1_light'))

        self.error_key.config(bg=os.getenv('blue_light'),
                              fg=os.getenv('blue_1_light'))

        self.error_location.config(bg=os.getenv('blue_light'),
                                   fg=os.getenv('blue_1_light'))

        self.choose_path_button.config(bg=os.getenv('blue_2_light'),
                                       fg=os.getenv('black'))

        self.error_location_2.config(bg=os.getenv('blue_light'),
                                     fg=os.getenv('blue_1_light'))

        self.choose_path_button_2.config(bg=os.getenv('blue_2_light'),
                                         fg=os.getenv('black'))

        self.encrypt_button.config(bg=os.getenv('blue_2_light'),
                                   fg=os.getenv('black'))

        self.decrypt_button.config(bg=os.getenv('blue_2_light'),
                                   fg=os.getenv('black'))

        self.sucess_label.config(bg=os.getenv('blue_light'),
                                 fg=os.getenv('green_light'))

    def open_file_path_to_choice(self):
        self.folder_name_choose = filedialog.askopenfilename(initialdir="Desktop", title=os.getenv('text_label_9'),
                                                             filetypes=(("all files", "*.*"), ("all files", "*.*")))
        self.remove_path_from_filename = os.path.basename(self.folder_name_choose)

        if len(self.folder_name_choose) > 1:
            self.error_location.config(text=self.folder_name_choose, fg=os.getenv('green_light'))

        else:
            self.error_location.config(text=os.getenv('text_label_6'), fg=os.getenv('red_light'))

    def open_file_path_to_save(self):
        self.folder_name_save = filedialog.askdirectory()
        if len(self.folder_name_save) > 1:
            self.error_location_2.config(text=self.folder_name_save, fg=os.getenv('green_light'))

        else:
            self.error_location_2.config(text=os.getenv('text_label_6'), fg=os.getenv('red_light'))

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
            try:
                data[index] = value ^ int(self.key_entry.get())
            except ValueError:
                self.error_key.config(text='A chave deve ser menor que 255.', fg=os.getenv('red_light'))
                return
            if int(self.key_entry.get()) <= 0:
                self.error_key.config(text='A chave deve ser maior que 0.', fg=os.getenv('red_light'))
                return

        file = open(f'{hash_filename}-{extract_filename}{extract_extension}', "wb")
        file.write(data)
        file.close()
        time.sleep(1)
        copy2(f'{hash_filename}-{extract_filename}{extract_extension}', self.folder_name_save)
        self.sucess_label.config(text=os.getenv('text_label_10'), fg=os.getenv('green_light'))
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
        self.sucess_label.config(text=os.getenv('text_label_11'), fg=os.getenv('green_light'))
        time.sleep(0.5)
        self.clear_screen()
