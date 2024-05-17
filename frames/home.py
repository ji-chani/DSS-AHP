import customtkinter as ctk

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

        welcome_text = """
Welcome to our AHP-based decision support system, tailored specifically for incoming 3rd year students pursuing BS Applied Mathematics and BS Mathematics at the University of the Philippines Los Baños. We recognize that choosing the right major elective courses is a crucial moment in shaping your academic journey and future career prospects. Thus, we have developed this platform to assist you in this important decision-making process.

Our system is meticulously crafted to offer  you guidance as you navigate through the range of AMAT/MATH major elective courses available in your curriculum. By leveraging AHP, we ensure that your choices are not only informed but also align with your individual preferences.

Through this platform, our aim is to equip you with a tool that enables you to rank the major elective courses based on factors such as self-preference, course availability, perceived difficulty, and the influence of peer pressure which are essential for crafting your plan of study (POS) effectively.

So, take the reins of your academic journey with confidence! Explore our decision support system, unlock a world of possibilities, and chart a course towards a fulfilling future in mathematics and applied mathematics.

Welcome aboard, and happy exploring!"""
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
