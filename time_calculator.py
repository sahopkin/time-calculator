def add_time(start, duration, day = None):

  start_len = len(start)
  duration_len = len(duration)

  #pulls out AM or PM for start time
  am_pm = start[-2:]
  start_hour = int(start[0:-6])# if start_len < 8 else int(start[0:2])
  start_min = int(start[-5:-3])

  dur_hour = int(duration[0:-3])
  dur_min = int(duration[-2:])

  #convert start hour to 24-hour time
  if start_hour == 12 and am_pm == "AM":
    start_hour = 0
  elif start_hour != 12 and am_pm == "PM":
    start_hour += 12

  #print(start_hour, start_min)

  #convert duration to minutes
  dur_as_mins = (dur_hour * 60) + dur_min
  total_mins = dur_as_mins + start_min
  #determine number of hours and minutes to add to start_time
  add_hours = total_mins // 60
  new_hour = start_hour + add_hours
  new_min = str(round(((total_mins / 60) - add_hours) * 60))
  #adds leading 0 if new_min is only 1 digit in length
  if len(new_min) == 1:
    new_min = f'0{new_min}'
  #print(new_hour, new_min)

  #adjust to proper AM/PM designation.  Floor division of AM hours (0-11) is always an even number; (12-23) is always an odd number.  Taking the modulo of that result provides the index to pull the proper designation from the list a_p.
  a_p = ["AM", "PM"]
  new_am_pm = a_p[((new_hour // 12) % 2)]

  #convert hour back to 12-hour time
  stand_hour = new_hour % 12
  new_stand_hour = str(12) if stand_hour == 0 else str(stand_hour)

  #determine number of days later
  day_count = new_hour // 24
  if day_count > 1:
    statement = f" ({day_count} days later)"
  elif day_count == 1:
    statement = " (next day)"
  else:
    statement = ""
  
  #include new day of the week if day is included as a parameter
  if day != None:
    day = day.lower().title()
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    days_len = len(days)
    day_index = days.index(day)
    new_day = days[(day_index + day_count) % days_len]
    return f'{new_stand_hour}:{new_min} {new_am_pm}, {new_day}{statement}'
  else:
    return f'{new_stand_hour}:{new_min} {new_am_pm}{statement}'
