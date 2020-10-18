import calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
# year: 2022, column width: 2, lines per week: 1 
# number of spaces between month columns: 1
# 3: no. of months per column.
print(cal.formatyear(2022, 2, 1, 1, 3))
