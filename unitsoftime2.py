sec = input(print("please enter number of seconds"))

# second int
sec = int(sec)

# day used
day = sec//(24*60*60)
sec = sec%(24*60*60)

# hour used
hour = sec//(60*60)
sec = sec%(60*60)

# min used
min = sec//60
sec = sec % 60

# amount of time in the form D:HH:MM:SS
print("%i:%02i:%02i:%02i" %(day ,hour, min, sec))
