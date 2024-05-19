# Consists of all instruction used in the frames

home_instructions = """Welcome to our AHP-based decision support system, tailored specifically for incoming 3rd year students pursuing BS Applied Mathematics and
BS Mathematics at the University of the Philippines Los Baños. We recognize that choosing the right major elective courses is a crucial moment 
in shaping your academic journey and future career prospects. Thus, we have developed this platform to assist you in this important 
decision-making process.

Our system is meticulously crafted to offer you guidance as you navigate through the range of AMAT/MATH major elective courses available in your 
curriculum. By leveraging AHP, we ensure that your choices are not only informed but also align with your individual preferences.

Through this platform, our aim is to equip you with a tool that enables you to rank the major elective courses based on factors such as self-preference, 
course availability, perceived difficulty, and the influence of peer pressure which are essential for crafting your plan of study (POS) effectively.

So, take the reins of your academic journey with confidence! Explore our decision support system, unlock a world of possibilities, and chart a course 
towards a fulfilling future in mathematics and applied mathematics.

Welcome aboard, and happy exploring!
"""

user_instructions = """On this page, please choose your degree program and 4th year academic option by following the steps below:

1. Select Your Degree Program:
        - Go to the "Degree Program" section.
        - Choose either "Bachelor of Science in Applied Mathematics" or "Bachelor of Science in Mathematics."
        - Choosing your degree program is important for the system to recommend the appropriate major electives for your program.

2. Choose Your 4th Year Academic Option:
        - Navigate to the "Option" section.
        - Select your 4th year option: either "Special Problem Option" or "Thesis Option."
        - Selecting your 4th year option is important for the system to determine how many units of major electives you will need to take.

3. Save Your Progress:
        - Once you have made your selections, click "Save" to save your progress.

        
Thank you!
"""

criteria_instruction = """Analytical Hierarchy Process (AHP) is a method for making decisions by 
breaking down a problem into a hierarchy of criteria and alternatives. 
In this page, the system will create a pairwise comparison matrix for 
the criteria, which requires user input.

Criteria for ranking major elective courses are as follows:
        (a) Course availability: Number of slots in SAIS. 
        (b) Perceived difficulty: User's expectation of course difficulty. 
        (c) Personal preferences: User's desire to take the course. 
        (d) Peer pressure: Influence of peer pressure in taking the course.

To create the pairwise comparison matrix, follow these steps:

1. Comparing Criteria:
        - Click the dropdown button in the "preferred" column to choose 
            your preferred criterion between the two being compared.
        - Ensure the transitivity property is satisfied: if A is preferred over B 
            and B is preferred over C, then A must be preferred over C.
        
            Example:
            Criteria: Availability, Difficulty, Peer Pressure

            Availability vs Difficulty 
            Preferred: Difficulty

            Availability vs Peer Pressure
            Preferred: Availability

            Difficulty vs Peer Pressure 
            Preferred: Difficulty

            Order of Preferred Criteria: Difficulty > Availability > Peer Pressure

2. Assigning Importance:
        - After selecting the preferred criterion, assign a value indicating 
            how much more important it is compared to the other criterion 
            using the Saaty Scale of Importance.

            Example: 
            Criteria: Availability vs Difficulty 
            Preferred: Difficulty 
            Value: 5 (This means that "Difficulty" is strongly important 
                    than "Availability")


3. Ensuring Consistency:
        - The values may not necessarily be different for each comparison, 
            but the overall comparison must have an acceptable level of 
            inconsistency, which will be shown in the Consistency Ratio 
            below the Comparing Criteria section.

4. Checking Consistency:
        - If the inconsistency is acceptable, click "Save" to proceed. 
        - If unacceptable, adjust the values until the inconsistency becomes 
            acceptable.

            
Thank you!
"""

preference_instruction= """In this section, you will be asked to rank the courses listed on the left 
side of your screen. Please rank the courses based on your preference
for taking them during your academic journey.

1. Rank the Courses:
        - Assign a ranking to each course subject based on your preference.
        - If you prefer multiple courses equally, you can give them the same 
            ranking.
        - The rank of the courses will determine the corresponding weights 
            of each course under the personal preference criterion.

2. Ranking Guidelines:
        - Ensure the number of rankings matches the number of courses 
            listed.
        - Duplicate rankings are allowed.
        - Refer to the course titles provided for clarity and guidance.

3. Course Titles:
        - BS AMAT Major Courses:
                > AMAT 115. Introduction to Mathematical Decision Theory
                > AMAT 160. Linear Programming 
                > AMAT 161. Nonlinear Programming 
                > AMAT 162. Integer and Dynamic Programming 
                > AMAT 163. Metaheuristics 
                > AMAT 167. Mathematical Models in Operations Research I 
                > AMAT 168. Mathematical Models in Operations Research II 
                > AMAT 171.  Life Insurance Mathematics I 
                > AMAT 172. Life Insurance Mathematics II 
                > AMAT 174. Measurement of Mortality 
                > AMAT 176. Actuarial Science 
                > AMAT 177. Introduction to Mathematical Finance
                > AMAT 178. Stochastic Calculus for Finance
                > AMAT 180. Introduction to Biomathematics 
                > AMAT 191. Special Topics
                > MATH 111. Modern Algebra I
                > MATH 115. Introduction to Coding Theory and Cryptography
                > MATH 141. Introduction to Combinatorics
                > MATH 143. Graph Theory
                > MATH 152. Partial Differential Equations
                > MATH 182. Stochastic Processes

        - BS MATH Major Courses:
                > MATH 112. Modern Algebra II 
                > MATH 115. Introduction to Coding Theory and Cryptography
                > MATH 143. Graph Theory 
                > MATH 152. Partial Differential Equations
                > MATH 156. Advance Calculus II 
                > MATH 160. Vector Analysis
                > MATH 166. Complex Analysis II 
                > MATH 170. Finite Differences 
                > MATH 174. Numerical Analysis I 
                > MATH 175 Numerical Analysis II 
                > MATH 182. Stochastic Processes
                > MATH 191. Special Topics

4. Review Your Rankings:
        - Double-check your rankings to ensure they reflect your 
            true preferences.

5. Solve Your Rankings:
        - Once you are satisfied with your rankings, click the "Solve" button 
            to submit your preferences.
        - Results will appear on your screen to present the system’s 
            decision on choosing the right courses based on your rankings.

            
Thank you!
"""