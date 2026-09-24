import datetime
import calendar

d = datetime.date.today
month = calendar.month_abbr
print(datetime.date.today().strftime("%b %d %Y"))

#Expected output:
#$>python format_ft_time.py | cat -e
#Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
#Oct 21 2022$


#SOURCES
#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior