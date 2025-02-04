import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

speed_mean = numpy.mean(speed)
#print(speed_mean)

speed_median = numpy.median(speed) #It is important that the numbers are sorted before you can find the median.
#print (speed_median)

speed_mode = stats.mode(speed)
print(speed_mode)
