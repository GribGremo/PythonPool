import datetime
import time

print(f"Seconds since January 1, 1970: {time.time():,.4f} or {time.time():.2e} in scientific notation")
print(datetime.date.today().strftime("%b %d %Y"))
#Expected output:
#$>python format_ft_time.py | cat -e
#Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
#Oct 21 2022$


#SOURCES
#Formatage date
#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

#Formatage nombre
#https://docs.python.org/fr/3/library/string.html?utm_source=chatgpt.com#formatspec