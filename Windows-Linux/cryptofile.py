from functionalities import Functionalities
from tkinter import *
from PIL import ImageTk, Image
import dotenv
import os
from strings.pt_br import text_label_8, text_label_2, text_button_0, text_button_2, text_button_1, text_button_3, fonts, \
    text_quit, text_credits

dotenv.find_dotenv()
dotenv.load_dotenv()


class MainApplication(Functionalities):

    def __init__(self):
        self.folder_name_choose = ""
        self.folder_name_save = ""
        self.root = Tk()
        self.pic = ""
        self.pic2 =""
        self.screen_config()
        self.screen_frames()
        self.widgets()

    def screen_config(self):
        self.root.title(os.getenv('screen_title'))
        self.root.geometry(os.getenv('screen_size'))
        self.root.columnconfigure(0, weight=1)
        self.root.iconbitmap('static/img/favicon.ico')
        self.root.protocol("WM_DELETE_WINDOW", self.root.iconify)
        self.root.resizable(False, False)
        self.root.configure(background=os.getenv('gray_light'))

    def menu_top(self):
        self.credits_btn = Button(self.frame_encrypt,
                             width=10,
                             bg=os.getenv('blue_2_light'),
                             fg=os.getenv('black'),
                             text=text_credits,
                             font=(fonts['Helvetica'], 8),
                             command=self.credits)
        self.credits_btn.place(x=10, y=10)

        self.quit_btn = Button(self.frame_encrypt,
                          width=5,
                          bg=os.getenv('blue_2_light'),
                          fg=os.getenv('black'),
                          text=text_quit,
                          font=(fonts['Helvetica'], 8),
                          command=self.quit)
        self.quit_btn.place(x=460, y=10)

    def switch(self):
        switch_frame = Frame(self.frame_encrypt)
        switch_frame.grid()

        switch_variable = StringVar(value="off")
        on_btn = Radiobutton(switch_frame, text="On", variable=switch_variable,
                             indicatoron=False, value="on", width=8, command=self.dark_mode)
        off_btn = Radiobutton(switch_frame, text="Off", variable=switch_variable,
                              indicatoron=False, value="off", width=8, command=self.light_mode)

        on_btn.pack(side="left")
        off_btn.pack(side="left")

    def screen_frames(self):
        self.frame_encrypt = Frame(self.root)
        self.frame_encrypt.grid(ipadx=130, ipady=1, padx=(10, 10), pady=(10, 10))
        self.frame_encrypt.configure(background=os.getenv('blue_light'))

    def header(self):

        self.pic = ImageTk.PhotoImage(Image.open(os.getenv('logo_background_light')).resize((250, 250), Image.ANTIALIAS))
        self.pic2 = ImageTk.PhotoImage(Image.open(os.getenv('logo_background_dark')).resize((250, 250), Image.ANTIALIAS))
        self.panel = Label(self.frame_encrypt, image=self.pic, borderwidth=0)
        self.panel.image = self.pic
        self.panel.grid(padx=145, pady=5)
        # panel.pack(side="bottom", fill="both", expand="yes")

    def widgets(self):
        self.header()
        self.menu_top()
        self.switch()

        self.key_label = Label(self.frame_encrypt,
                               text=text_label_8,
                               font=(fonts['Helvetica'], 12, 'bold'),
                               bg=os.getenv('blue_light'),
                               fg=os.getenv('blue_1_light'))

        self.key_label.grid(pady=(0, 2))

        self.key_entry_var = IntVar()
        self.key_entry = Entry(self.frame_encrypt, width=30, textvariable=self.key_entry_var)
        self.key_entry.grid(pady=(0, 15))

        self.error_key = Label(self.frame_encrypt,
                               text='',
                               fg=os.getenv('blue_1_light'),
                               font=(fonts['Helvetica'], 12, 'bold'),
                               bg=os.getenv('blue_light'))
        self.error_key.grid()

        # ESCOLHER CAMINHO P/ ABRIR ==========================

        self.error_location = Label(self.frame_encrypt,
                                    text=text_label_2,
                                    fg=os.getenv('blue_1_light'),
                                    font=(fonts['Helvetica'], 12, 'bold'),
                                    bg=os.getenv('blue_light'))
        self.error_location.grid()

        self.choose_path_button = Button(self.frame_encrypt,
                                         width=os.getenv('small_size_button'),
                                         bg=os.getenv('blue_2_light'),
                                         fg=os.getenv('black'),
                                         text=text_button_0,
                                         command=self.open_file_path_to_choice)
        self.choose_path_button.grid(pady=(2, 10))
        # =====================================================
        # ESCOLHER CAMINHO P/ SALVAR ==========================
        '''
                LABEL - ERRO 2
        '''

        self.error_location_2 = Label(self.frame_encrypt,
                                      text=text_label_2,
                                      fg=os.getenv('blue_1_light'),
                                      font=(fonts['Helvetica'], 12, 'bold'),
                                      bg=os.getenv('blue_light'))
        self.error_location_2.grid()

        self.choose_path_button_2 = Button(self.frame_encrypt,
                                           width=os.getenv('small_size_button'),
                                           bg=os.getenv('blue_2_light'),
                                           fg=os.getenv('black'),
                                           text=text_button_2,
                                           command=self.open_file_path_to_save)
        self.choose_path_button_2.grid(pady=(2, 10))
        '''
                BUTTON - EnCRYPT
        '''
        self.encrypt_button = Button(self.frame_encrypt,
                                     text=text_button_1,
                                     width=10,
                                     bg=os.getenv('blue_2_light'),
                                     fg=os.getenv('black'),
                                     command=self.encrypt_file)
        self.encrypt_button.grid(pady=10)

        '''
                BUTTON - DECRYPT
        '''
        self.decrypt_button = Button(self.frame_encrypt,
                                     text=text_button_3,
                                     width=12,
                                     bg=os.getenv('blue_2_light'),
                                     fg=os.getenv('black'),
                                     command=self.decrypt_file)
        self.decrypt_button.grid(pady=10, padx=(4, 10))

        '''
        LABEL - Sucesso
        '''
        self.sucess_label = Label(self.frame_encrypt,
                                  text='',
                                  fg=os.getenv('green_light'),
                                  font=(fonts['Helvetica'], 12),
                                  bg=os.getenv('blue_light'))
        self.sucess_label.grid(pady=10)


if __name__ == '__main__':
    main = MainApplication()
    mainloop()
