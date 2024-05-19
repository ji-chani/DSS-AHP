import customtkinter as ctk
from utils import home_instructions


# text sizes
global normal, average, semi_header, header
normal, average, semi_header, header = 15, 18, 20, 25

class HomeFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # frame configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # create instructions
        self.welcome_label = ctk.CTkLabel(self, text='Hello Iskolar!', font=ctk.CTkFont(size=semi_header, weight="bold"))
        self.welcome_label.grid(row=0, column=0, padx=20, pady=(20,10), sticky="w")

        welcome_text = home_instructions
        self.welcome_text = ctk.CTkTextbox(self, width=250, height=500, 
                                           font=ctk.CTkFont(size=normal+3))
        self.welcome_text.grid(row=1, column=0, padx=20, pady=(0,20), sticky='new')
        self.welcome_text.insert(index="0.0", text=welcome_text)
        self.welcome_text.configure(state="disabled")

        # continue button
        self.home_continue_button = ctk.CTkButton(self, text='Continue', anchor='w', bg_color='transparent',
                                              image=master.next_image, compound='left',
                                              font=ctk.CTkFont(size=semi_header, weight='bold'),
                                              command=master.user_button_callback)
        self.home_continue_button.grid(row=3, column=0, pady=20, sticky='s')