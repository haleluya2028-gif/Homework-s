time = int ( input (" Enter the time of the day "))
def time_of_the_day (time):
    if time >=5 and time<= 11:
     print (" morning")
    elif time >= 12 and time <= 16 :
      print (" Afternoon")
    elif time >= 17 and time <= 20:
        print ( "evening")
    else :
      print (" Night")
time_of_the_day ( time)
