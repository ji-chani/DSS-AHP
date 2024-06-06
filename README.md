# Decision Support System for Selecting UPLB BS AMAT/MATH Major Courses using Analytic Hierarchy Process

## Authors
de Lemos R.F.Z., Dinglasan R.O., Jetomo C.B., Parba M.M.E., & Valderama D.E.S.

## Abstract
Before becoming a 3rd-year student, every student pursuing a degree in BS Applied Mathematics or BS Mathematics must submit their Plan of Study (POS). This process involves determining their specialization, opting for either a thesis or a special problem, selecting their thesis/SP adviser, choosing major and free electives, and scheduling when to take them. While an orientation covers these aspects, many students struggle in selecting their electives. Hence, this project aims to be an aid in selecting major courses that are based on the student’s preference, the courses’ perceived difficulty, availability of slots, and peer pressure. Specifically, this project aims to create a decision support system for students in selecting major courses. The development of the decision support system (DSS) was successfully implemented using the Analytic Hierarchy Process (AHP) framework. Upon inputting the necessary data into the system,  the DSS generates ranked courses based on all the criteria stated and provides a list of major courses, ordered according to their overall importance determined by the AHP process.

_**Keywords**: analytic hierarchy process (AHP), decision support system (DSS), plan of study (POS), major elective courses._

## Preliminaries and Theoretical Framework
In this problem, AHP assists students in systematically evaluating and ranking major courses according to various factors such as **personal preferences**, **perceived difficulty**, class **availability**, and the influence of **peer pressure**. By breaking down the decision-making process into hierarchical criteria, AHP enables students to make well-informed choices aligned with their individual goals and circumstances.

The following decision structure describes our project's goal. 
![image](https://github.com/ji-chani/DSS-AHP/assets/120572492/8de3d6c3-ff71-4eb0-a820-b3c931b2ac8d)

The users will be asked to select their degree program which will specify the courses that will be the alternatives. They will also be required to indicate their chosen specialization. As shown in the figure, the researchers will need some data to be able to conduct AHP including the course availability, students’ perceived difficulty toward major courses, personal preferences regarding the courses, and the effect of peer pressure on course selection.

The course availability will be obtained from the Student Academic Information System (SAIS), specifically the number of slots open for the last 3 semesters that each course was offered. The personal preferences of the user regarding the courses will be obtained by asking the user to rank some, if not all, courses from their option. The rank difference approach from [1] will be applied in this setup to construct the corresponding pairwise comparison matrix. The perceived difficulty and the effect of peer pressure, on the other hand, will be asked from 20-30 students of BS Applied Mathematics and BS Mathematics using Google Forms. Each of their responses will be recorded and the average for each course will be used in AHP. When the user is done inputting the data needed, the program will conduct AHP and will provide an output showing the ranked courses. The users can then use this ranking to help them in selecting major electives.

## Results and Discussion

### Data Description
The course availability was obtained by identifying the class capacity or the maximum number of slots for each course over the last three semesters it was offered. The data for perceived difficulty and influence of peer pressure, on the other hand, were both obtained from a survey with 10 respondents each from BS Applied Mathematics and BS Mathematics. The average of the class capacities, perceived difficulty, and influence of peer pressure were computed and their corresponding weights were obtained by normalizing the data. The data from the aforementioned criteria along with their weights are shown in Tables 1 and 2.

**Table 1:** Data obtained for course availability, perceived difficulty, and influence of peer pressure, and the corresponding weights of major elective courses for BS AMAT.
![image](https://github.com/ji-chani/DSS-AHP/assets/120572492/f0ebc87e-6989-4cc6-b0fc-76d5e8631405)

**Table 2:** Data obtained for course availability, perceived difficulty, and influence of peer pressure, and the corresponding weights of major elective courses for BS MATH.
![image](https://github.com/ji-chani/DSS-AHP/assets/120572492/0e06eaf2-381d-49d5-b494-e2323abcbbeb)

Lastly, since personal preferences are subjective and unique to each student, our AHP-based decision support system will ask users to provide this information. To obtain the data for personal preferences, the user will be required to rank the courses based on their preference. The rankings are not limited to one course per rank; the DSS allows the user to have multiple courses in one rank. To create the comparison matrix, pairwise rank differences between the courses are determined and the comparison value (which we denote by $a_k$ where $k$ is the absolute rank difference) is computed as follows:
$$a_0 = 1$$
$$a_k = a_{k-1}+ \frac{8}{num of alternatives} - 1$$
such that $a_n=9$ where $n$ is the maximum rank given to the courses. After this, we proceeded with getting the corresponding matrix containing the normalized vectors and obtaining the weights for personal preferences.

### AHP-based DSS
The graphical user interface (GUI) for the AHP-based DSS has five tabs: Home, User Details, Criteria, User Preference, and Results. The “Home” tab displays details about the DSS. The “User Details” tab includes instructions and relevance of selecting the degree program and academic option (Thesis or SP) and a dropdown selection of the said data. The “Criteria” tab includes instructions for the criteria comparison, the Saaty Scale of Importance, dropdown selection for pairwise comparison of preference of a criterion and level of importance over the other, consistency ratio of the comparison matrix of the criteria, and whether or not the inconsistency is acceptable. The “User Preference” tab asks the user to rank the courses according to the user’s preference, with instructions beside it. Lastly, the “Results” tab shows the weights and corresponding ranks for each course. It also displays the top 3 courses for the SP option or the top 2 courses for the Thesis option for BS Mathematics. For BS Applied Mathematics, this tab will display the top 5 courses for the SP option or the top 4 courses for the Thesis option.

A sample demo of using the GUI is shown below.

https://github.com/ji-chani/DSS-AHP/assets/120572492/158ea1fd-5e80-4bb0-9299-6147ecf9b70e








