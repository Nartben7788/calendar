def dayOfWeekNumber(day, month, year):

    if (month == 1):
        month = 13
        year -=1
    if (month == 2):
        month = 14
        year -= 2

    q = day
    m = month
    k = year%100
    j = year//100
    h = (q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j)%7
    return h
    

def monthName(number):
    names ={
        0:'January',
        1:'February',
        2:'March',
        3:'April',
        4:'May',
        5:'June',
        6:'July',
        7:'August',
        8:'September',
        9:'October',
        10:'November',
        11:'December'
    }
    return names[number]

def numberOfDays(month, year):
    
    if month == 1:
        if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28
    elif month in  [0, 2, 4, 6, 7, 9, 11]:
        return 31
    else:
        return 30
    
def displayCalender(year):
   print(year, "--Calender")
   day_of_week_num = dayOfWeekNumber(1, 1, year)
   
   for i in range(12):
        print("\n---------------", monthName(i), "-----------------\n")
        print("Sun Mon Tue Wed Thu Fri Sat")
        num_of_days_in_month = numberOfDays(i, year)

        row_counter = 0

        for _ in range(day_of_week_num):
            print("    ", end="")
            row_counter+=1

        for k in range(num_of_days_in_month):
            print(f"{k:5d}", end="")

            row_counter+=1
            if row_counter > 6:
                row_counter = 0
                print()
        if row_counter:
            print()

        day_of_week_num = row_counter

displayCalender(2024)