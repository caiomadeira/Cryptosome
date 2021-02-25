from functionalities import Functionalities
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import dotenv
import os

dotenv.find_dotenv()
dotenv.load_dotenv()


class MainApplication(Functionalities):

    def __init__(self):
        self.folder_name_choose = ""
        self.folder_name_save = ""
        self.root = Tk()
        self.screen_config()
        self.screen_frames()
        self.widgets()

    def screen_config(self):
        self.root.title(os.getenv('screen_title'))
        self.root.geometry(os.getenv('screen_size'))
        self.root.columnconfigure(0, weight=1)
        self.root.iconbitmap('static/img/favicon.ico')
        # self.root.protocol("WM_DELETE_WINDOW", self.root.iconify)
        self.root.resizable(False, False)
        self.root.configure(background=os.getenv('gray'))

    def screen_frames(self):
        self.frame_encrypt = Frame(self.root)
        self.frame_encrypt.grid(ipadx=130, ipady=1, padx=(10, 10), pady=(10, 10))
        self.frame_encrypt.configure(background=os.getenv('blue'))

    def header(self):
        image = Image.open(os.getenv('logo_background')).resize((250, 250), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(image)

        panel = Label(self.frame_encrypt, image=pic, borderwidth=0)
        panel.image = pic
        panel.grid(padx=145, pady=5)

    def widgets(self):
        self.header()
        key_label = Label(self.frame_encrypt, text=os.getenv('text_label_8'),
                          font=os.getenv('font_2', os.getenv('smallsize_1')), bg=os.getenv('blue'), fg=os.getenv('blue_1'))
        key_label.grid(pady=(0, 2))

        self.key_entry_var = IntVar()
        self.key_entry = Entry(self.frame_encrypt, width=30, textvariable=self.key_entry_var)
        self.key_entry.grid(pady=(0, 15))

        # ESCOLHER CAMINHO P/ ABRIR ==========================

        self.error_location = Label(self.frame_encrypt, text=os.getenv('text_label_2'), fg=os.getenv('blue_1'),
                                    font=os.getenv('font_2'), bg=os.getenv('blue'))
        self.error_location.grid()

        choose_path_button = Button(self.frame_encrypt, width=os.getenv('small_size_button'), bg=os.getenv('blue_2'),
                                    fg=os.getenv('black'),
                                    text=os.getenv('text_button_0'), command=self.open_file_path_to_choice)
        choose_path_button.grid(pady=(2, 10))
        # =====================================================
        # ESCOLHER CAMINHO P/ SALVAR ==========================

        self.error_location_2 = Label(self.frame_encrypt, text=os.getenv('text_label_2'), fg=os.getenv('blue_1'),
                                      font=os.getenv('font_2'), bg=os.getenv('blue'))
        self.error_location_2.grid()

        choose_path_button_2 = Button(self.frame_encrypt, width=os.getenv('small_size_button'), bg=os.getenv('blue_2'),
                                      fg=os.getenv('black'),
                                      text=os.getenv('text_button_2'), command=self.open_file_path_to_save)
        choose_path_button_2.grid(pady=(2, 10))
        # =====================================================
        # ESCOLHER A HASH E ENCRYPT ===========================
        # choose_hash_label = Label(self.frame_encrypt, text=os.getenv('text_label_5'), font=os.getenv('smallsize_2'))
        # choose_hash_label.grid(pady=10)
        #
        # choice_hash_box = ttk.Combobox(self.frame_encrypt, values=os.getenv('choice_hash'))
        # choice_hash_box.grid(pady=10)

        encrypt_button = Button(self.frame_encrypt, text=os.getenv('text_button_1'), width=10, bg=os.getenv('blue_2'),
                                fg=os.getenv('black'), command=self.encrypt_file)
        encrypt_button.grid(pady=10)

        decrypt_button = Button(self.frame_encrypt, text=os.getenv('text_button_3'), width=12, bg=os.getenv('blue_2'),
                                fg=os.getenv('black'), command=self.decrypt_file)
        decrypt_button.grid(pady=10, padx=(4, 10))

        self.sucess_label = Label(self.frame_encrypt, text='', fg=os.getenv('green'),
                                  font=os.getenv('arial', os.getenv('medium_size_button')), bg=os.getenv('blue'))
        self.sucess_label.grid(pady=10)


if __name__ == '__main__':
    main = MainApplication()
    mainloop()
