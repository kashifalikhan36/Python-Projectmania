import pandas
import math
data={row.names:[row.email,row.year,row.month,row.day] for index,row in pandas.read_csv("Day_32\\birthday-wisher\\birthdays.csv").iterrows()}
for name in data:

    print(int(data[name][1]))
    # year=math.floor(data[name][1])
    # month=math.floor(data[name][2])
    # day=math.floor(data[name][3])