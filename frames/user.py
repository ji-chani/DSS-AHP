import customtkinter as ctk


# text sizes
global normal, average, semi_header, header
normal, average, semi_header, header = 15, 18, 20, 25

class UserFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # frame configuration

        # create instructions
        self.instructions_frame = ctk.CTkFrame(self, **kwargs)
        self.instructions_frame.place(relx=0, rely=0, relwidth=1, relheight=0.6)
        
        # create instructions label
        self.instructions_label = ctk.CTkLabel(self.instructions_frame, text='Instructions',
                                              font=ctk.CTkFont(size=semi_header, weight="bold"))
        self.instructions_label.pack(padx=20, pady=(20,10), anchor='nw')

        # create instruction box
        instructions_text = "Insert instructions here ... \n\n " + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n \n" * 20
        self.instructions = ctk.CTkTextbox(self.instructions_frame,
                                         font=ctk.CTkFont(size=average))
        self.instructions.pack(padx=20, pady=(10,10), expand=True, fill='both', anchor='n')
        self.instructions.insert(index="0.0", text=instructions_text)
        self.instructions.configure(state="disabled")
        
        # create options frame
        self.options_frame = ctk.CTkFrame(self, **kwargs)
        self.options_frame.place(relx=0, rely=0.6, relwidth=1, relheight=0.3)

        # degree program option menu
        self.deg_prog_var = ctk.StringVar(value="BS AMAT")
        self.deg_prog_label = ctk.CTkLabel(self.options_frame, text="Degree Program", anchor='center',
                                           font=ctk.CTkFont(size=average, weight='bold'))
        self.deg_prog_label.pack(padx=20, pady=(10,5), expand=True, fill='both', anchor='nw')
        self.deg_prog = ctk.CTkOptionMenu(self.options_frame, corner_radius=6, width=200, anchor='center',
                                          values=["BS AMAT", "BS MATH"], variable=self.deg_prog_var,
                                          command=self.changed_deg_prog, font=ctk.CTkFont(size=normal))
        self.deg_prog.pack(padx=20, pady=(5,10), expand=True, fill='y', anchor='n')

        # SP/thesis option menu
        self.option_var = ctk.StringVar(value='Special Problem')
        self.option_label = ctk.CTkLabel(self.options_frame, text="Option", anchor='center',
                                           font=ctk.CTkFont(size=average, weight='bold'))
        self.option_label.pack(padx=20, pady=(10,5), expand=True, fill='both', anchor='nw')
        self.option = ctk.CTkOptionMenu(self.options_frame, corner_radius=6, width=200, anchor='center',
                                        values=['Special Problem', 'Thesis'], variable=self.option_var,
                                        command=self.changed_option, font=ctk.CTkFont(size=normal))
        self.option.pack(padx=20, pady=(5,20), expand=True, fill='y', anchor='s')

        # back and save frame
        self.user_back_save_frame = ctk.CTkFrame(self, **kwargs)
        self.user_back_save_frame.place(relx=0.25, rely=0.9, relwidth=0.5, relheight=0.1)
        self.user_back_save_frame.grid_columnconfigure((0,1), weight=1)
        self.user_back_save_frame.grid_rowconfigure(0, weight=1)

        # back button
        self.user_back_button = ctk.CTkButton(self.user_back_save_frame, text='Back', anchor='center', bg_color='transparent',
                                              image=master.back_image, compound='left',
                                              font=ctk.CTkFont(size=semi_header, weight='bold'),
                                              command=master.home_button_callback)
        self.user_back_button.grid(row=0, column=0, padx=10, pady=(10,10), sticky='s')

        # save button
        self.user_save_button = ctk.CTkButton(self.user_back_save_frame, text='Save', anchor='center', bg_color='transparent',
                                              image=master.save_image, compound='left',
                                              font=ctk.CTkFont(size=semi_header, weight='bold'),
                                              command=master.criteria_button_callback)
        self.user_save_button.grid(row=0, column=1, padx=10, pady=(10,10), sticky='s')

    def changed_deg_prog(self, value=None):
        print(f'Degree Program changed to {self.deg_prog_var.get()}.')

    def changed_option(self, value=None):
        print(f'Option changed to {self.option_var.get()}.')

