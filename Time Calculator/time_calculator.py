def add_time(start, duration, starting_day=None):
    # start is in format #:## AM/PM
    start_time_splitted = start.split(" ")
    start_time = start_time_splitted[0]
    time_ending = start_time_splitted[1]
    start_time_splitted = start_time.split(":")
    start_hour = start_time_splitted[0]
    start_minutes = start_time_splitted[1]
    duration_splitted = duration.split(":")
    duration_hour = int(duration_splitted[0])
    duration_minutes = int(duration_splitted[1])
    new_hour = int(start_hour) + duration_hour
    new_minutes = int(start_minutes) + duration_minutes
    half_days = 0

    if new_minutes > 60:
        new_minutes -= 60
        new_hour += 1


    if new_hour >= 12:
        half_days = new_hour // 12
        new_hour -= 12 * half_days
        if half_days % 2 == 1 and time_ending == "AM":
            time_ending = "PM"
        elif half_days % 2 == 1 and time_ending == "PM":
            time_ending = "AM"
            half_days += 2

    if len(str(new_minutes)) == 1:
        new_minutes = "0" + str(new_minutes)
    else:
        new_minutes = str(new_minutes)

    if new_hour == 0:
        new_hour = 12

    new_hour = str(new_hour)

    if starting_day is not None:
        starting_day = starting_day.lower()
        starting_day = starting_day.capitalize()
        days = ["Monday", "Tuesday", "Wednesday", "Thurdays", "Friday", "Saturday", "Sunday"]
        day_index = days.index(starting_day)
        if half_days > 2 and half_days//2 != 1:
            day_index += half_days//2
            if day_index >= len(days):
                day_index = day_index % len(days)
            starting_day = days[day_index]
            new_time = new_hour + ":" + new_minutes + " " + time_ending + ", " + starting_day + " (%d days later)" % (half_days//2)
        elif half_days >= 1 and time_ending == "AM":
            starting_day = days[day_index+1]
            new_time = new_hour + ":" + new_minutes + " " + time_ending + ", " + starting_day + " (next day)"
        else:
            new_time = new_hour + ":" + new_minutes + " " + time_ending + ", " + starting_day
    else:
        if half_days > 2 and half_days//2 != 1:
            new_time = new_hour + ":" + new_minutes + " " + time_ending + " (%d days later)" % (half_days//2)
        elif half_days >= 1 and time_ending == "AM":
            new_time = new_hour + ":" + new_minutes + " " + time_ending + " (next day)"
        else:
            new_time = new_hour + ":" + new_minutes + " " + time_ending

    return new_time
