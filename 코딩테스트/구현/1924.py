a, b = map(int,input().split())
lst = [0,0,31,28,31,30,31,30,31,31,30,31,30]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
print(days[(sum(lst[:a])+b)%7])
