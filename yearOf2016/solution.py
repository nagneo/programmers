def solution(a, b):
    
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dates = (0 if a == 1 else sum(months[0:a-1])) + b - 1

    return days[dates % 7]

#print(solution(1,8))
#print(solution(5,24))