import customtkinter as ctk
from tkinter import ttk
from CTkTable import *
import numpy as np
from utils import get_consistency_ratio

# text sizes
global normal, average, semi_header, header
normal, average, semi_header, header = 15, 18, 20, 25


class CriteriaFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # 2x2 grid placement
        self.create_instructions_frame(**kwargs) # row 1, column 1
        self.create_comparison_frame(**kwargs) # row 1, column 1
        self.create_back_save_frame(master, **kwargs) # row 2, column 1 and 2

        # initialize pairwise matrix of criteria and update current inconsistencies
        self.pairwise_matrix = np.ones(shape=(4,4))
        self.update_matrix_from_option_menu()

    def create_instructions_frame(self, **kwargs):
        # create intructions frame
        self.instructions_frame = ctk.CTkFrame(self, **kwargs)
        self.instructions_frame.place(x=0, y=0, relwidth=0.5, relheight=0.9)

        # create instructions label
        self.instructions_label = ctk.CTkLabel(self.instructions_frame, text='Instructions',
                                              font=ctk.CTkFont(size=semi_header, weight="bold"))
        self.instructions_label.pack(padx=20, pady=(20,10), anchor='nw')

        # create instruction box
        instructions_text = "Insert instructions here ... \n\n " + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n \n" * 20
        self.instructions = ctk.CTkTextbox(self.instructions_frame, height=200,
                                         font=ctk.CTkFont(size=average))
        self.instructions.pack(padx=20, pady=(10,10), expand=True, fill='both', anchor='n')
        self.instructions.insert(index="0.0", text=instructions_text)
        self.instructions.configure(state="disabled")

        # create saaty table
        self.saaty_table_label = ctk.CTkLabel(self.instructions_frame, text='Saaty Scale of Importance',
                                              font=ctk.CTkFont(size=semi_header, weight="bold"))
        self.saaty_table_label.pack(padx=20, pady=(20,5), anchor='nw')
        saaty_scale = [['Value', 'Importance Level'],
                       [1, 'Equal'],
                       [2, 'Weak or Slight'],
                       [3, 'Moderate'],
                       [4, 'Moderate Plus'],
                       [5, 'Strong'],
                       [6, 'Strong Plus'],
                       [7, 'Very Strong'],
                       [8, 'Very, very Strong'],
                       [9, 'Extreme']]
        self.saaty_table = CTkTable(self.instructions_frame, row=10, column=2, 
                                    values=saaty_scale, font=ctk.CTkFont(size=average))
        self.saaty_table.pack(padx=20, pady=(5,20), expand=True, anchor='s')
        self.saaty_table.edit_row(row=0, font=ctk.CTkFont(size=average, weight='bold'), fg_color=("gray70", "gray30"))

    def create_comparison_frame(self, **kwargs):
        # create comparison frame
        self.comparison_frame = ctk.CTkFrame(self, **kwargs)
        self.comparison_frame.place(relx=0.5, y=0, relwidth=0.5, relheight=0.9)

        # create comparison label
        self.comparison_label = ctk.CTkLabel(self.comparison_frame, text='Comparing Criteria',
                                              font=ctk.CTkFont(size=semi_header, weight="bold"))
        self.comparison_label.pack(padx=20, pady=(20,10), anchor='nw')

        # create comparisons table
        self.comparison_table_frame = ctk.CTkFrame(self.comparison_frame, corner_radius=10, height=400,
                                                   fg_color=('gray100', 'gray20'))
        self.comparison_table_frame.pack(padx=20, pady=(5,10), expand=True, fill='both', anchor='n')

        # table headers
        self.header_frame = ctk.CTkFrame(self.comparison_table_frame, fg_color='transparent')
        self.header_frame.place(x=0, y=0, relwidth=1, relheight=0.1)

        header_kwargs = dict(fg_color='transparent', font=ctk.CTkFont(size=average, weight='bold'))
        self.header1 = ctk.CTkLabel(self.header_frame, text='Criteria', **header_kwargs)
        self.header1.place(relx=0, rely=0, relwidth=1/3, relheight=1)
        self.header2 = ctk.CTkLabel(self.header_frame, text='Preferred', **header_kwargs)
        self.header2.place(relx=1/3, rely=0, relwidth=1/3, relheight=1)
        self.header3 = ctk.CTkLabel(self.header_frame, text='Value', **header_kwargs)
        self.header3.place(relx=2/3, rely=0, relwidth=1/3, relheight=1)
        
        # criteria column
        self.criteria_column_frame = ctk.CTkFrame(self.comparison_table_frame, **kwargs)
        self.criteria_column_frame.place(relx=0, rely=0.1, relwidth=1/3, relheight=0.9)

        criteria_kwargs = dict(fg_color='transparent', font=ctk.CTkFont(size=normal))
        self.row1 = ctk.CTkLabel(self.criteria_column_frame, text='Availability vs \n Difficulty', **criteria_kwargs)
        self.row1.place(relx=0, rely=0, relwidth=1, relheight=0.18)
        self.row2 = ctk.CTkLabel(self.criteria_column_frame, text='Availability vs \n Peer Pressure', **criteria_kwargs)
        self.row2.place(relx=0, rely=0.15, relwidth=1, relheight=0.18)
        self.row3 = ctk.CTkLabel(self.criteria_column_frame, text='Availability vs \n Preference', **criteria_kwargs)
        self.row3.place(relx=0, rely=0.30, relwidth=1, relheight=0.18)
        self.row4 = ctk.CTkLabel(self.criteria_column_frame, text='Difficulty vs \n Peer Pressure', **criteria_kwargs)
        self.row4.place(relx=0, rely=0.45, relwidth=1, relheight=0.18)
        self.row5 = ctk.CTkLabel(self.criteria_column_frame, text='Difficulty vs \n Preference', **criteria_kwargs)
        self.row5.place(relx=0, rely=0.60, relwidth=1, relheight=0.18)
        self.row6 = ctk.CTkLabel(self.criteria_column_frame, text='Peer Pressure vs \n Preference', **criteria_kwargs)
        self.row6.place(relx=0, rely=0.75, relwidth=1, relheight=0.18)

        # preferred column
        self.preferred_column_frame = ctk.CTkFrame(self.comparison_table_frame, **kwargs)
        self.preferred_column_frame.place(relx=1/3, rely=0.1, relwidth=1/3, relheight=0.9)
        self.preferred_column_frame.grid_columnconfigure(0, weight=1)

        comparison_table_values = np.array([['Availability', 'Difficulty'],
                                   ['Availability', 'Peer Pressure'],
                                   ['Availability', 'Preference'],
                                   ['Difficulty', 'Peer Pressure'],
                                   ['Difficulty', 'Preference'],
                                   ['Peer Pressure', 'Preference']])
        self.criteria_list = np.unique(comparison_table_values)
        self.comparison_values_indices = np.array([np.where(self.criteria_list == crit) for crit in comparison_table_values.flatten()]).reshape(*comparison_table_values.shape)
        
        # option variables
        self.option1_var, self.option2_var, self.option3_var = ctk.StringVar(value='Availability'), ctk.StringVar(value='Availability'), ctk.StringVar(value='Availability')
        self.option4_var, self.option5_var, self.option6_var = ctk.StringVar(value='Difficulty'), ctk.StringVar(value='Difficulty'), ctk.StringVar(value='Peer Pressure')
        
        # option menus
        self.option1 = ctk.CTkOptionMenu(self.preferred_column_frame, values=comparison_table_values[0], 
                                         command=self.update_matrix_from_option_menu, variable=self.option1_var)
        self.option1.place(relx=0, rely=0.05, relwidth=1, relheight=0.075)
        self.option2 = ctk.CTkOptionMenu(self.preferred_column_frame, values=comparison_table_values[1],
                                         command=self.update_matrix_from_option_menu, variable=self.option2_var)
        self.option2.place(relx=0, rely=0.20, relwidth=1, relheight=0.075)
        self.option3 = ctk.CTkOptionMenu(self.preferred_column_frame, values=comparison_table_values[2], 
                                         command=self.update_matrix_from_option_menu, variable=self.option3_var)
        self.option3.place(relx=0, rely=0.35, relwidth=1, relheight=0.075)
        self.option4 = ctk.CTkOptionMenu(self.preferred_column_frame, values=comparison_table_values[3], 
                                         command=self.update_matrix_from_option_menu, variable=self.option4_var)
        self.option4.place(relx=0, rely=0.50, relwidth=1, relheight=0.075)
        self.option5 = ctk.CTkOptionMenu(self.preferred_column_frame, values=comparison_table_values[4], 
                                         command=self.update_matrix_from_option_menu, variable=self.option5_var)
        self.option5.place(relx=0, rely=0.65, relwidth=1, relheight=0.075)
        self.option6 = ctk.CTkOptionMenu(self.preferred_column_frame, values=comparison_table_values[5], 
                                         command=self.update_matrix_from_option_menu, variable=self.option6_var)
        self.option6.place(relx=0, rely=0.80, relwidth=1, relheight=0.075)

        # value column
        self.value_column_frame = ctk.CTkFrame(self.comparison_table_frame, **kwargs)
        self.value_column_frame.place(relx=2/3, rely=0.1, relwidth=1/3, relheight=0.9)

        # value variables
        values = [str(i) for i in range(1,10)]
        self.val1, self.val2, self.val3 = ctk.StringVar(value='1'), ctk.StringVar(value='1'), ctk.StringVar(value='1')
        self.val4, self.val5, self.val6 = ctk.StringVar(value='1'), ctk.StringVar(value='1'), ctk.StringVar(value='1')
        self.entry1 = ctk.CTkOptionMenu(self.value_column_frame, values=values,
                                        command=self.update_matrix_from_option_menu, variable=self.val1)
        self.entry1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.075)
        self.entry2 = ctk.CTkOptionMenu(self.value_column_frame, values=values,
                                        command=self.update_matrix_from_option_menu, variable=self.val2)
        self.entry2.place(relx=0.1, rely=0.20, relwidth=0.8, relheight=0.075)
        self.entry3 = ctk.CTkOptionMenu(self.value_column_frame, values=values,
                                        command=self.update_matrix_from_option_menu, variable=self.val3)
        self.entry3.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.075)
        self.entry4 = ctk.CTkOptionMenu(self.value_column_frame, values=values,
                                        command=self.update_matrix_from_option_menu, variable=self.val4)
        self.entry4.place(relx=0.1, rely=0.50, relwidth=0.8, relheight=0.075)
        self.entry5 = ctk.CTkOptionMenu(self.value_column_frame, values=values,
                                        command=self.update_matrix_from_option_menu, variable=self.val5)
        self.entry5.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.075)
        self.entry6 = ctk.CTkOptionMenu(self.value_column_frame, values=values,
                                        command=self.update_matrix_from_option_menu, variable=self.val6)
        self.entry6.place(relx=0.1, rely=0.80, relwidth=0.8, relheight=0.075)


        # create inconsistency label
        self.inconsistency_label = ctk.CTkLabel(self.comparison_frame, text='Consistency Ratio',
                                                font=ctk.CTkFont(size=semi_header, weight='bold'))
        self.inconsistency_label.pack(padx=20, pady=(0,10), expand=True, anchor='nw')

        # create inconsistency frame
        self.inconsistency_frame = ctk.CTkFrame(self.comparison_frame)
        self.inconsistency_frame.pack(padx=20, pady=(0,20), expand=True, fill='both', anchor='n')
        
        # create inconsistency value
        self.consistency_ratio = ctk.StringVar(self)
        self.inconsistency = ctk.StringVar(self)
        self.inconsistency_value_label = ctk.CTkLabel(self.inconsistency_frame, text='Value: ',
                                                      font=ctk.CTkFont(size=average, weight='bold'))
        self.inconsistency_value_label.place(relx=0, rely=0, relwidth=0.4, relheight=0.5)
        self.inconsistency_value = ctk.CTkLabel(self.inconsistency_frame, textvariable=self.consistency_ratio,
                                                font=ctk.CTkFont(size=average, weight='bold'), fg_color=["#3a7ebf", "#1f538d"])
        self.inconsistency_value.place(relx=0.4, rely=0, relwidth=0.6, relheight=0.5)

        self.inconsistency_accept_label = ctk.CTkLabel(self.inconsistency_frame, text='Inconsistency: ',
                                                      font=ctk.CTkFont(size=average, weight='bold'))
        self.inconsistency_accept_label.place(relx=0, rely=0.5, relwidth=0.4, relheight=0.5)
        self.inconsistency_accept = ctk.CTkLabel(self.inconsistency_frame, textvariable=self.inconsistency,
                                                 font=ctk.CTkFont(size=average, weight='bold'), fg_color=["#3a7ebf", "#1f538d"])
        self.inconsistency_accept.place(relx=0.4, rely=0.5, relwidth=0.6, relheight=0.5)

    def create_back_save_frame(self, master, **kwargs):
        # create back and save button frame
        self.criteria_back_save_frame = ctk.CTkFrame(self, **kwargs)
        self.criteria_back_save_frame.place(relx=0.25, rely=0.9, relwidth=0.5, relheight=0.1)
        self.criteria_back_save_frame.grid_columnconfigure((0,1), weight=1)
        self.criteria_back_save_frame.grid_rowconfigure(0, weight=1)

        # create back button
        self.criteria_back_button = ctk.CTkButton(self.criteria_back_save_frame, text='Back', anchor='center', bg_color='transparent',
                                              image=master.back_image, compound='left',
                                              font=ctk.CTkFont(size=semi_header, weight='bold'),
                                              command=master.user_button_callback)
        self.criteria_back_button.grid(row=0, column=0, padx=10, pady=(10,10), sticky='s')
        
        # create save button
        self.criteria_save_button = ctk.CTkButton(self.criteria_back_save_frame, text='Save', anchor='center', bg_color='transparent',
                                              image=master.save_image, compound='left',
                                              font=ctk.CTkFont(size=semi_header, weight='bold'),
                                              command=master.preference_button_callback)
        self.criteria_save_button.grid(row=0, column=1, padx=10, pady=(10,10), sticky='s')

    def update_matrix_from_option_menu(self, value=None):
        # list of preferred options
        self.option_variables = [str(option) for option in [self.option1_var.get(), self.option2_var.get(), self.option3_var.get(),
                                                            self.option4_var.get(), self.option5_var.get(), self.option6_var.get()]]
        self.selected_option_indices = [np.where(self.criteria_list == option)[0][0] for option in self.option_variables]

        # list of non preferred options
        self.nonselected_option_indices = [self.comparison_values_indices[idx][np.where(self.comparison_values_indices[idx] != self.selected_option_indices[idx])[0][0]]
                                           for idx in range(len(self.selected_option_indices))]
        
        # matrix indices with integer (direct), and corresponding (inverse) values
        self.direct = [[self.selected_option_indices[idx], self.nonselected_option_indices[idx]] for idx in range(len(self.selected_option_indices))]
        self.inverse =  [[self.nonselected_option_indices[idx], self.selected_option_indices[idx]] for idx in range(len(self.selected_option_indices))]
        
        # list of values
        self.value_variables = [int(str(value)) for value in [self.val1.get(), self.val2.get(), self.val3.get(),
                                                              self.val4.get(), self.val5.get(), self.val6.get()]]
        
        # update matrix
        self.update_matrix()
        # print(self.pairwise_matrix)

        # update inconsistency
        self.update_inconsistency()
        # print(self.consistency_ratio.get())
        # print(self.inconsistency.get())

    def update_matrix(self):
        # direct
        for idx in range(len(self.direct)):
            r, c = self.direct[idx][0], self.direct[idx][1]
            self.pairwise_matrix[r, c] = self.value_variables[idx]
        # inverse
        for idx in range(len(self.inverse)):
            r, c = self.inverse[idx][0], self.inverse[idx][1]
            self.pairwise_matrix[r, c] = 1/self.value_variables[idx]

    def update_inconsistency(self):
        consistency_ratio, inconsistency = get_consistency_ratio(self.pairwise_matrix)
        # update stringVars
        self.consistency_ratio.set(value=f'{consistency_ratio:.5f}')
        self.inconsistency.set(value=f'{inconsistency}')

class InvalidInconsistency(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # label and button
        label_kwargs = dict(font=ctk.CTkFont(size=average, weight='bold'))
        self.label1 = ctk.CTkLabel(self,
                                  text='Inconsistency is not acceptable.', **label_kwargs)
        self.label1.pack(padx=20, pady=(20,5))
        self.label2 = ctk.CTkLabel(self,
                                  text='Try modifying your criteria preference.', **label_kwargs)
        self.label2.pack(padx=20, pady=(5,20))

        # back button
        self.button = ctk.CTkButton(self, text='Return', font=ctk.CTkFont(size=semi_header, weight='bold'),
                                    image=master.back_image, compound='left',
                                    command=master.criteria_button_callback)
        self.button.pack(padx=20, pady=20)
