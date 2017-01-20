import datetime
years = []
for x in range(106, 2006, 10):
    my_date = datetime.date(x, 1, 26)
    if my_date.weekday() == 0:
        years.append(my_date.year)
print(years)
