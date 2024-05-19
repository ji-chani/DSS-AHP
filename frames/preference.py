import customtkinter as ctk

from utils import preference_instruction, get_consistency_ratio, rank_difference

# text sizes
global normal, average, semi_header, header
normal, average, semi_header, header = 15, 18, 20, 25

class PreferenceFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # frame configuration, 2x2 grid placement
        self.create_instructions_frame(**kwargs)  # row 1, column 1
        self.create_rank_frame(master, **kwargs)  # row 1, column 2
        self.create_back_save_frame(master, **kwargs)  # row 2, columnspan=2


    def create_instructions_frame(self, **kwargs):
        # create instructions (frame, label, and textbox)
        self.instructions_frame = ctk.CTkFrame(self, **kwargs)
        self.instructions_frame.place(x=0, y=0, relwidth=0.5, relheight=0.9)

        self.instructions_label = ctk.CTkLabel(self.instructions_frame, text='Instructions: ',
                                                font=ctk.CTkFont(size=semi_header, weight="bold"))
        self.instructions_label.pack(padx=20, pady=(20,10), anchor='nw')

        instructions_text = preference_instruction
        self.instructions = ctk.CTkTextbox(self.instructions_frame,
                                         font=ctk.CTkFont(size=average))
        self.instructions.pack(padx=20, pady=(10,20), expand=True, fill='both', anchor='s')
        self.instructions.insert(index="0.0", text=instructions_text)
        self.instructions.configure(state="disabled")

    def create_rank_frame(self, master, **kwargs):
        # create rank frane and label
        self.rank_frame = ctk.CTkFrame(self, **kwargs)
        self.rank_frame.place(relx=0.5, y=0, relwidth=0.5, relheight=0.9)
        self.rank_label = ctk.CTkLabel(self.rank_frame, text='Ranking: ', 
                                       font=ctk.CTkFont(size=semi_header, weight="bold"))
        self.rank_label.pack(padx=20, pady=(20,10), anchor='nw')

        # frame for list of courses
        self.courses_frame = ctk.CTkScrollableFrame(self.rank_frame)
        self.courses_frame.pack(padx=20, pady=(10,20), fill='both', expand=True, anchor='n')
        self.courses_frame.grid_columnconfigure((0,1), weight=1)

        # list headers
        self.course_header = ctk.CTkLabel(self.courses_frame, text='Courses',
                                          font=ctk.CTkFont(size=semi_header, weight='bold'))
        self.course_header.grid(row=0, column=0, padx=20, pady=(10,5), sticky='w')
        self.rank_header = ctk.CTkLabel(self.courses_frame, text='Rank',
                                          font=ctk.CTkFont(size=semi_header, weight='bold'))
        self.rank_header.grid(row=0, column=1, padx=20, pady=(10,5), sticky='nsew')

        # courses placeholder
        self.courses = None
        
    def create_back_save_frame(self, master, **kwargs):

        # back and solve (frame and buttons)
        self.preference_back_save_frame = ctk.CTkFrame(self, **kwargs)
        self.preference_back_save_frame.place(relx=0.25, rely=0.9, relwidth=0.5, relheight=0.1)
        self.preference_back_save_frame.grid_columnconfigure((0,1), weight=1)
        self.preference_back_save_frame.grid_rowconfigure(0, weight=1)

        # back button
        self.preference_back_button = ctk.CTkButton(self.preference_back_save_frame, text='Back', anchor='center', bg_color='transparent',
                                              image=master.back_image, compound='left',
                                              font=ctk.CTkFont(size=semi_header, weight='bold'),
                                              command=master.criteria_button_callback)
        self.preference_back_button.grid(row=0, column=0, padx=10, pady=(10,10), sticky='s')

        # solve button
        self.preference_save_button = ctk.CTkButton(self.preference_back_save_frame, text='Solve', anchor='center', bg_color='transparent',
                                              image=master.save_image, compound='left',
                                              font=ctk.CTkFont(size=semi_header, weight='bold'),
                                              command=master.solve_button_callback)
        self.preference_save_button.grid(row=0, column=1, padx=10, pady=(10,10), sticky='s')
    
    def open_subject_list(self, subjects_dict:dict):
        
        if self.courses is not None:
            for i in range(len(self.courses_labels)):
                self.courses_labels[i].destroy()
            for i in range(len(self.course_rank_options)):
                self.course_rank_options[i].destroy()
        
        # create course labels in first column
        self.courses = list(subjects_dict.keys())
        self.courses_labels = []
        for i in range(len(self.courses)):
            self.courses_labels.append(ctk.CTkLabel(self.courses_frame, text=self.courses[i],
                                                   font=ctk.CTkFont(size=normal)))
            self.courses_labels[i].grid(row=i+1, column=0, padx=20, pady=(5,5), sticky='w')
        
        # create option menus in second column
        values = [str(i) for i in range(1, len(self.courses)+1)]
        self.course_rank_vars = [ctk.StringVar(self, value='1') for i in range(len(self.courses))]
        self.course_rank_options = []
        for i in range(len(self.courses)):
            self.course_rank_options.append(ctk.CTkOptionMenu(self.courses_frame, values=values,
                                                              command=self.update_ranking, variable=self.course_rank_vars[i]))
            self.course_rank_options[i].grid(row=i+1, column=1, padx=20, pady=(5,5), sticky='nsew')
        
        self.ranking_values = [int(self.course_rank_vars[i].get()) for i in range(len(self.course_rank_vars))]

    def update_ranking(self, value=None):
        # update ranking values 
        self.ranking_values = [int(self.course_rank_vars[i].get()) for i in range(len(self.course_rank_vars))]

        val, cons = get_consistency_ratio(rank_difference(self.ranking_values))
        print(f'Ranking updated. New ranking is {self.ranking_values}')
        print(f'with inconsistency value of {val} which is {cons}.')
