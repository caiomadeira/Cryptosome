from functionalities import Functionalities
from tkinter import *
from tkinter import ttk
import dotenv
import os

dotenv.find_dotenv()
dotenv.load_dotenv()


class MainApplication(Functionalities):

    def __init__(self):
        super().__init__()
        self.folder_name_choose = ""
        self.folder_name_save = ""
        self.root = Tk()
        self.screen_config()
        self.key = 0
        self.widgets()

        # self.screen()

    def screen_config(self):
        self.root.title(os.getenv('screen_title'))
        self.root.geometry(os.getenv('screen_size'))
        self.root.columnconfigure(0, weight=1)
        self.root.resizable = False

    def widgets(self):
        first_label = Label(self.root, text=os.getenv('text_label_0'),
                            font=(os.getenv('font_2'), os.getenv('smallsize_2')))
        first_label.grid()

        key_label = Label(self.root, text=os.getenv('text_label_8'),
                          font=os.getenv('font_2', os.getenv('smallsize_1')))
        key_label.grid()

        # self.key_entry_var = IntVar()
        self.key_entry = Entry(self.root, width=30)
        self.key_entry.grid()

        # ESCOLHER CAMINHO P/ ABRIR ==========================
        choose_path_label = Label(self.root, text=os.getenv('text_label_1'),
                                  font=os.getenv('font_2', os.getenv('smallsize_1')))
        choose_path_label.grid()

        self.select_path_entry = Entry(self.root, width=50)
        self.select_path_entry.grid()

        self.error_location = Label(self.root, text=os.getenv('text_label_2'), fg=os.getenv('red'),
                                    font=os.getenv('font_2'))
        self.error_location.grid()

        choose_path_button = Button(self.root, width=os.getenv('small_size_button'), bg=os.getenv('red'),
                                    fg=os.getenv('white'),
                                    text=os.getenv('text_button_0'), command=self.open_file_path_to_choice)
        choose_path_button.grid()
        # =====================================================
        # ESCOLHER CAMINHO P/ SALVAR ==========================

        choose_path_label_2 = Label(self.root, text=os.getenv('text_label_7'),
                                    font=os.getenv('font_2', os.getenv('smallsize_1')))
        choose_path_label_2.grid()

        self.select_path_entry_2 = Entry(self.root, width=50)
        self.select_path_entry_2.grid()

        self.error_location_2 = Label(self.root, text=os.getenv('text_label_2'), fg=os.getenv('red'),
                                      font=os.getenv('font_2'))
        self.error_location_2.grid()

        choose_path_button_2 = Button(self.root, width=os.getenv('small_size_button'), bg=os.getenv('red'),
                                      fg=os.getenv('white'),
                                      text=os.getenv('text_button_0'), command=self.open_file_path_to_save)
        choose_path_button_2.grid()
        # =====================================================
        # ESCOLHER A HASH E ENCRYPT ==========================
        choose_hash_label = Label(self.root, text=os.getenv('text_label_5'), font=os.getenv('smallsize_2'))
        choose_hash_label.grid()

        choice_hash_box = ttk.Combobox(self.root, values=os.getenv('choice_hash'))
        choice_hash_box.grid()

        encrypt_button = Button(self.root, text=os.getenv('text_button_1'), width=10, bg=os.getenv('red'),
                                fg=os.getenv('white'), command=self.encrypt_file)
        encrypt_button.grid()
        # =====================================================
        # CREDITS ==========================

        credits_label = Label(self.root, text=os.getenv('text_credits'),
                              font=os.getenv('arial', os.getenv('smallsize_1')))
        credits_label.grid()


if __name__ == '__main__':
    main = MainApplication()
    mainloop()
