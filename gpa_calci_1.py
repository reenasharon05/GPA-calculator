name=str(input("Enter student name: "))
register_no=int(input("Enter the register number: "))
num_sub=int(input("Enter the number of subjects of the semester: "))
tot = 0
tot_cred = 0
#Get the elements from the user
for i in range(num_sub):
    num = float(input(f"Enter marks{i+1}: "))
    cred= int(input("Enter the credit of the subject: ")) 
    # to find the grade points
    if num>90:
        print("GRADE: O")
        g_pts=10 # assigning grade point based on grade
    elif num>80:
        print("GRADE: A+")
        g_pts=9
    elif num>70:
        print("GRADE: A")
        g_pts=8
    elif num>60:
        print("GRADE: B+")
        g_pts=7
    elif num>50:
        print("GRADE: B")
        g_pts=6
    else:
        print("RESULT: FAIL")
        break
    sub_score = cred*g_pts  #per subject score
    tot+=sub_score
    tot_cred+=cred#total number of credits
print(tot_cred)
gpa = tot/tot_cred
#display the data
print(f"Name:{name}")
print(f"Register number:{register_no}")
print("Total credits:",tot_cred)
print("GPA:",gpa)    