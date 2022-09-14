#prompt one:
hour = 0
min = 0
sec = 0

#get user input
hour = int(input("Enter the hours: "))
min = int(input("Enter the minutes: "))
sec = int(input("Enter the seconds: "))

#perform nessicary calculations

SECONDS_IN_HOUR = 120
SECONDS_IN_MINUTE = 60

sec_hour = hour * SECONDS_IN_HOUR
sec_min = min * SECONDS_IN_MINUTE
total_sec = sec + sec_hour + sec_min

#print the result
print("the result total of seconds is: ", total_sec)

#java version of this application available at: 
# https://github.com/tadpole63/javaL2JAVA_VERSION