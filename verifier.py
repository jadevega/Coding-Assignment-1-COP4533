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

hospital_match = [-1] * num
student_match = [-1] * num

for i in range(num):
    pair = input().split()
    hospital = int(pair[0]) - 1
    student = int(pair[1]) - 1
    #check duplicates:
    if hospital_match[hospital] != -1:
        print("INVALID (Hospital matched more than once)")
        exit()
    if student_match[student] != -1:
        print("INVALID (Student matched more than once)")
        exit()

    hospital_match[hospital] = student
    student_match[student] = hospital

#check if there is an unmatched hospital or student
if -1 in hospital_match:
    print("INVALID (Unmatched hospital)")
    exit()
if -1 in student_match:
    print("INVALID (Unmatched student)")
    exit()

#create rank tables for hospitals and students
hospital_rank = [[0] * num for _ in range(num)]
student_rank = [[0] * num for _ in range(num)]

for hospital in range (num):
    for rank, student in enumerate(hospital_preferences[hospital]):
        hospital_rank[hospital][student] = rank

for student in range (num):
    for rank, hospital in enumerate(student_preferences[student]):
        student_rank[student][hospital] = rank

#check for blocked pairs
for hospital in range(num):
    student_matched = hospital_match[hospital]
    for student in hospital_preferences[hospital]:
        if student == student_matched:
            break
        current_match = student_match[student]

        if student_rank[student][hospital] < student_rank[student][current_match]:
            print("Unstable (", student + 1, ",", hospital + 1, ")")
            exit()

print("VALID STABLE")
