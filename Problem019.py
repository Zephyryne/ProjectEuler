#Calculate the number of days in the range
#364 days in 52 weeks, so the first day of 1901 is a Tuesday -> Sunday = day%7==5
days = 0
sundays = 0
for i in range(1901,2001):
  for m in ["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]:
    if m in ["jan","mar","may","jul","aug","oct","dec"]:
      days+=31
    elif m in ["apr","jun","sept","nov"]:
      days+=30
    elif m=="feb":
      if i%400==0 or (i%4==0 and i%100!=0):
        days+=29
      else:
        days+=28
    if days%7==5:
      sundays+=1
print(sundays)