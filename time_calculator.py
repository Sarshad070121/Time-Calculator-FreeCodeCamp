def add_time(start, dur, day=None):
    
    week_map = {
        "Saturday": 0,
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6}
    
    Time, md = start.split()
    hrs, min = Time.split(':')
    hrs = int(hrs)
    min = int(min)
    
    if md == "PM":
        hrs += 12

    dur_hrs, dur_min = dur.split(':')
    dur_hrs = int(dur_hrs)
    dur_min = int(dur_min)

    
    tmin = min + dur_min
    min_ans = tmin % 60
    exhrs = tmin // 60
    total_hour = hrs + dur_hrs + exhrs

    
    ans_hour = (total_hour % 24) % 12

    total_day = (total_hour // 24)

    if ans_hour == 0:
        ans_hour = 12
    ans_hour = str(ans_hour)

    
    midday_answer = ""
    if (total_hour % 24) <= 11:
        midday_answer = "AM"
    else:
        midday_answer = "PM"

   
    if min_ans <= 9:
        min_ans = '0' + str(min_ans)
    else:
        min_ans = str(min_ans)
   
    time_stamp = ans_hour + ":" + min_ans + ' ' + midday_answer
    if day == None:
        if total_day == 0:
            return time_stamp
        if total_day == 1:
            return time_stamp + ' (next day)'
        return time_stamp + ' (' + str(total_day) + ' days later)'
    else:
        ans_day = (week_map[day.lower().capitalize()] + total_day) % 7
        for i, j in week_map.items():
            if j == ans_day:
                ans_day = i
                break
        if total_day == 0:
            return time_stamp + ', ' + ans_day
        if total_day == 1:
            return time_stamp + ', ' + ans_day + ' (next day)'
        return time_stamp + ', ' + ans_day + ' (' + str(
            total_day) + ' days later)'
