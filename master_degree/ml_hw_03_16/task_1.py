hours = int(input())
minutes = int(input())

if not (0 <= hours <= 23 and 0 <= minutes <= 59):
    print("ошибка")
else:
    if hours < 12:
        period = 'AM'
        display_hours = hours if hours != 0 else 12
    else:
        period = 'PM'
        display_hours = hours - 12 if hours != 12 else 12

    print(f"{display_hours:02d}:{minutes:02d} {period}")
