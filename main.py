num_of_hos_app = int(input().strip())

basic_preferences = []

for i in range(2 * num_of_hos_app):
    preferences_list = input().split()
    valuefix = []
    for num in preferences_list: #goes through the top 3 preferences
        intvalue = int(num) #turns each number to an integer
        valuefix.append(intvalue-1) #fixes pref value so we can use them as indices later.

    basic_preferences.append(valuefix)

hospital_preferences = basic_preferences[:num_of_hos_app] #splits the preferences into first batch as hospital prefs
student_preferences = basic_preferences[num_of_hos_app:] #splits the preferences into second batch as student  prefs

