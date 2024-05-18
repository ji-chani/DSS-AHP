import customtkinter as ctk
# text sizes
global normal, average, semi_header, header
normal, average, semi_header, header = 15, 18, 20, 25

class OutputFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # frame configuration, 2x2 grid placement
        self.create_complete_result_frame(master, **kwargs) # row 1, column 1
        self.create_final_result_frame(master, **kwargs)  # row 1, column 2
        self.create_back_save_frame(master, **kwargs)  # row 2, columnspan=2

    def create_complete_result_frame(self, master, **kwargs):

        # ------------ complete result frame
        self.complete_result_frame = ctk.CTkFrame(self, **kwargs)
        self.complete_result_frame.place(x=0, y=0, relwidth=0.60, relheight=0.9)

        self.complete_label = ctk.CTkLabel(self.complete_result_frame, text='Complete Results',
                                    font=ctk.CTkFont(size=semi_header, weight='bold'))
        self.complete_label.pack(padx=20, pady=(20,10), anchor='nw')

        # weighted courses
        self.weighted_courses_frame = ctk.CTkScrollableFrame(self.complete_result_frame)
        self.weighted_courses_frame.pack(padx=20, pady=(10,20), expand=True, fill='both')
        self.weighted_courses_frame.grid_columnconfigure((0,1,2), weight=1)

        # weighted courses header
        self.course_header = ctk.CTkLabel(self.weighted_courses_frame, text='Courses',
                                          font=ctk.CTkFont(size=average, weight='bold'))
        self.course_header.grid(row=0, column=0, padx=10, pady=(10,5), sticky='nsew')
        self.weight_header = ctk.CTkLabel(self.weighted_courses_frame, text='Weights',
                                          font=ctk.CTkFont(size=average, weight='bold'))
        self.weight_header.grid(row=0, column=1, padx=10, pady=(10,5), sticky='nsew')
        self.rank_header = ctk.CTkLabel(self.weighted_courses_frame, text='Rank',
                                        font=ctk.CTkFont(size=average, weight='bold'))
        self.rank_header.grid(row=0, column=2, padx=10, pady=(10,5), sticky='nsew')

        # fetch the complete list of courses, weights, and ranking
        self.complete_courses = None
    
    def create_final_result_frame(self, master, **kwargs):

        # final result frame
        self.final_result_frame = ctk.CTkFrame(self, **kwargs)
        self.final_result_frame.place(relx=0.60, rely=0, relwidth=0.4, relheight=0.7)

        # final result label
        self.final_label = ctk.CTkLabel(self.final_result_frame, text='Final Results',
                                        font=ctk.CTkFont(size=semi_header, weight='bold'))
        self.final_label.pack(padx=20, pady=(20,10), anchor='nw')

        # ranked courses frame
        self.ranked_course_frame = ctk.CTkFrame(self.final_result_frame)
        self.ranked_course_frame.pack(padx=20, pady=(10,10), expand=True, fill='both')
        self.ranked_course_frame.grid_columnconfigure((0,1), weight=1)

        # ranked courses frame headers
        self.ranked_course_rank_header = ctk.CTkLabel(self.ranked_course_frame, text='Rank',
                                                      font=ctk.CTkFont(size=average, weight='bold'))
        self.ranked_course_rank_header.grid(row=0, column=0, padx=20, pady=10, sticky='nsew')
        self.ranked_course_course_header = ctk.CTkLabel(self.ranked_course_frame, text='Course',
                                                        font=ctk.CTkFont(size=average, weight='bold'))
        self.ranked_course_course_header.grid(row=0, column=1, padx=20, pady=10, sticky='nsew')

        # change option label
        self.option_label = ctk.CTkLabel(self.final_result_frame, text='Option',
                                         font=ctk.CTkFont(size=average, weight='bold'))
        self.option_label.pack(padx=20, pady=(10,5), expand=True, anchor='nw')

        # change option menu
        self.option_menu = ctk.CTkOptionMenu(self.final_result_frame, values=['Special Problem', 'Thesis'],
                                             font=ctk.CTkFont(size=normal),
                                             variable=master.user_frame.option_var,
                                             command=master.solve_button_callback)
        self.option_menu.pack(padx=20, pady=(5,20), expand=True, anchor='n')


        self.top_ranks = None

    def create_back_save_frame(self, master, **kwargs):

        # back and solve (frame and buttons)
        self.output_back_save_frame = ctk.CTkFrame(self, **kwargs)
        self.output_back_save_frame.place(relx=0.25, rely=0.9, relwidth=0.5, relheight=0.1)
        self.output_back_save_frame.grid_columnconfigure((0,1), weight=1)
        self.output_back_save_frame.grid_rowconfigure(0, weight=1)

        # back button
        self.preference_back_button = ctk.CTkButton(self.output_back_save_frame, text='Back', anchor='center', bg_color='transparent',
                                              image=master.back_image, compound='left',
                                              font=ctk.CTkFont(size=semi_header, weight='bold'),
                                              command=master.preference_button_callback)
        self.preference_back_button.grid(row=0, column=0, padx=10, pady=(10,10), sticky='s')

        # solve button
        self.preference_save_button = ctk.CTkButton(self.output_back_save_frame, text='Home', anchor='center', bg_color='transparent',
                                              image=master.home_image_light, compound='left',
                                              font=ctk.CTkFont(size=semi_header, weight='bold'),
                                              command=master.home_button_callback)
        self.preference_save_button.grid(row=0, column=1, padx=10, pady=(10,10), sticky='s')
    
    def display_complete_ranks(self, master, subject_list:dict):

        if self.complete_courses is not None:
            for i in range(len(self.complete_courses)):
                self.complete_courses_labels[i].destroy()
            for i in range(len(self.complete_weights)):
                self.complete_weights_labels[i].destroy()
            for i in range(len(self.complete_ranking)):
                self.complete_ranking_labels[i].destroy()

        # create course labels in first column
        self.complete_courses = list(subject_list.keys())
        self.complete_courses_labels = []
        for i in range(len(self.complete_courses)):
            self.complete_courses_labels.append(ctk.CTkLabel(self.weighted_courses_frame, text=self.complete_courses[i],
                                                             font=ctk.CTkFont(size=normal)))
            self.complete_courses_labels[i].grid(row=i+1, column=0, padx=10, pady=5, sticky='nsew')
        
        # create course weights in second column
        self.complete_weights = [round(val, 4) for val in master.complete_weights]
        self.complete_weights_labels = []
        for i in range(len(self.complete_weights)):
            self.complete_weights_labels.append(ctk.CTkLabel(self.weighted_courses_frame, text=self.complete_weights[i],
                                                             font=ctk.CTkFont(size=normal)))
            self.complete_weights_labels[i].grid(row=i+1, column=1, padx=10, pady=5, sticky='nsew')

        # create course ranks in third column
        self.complete_ranking = [int(rank) for rank in master.complete_ranking]
        self.complete_ranking_labels = []
        for i in range(len(self.complete_ranking)):
            self.complete_ranking_labels.append(ctk.CTkLabel(self.weighted_courses_frame, text=self.complete_ranking[i],
                                                             font=ctk.CTkFont(size=normal)))
            self.complete_ranking_labels[i].grid(row=i+1, column=2, padx=10, pady=5, sticky='nsew')

    def display_final_ranks(self, master, num_top):

        if self.top_ranks is not None:
            for i in range(len(self.top_ranks)):
                self.top_ranks_labels[i].destroy()
            for i in range(len(self.top_courses)):
                self.top_courses_labels[i].destroy()


        # create rank numbers in first column
        self.top_ranks = list(range(1, num_top+1))
        self.top_ranks_labels = []
        for i in range(num_top):
            self.top_ranks_labels.append(ctk.CTkLabel(self.ranked_course_frame, text=str(self.top_ranks[i]),
                                                      font=ctk.CTkFont(size=average)))
            self.top_ranks_labels[i].grid(row=i+1, column=0, padx=20, pady=10, sticky='nsew')
        
        # list top courses in second column
        self.top_courses = []
        for rank in self.top_ranks:
            for i, r in enumerate(self.complete_ranking):
                if rank == r:
                    self.top_courses.append(self.complete_courses[i])
        self.top_courses_labels = []
        for i in range(num_top):
            self.top_courses_labels.append(ctk.CTkLabel(self.ranked_course_frame, text=str(self.top_courses[i]),
                                                      font=ctk.CTkFont(size=average), corner_radius=6,
                                                      fg_color= ["#3a7ebf", "#1f538d"], text_color=["#DCE4EE", "#DCE4EE"]))
            self.top_courses_labels[i].grid(row=i+1, column=1, padx=20, pady=10, sticky='nsew')