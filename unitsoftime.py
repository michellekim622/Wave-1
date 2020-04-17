day = input(print("please enter number of day"))
hour = input(print("please enter number of hour"))
min = input(print("please enter number of minute"))
sec = input(print("please enter number of second"))

day = int(day)
hour = int(hour)
min = int(min)
sec = int(sec)

total_sec = day*24*60*60 + hour*60*60 + min*60 + sec

print("Total duration is %i seconds", %total_sec)
