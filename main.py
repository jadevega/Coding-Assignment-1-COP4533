import random
import time
import statistics
import matplotlib.pyplot as plt
import sys
def gale_shapley(hospital_preferences, student_preferences):
#create a n x n table. sets up rank for students
    num = len(hospital_preferences)
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

    return hospital_match, num_proposals

def normal():
    num_of_hos_app = int(input().strip())

    basic_preferences = []  # includes all preferences (hospital + student)

    for i in range(2 * num_of_hos_app):
        preferences_list = input().split()
        if len(preferences_list) != num_of_hos_app:
            print("Invalid input")
            return
        valuefix = []
        for x in preferences_list:  # goes through the top 3 preferences
            intvalue = int(x)  # turns each number to an integer
            valuefix.append(intvalue - 1)  # fixes pref value so we can use them as indices later.

        basic_preferences.append(valuefix)

    hospital_preferences = basic_preferences[:num_of_hos_app]  # splits the preferences into first batch as hospital prefs
    student_preferences = basic_preferences[num_of_hos_app:]  # splits the preferences into second batch as student  prefs

    hospital_match, num_proposals = gale_shapley(hospital_preferences, student_preferences)

    for h in range(num_of_hos_app):
        print(h + 1, hospital_match[h] + 1)

    print("Number of proposals: ", num_proposals)


def randoms(n, ranges):
    students = list(range(n))
    hospitals = list(range(n))
    hospital_preferences = []

    for _ in range(n):
        stu = students[:]
        ranges.shuffle(stu)
        hospital_preferences.append(stu)

    student_preferences = []
    for _ in range(n):
        hos = hospitals[:]
        ranges.shuffle(hos)
        student_preferences.append(hos)

    return hospital_preferences, student_preferences

def findavg(func, repeats=5):
    times = []
    for _ in range(repeats):
        time0 = time.perf_counter()
        func()
        time1 = time.perf_counter()
        times.append(time1-time0)
    return statistics.mean(times)

def scale():
    values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    ranges = random.Random(0)

    times = []
    for val in values:
        hospitals, students = randoms(val, ranges)

        def run():
            gale_shapley(hospitals, students)

        avgtime = findavg(run, repeats=5)
        times.append(avgtime)

        print("n = ",val, "time =", avgtime)

    plt.plot(values, times,  color="pink")

    plt.xlabel("n (hospitals = students)")
    plt.ylabel("Run Time in seconds")
    plt.title("Scalability of Gale-Shapley Algorithm")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    if "--scalesetting" in sys.argv:
        scale()
    else:
        normal()