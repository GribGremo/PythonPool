import datetime
import time

# Return of seconds since epoch as a float
t = time.time()
print(
    f"Seconds since January 1, 1970: "
    f"{t:,.4f} or "  # "," Inserts a , every 3 digit, 4f 4 digits after decimal
    f"{t:.2e} in scientific notation")  # Exponent 1 digit, 
print(datetime.date.today().strftime("%b %d %Y"))

# Expected output:
# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09
# in scientific notation$
# Oct 21 2022$


# SOURCES
# Date
# https://docs.python.org/3/library/datetime.html#module-datetime

# Formatage date
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

# Formatage nombre
# https://docs.python.org/fr/3/library/string.html?utm_source=chatgpt.com#formatspec
