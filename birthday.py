import datetime

age = input("How old are you?:")
num = int(age)
def age_to_time(num):
    month = num * 12
    day = num * 356
    hour = day * 24
    minute = hour * 60
    print("Months:" + " " + str(month))
    print("Day:" + " " + str(day))
    print("Hours:" + " " + str(hour))
    print("Minute:" + " " + str(minute))


age_to_time(num)