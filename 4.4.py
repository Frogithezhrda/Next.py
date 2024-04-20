def gen_secs():
    for second in range(61):
        yield second


def gen_minutes():
    for minute in range(61):
        yield minute


def gen_hours():
    for hour in range(25):
        yield hour


def gen_years(start=2019):
    while True:
        yield start
        start += 1


def gen_months():
    for month in range(1, 14):
        yield month


def gen_days(month, leap_year=True):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        days_in_month = 31
    elif month in {4, 6, 9, 11}:
        days_in_month = 30
    elif month == 2 and leap_year:
        days_in_month = 29
    else:
        days_in_month = 28

    for day in range(1, days_in_month + 1):
        yield day
    day = 1
    yield day
def get_time():
    gen_hour = gen_hours()
    gen_minute = gen_minutes()
    gen_second = gen_secs()
    gen_year = gen_years()
    gen_month = gen_months()
    second = next(gen_second)
    year = next(gen_year)
    month = next(gen_month)
    gen_day = gen_days(month)
    day = next(gen_day)
    hours = next(gen_hour)
    minutes = next(gen_minute)

    while True:
        yield "%02d/%02d/%d %02d:%02d:%02d" % (day, month, year, hours, minutes, second)
        second = next(gen_second)
        if second > 59:
            gen_second = gen_secs()
            second = next(gen_second)
            minutes = next(gen_minute)
            if minutes > 59:
                gen_minute = gen_minutes()
                minutes = next(gen_minute)
                hours = next(gen_hour)
                if hours > 23:
                    gen_hour = gen_hours()
                    hours = next(gen_hour)
                    day = next(gen_day)
                    if day == 1:
                        month = next(gen_month)
                        gen_day = gen_days(month)
                        hours = next(gen_day)
                        if month > 12:
                            year = next(gen_year)


gen = get_time()
for i in range(1000000):
    print(next(gen))
