num_of_hos_app = int(input().strip())

basic_preferences = [] #includes all preferences (hospital + student)

for i in range(2 * num_of_hos_app):
    preferences_list = input().split()
    valuefix = []
    for num in preferences_list: #goes through the top 3 preferences
        intvalue = int(num) #turns each number to an integer
        valuefix.append(intvalue-1) #fixes pref value so we can use them as indices later.

    basic_preferences.append(valuefix)

hospital_preferences = basic_preferences[:num_of_hos_app] #splits the preferences into first batch as hospital prefs
student_preferences = basic_preferences[num_of_hos_app:] #splits the preferences into second batch as student  prefs

num = num_of_hos_app

#create a n x n table. sets up rank for students
student_rank = [[0] * num for _ in range(num)]
for stu in range (num):
    for rank, hospital in enumerate(student_preferences[stu]): #gives position in list and hospital num
        student_rank[stu][hospital] = rank #store rank


sec_choice= [0] * num #start with no proposal
stu_matched = [-1] * num #start with all free students
unmatched_hosp = list(range(num)) #num of free hospital

num_proposals = 0 #start with zero proposals

while unmatched_hosp:#while there are free hospitals
    hospital = unmatched_hosp.pop() #take first hospital of list

    if sec_choice[hospital] >= num:
        continue
    student = hospital_preferences[hospital][sec_choice[hospital]] #propose to the student it hasnt yet.
    sec_choice[hospital] +=1 # move to next student
    num_proposals = num_proposals+1 #increase num of poposals

    if stu_matched[student] == -1: #if unmatched accept
        stu_matched[student] = hospital #if student is free, accept the hospital

    else:
        current_match = stu_matched[student]

        if student_rank[student][hospital] < student_rank[student][current_match]:
            stu_matched[student]= hospital
            unmatched_hosp.append(current_match) #switch out match

        else:
            unmatched_hosp.append(hospital) #stay with match

#turn hospital centric
hospital_match = [-1] * num
#look at which hospital student is matched to and turn it to hospital match with student.
for student in range(num):
    hospital = stu_matched[student]
    hospital_match[hospital] = student

for hospital in range(num):
    print(hospital+1, hospital_match[hospital] + 1)

print("Number of proposals: ", num_proposals)