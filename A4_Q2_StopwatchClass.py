# Stopwatch class That starts the time and endstime when stopped and gives
#the time elpased.

from datetime import datetime, timedelta, time

class Stopwatch:

    def __int__(self, time=datetime.now()):
        self.__startTime = time
        self.__endTime = datetime.time()

    def start(self):
        self.__startTime = datetime.now()

    def stop(self):
        self.__endTime = datetime.now()

    def timeElapsed(self):
        time_elapsed = self.__endTime - self.__startTime
        return time_elapsed
        

#TestProgram to see if the stopWatch works

#starting the stopwatch

s1 = Stopwatch()
s1.start()
sum = 0
for i in range (1,1000000):
    sum += i
# Stopping the stopwatch
s1.stop()

#looking for time elapsed
elapsed = s1.timeElapsed()
print("Time elapsed = ",  elapsed.seconds," seconds  and " ,elapsed.microseconds, " microseconds")
