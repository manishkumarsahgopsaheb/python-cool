# import numpy
# from scipy import stats
# # finding of mean median and mode
# speed = [99, 86, 87, 88, 86, 103, 87, 94, 78, 77, 85, 86]
# # we can find the mean and median using numpy
# x_mean = numpy.mean(speed)
# x_median = numpy.median(speed)
# # for finding mode we have to use scipy module
# x_mode = stats.mode(speed)
# print("mean is: ", x_mean)
# print("median is: ", x_median)
# print("mode is: ", x_mode)
#
# # standard deviation
# x_std_deviation = numpy.std(speed)
# print(x_std_deviation)
#
# # finding of variance
# x_variance = numpy.var(speed)
# print(x_variance)
#
# # finding of percentile
# x_percentile = numpy.percentile(speed, 90)
# print(x_percentile)

# *************data distribution*******************

# create a array containing 250 random floats between 0 and 5
# import numpy
# x = numpy.random.uniform(0.0, 5.0, 250)
# print(x)

# histogram
# import numpy
# import matplotlib.pyplot as plt

# x = numpy.random.uniform(0.0, 5.0, 250)    # it is uniform distribution of data
# with 9 bars
# plt.hist(x, 9)
# plt.show()

# creating an array with 1 lakh float random numbers between 0 to 5 and display them using a histogram with 100 bars
# x = numpy.random.uniform(0.0, 5.0, 100000)
#
# plt.hist(x, 100)
# plt.show()

# normal data distribution

# x = numpy.random.normal(0.0, 5.0, 100000)  # it is normal distribution of data
# plt.hist(x, 100)
# plt.show()


# *******************scattter plot****************
# import matplotlib.pyplot as plt
#
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#
# plt.scatter(x, y)
# plt.show()

# ***********random data distribution***************

# let us create two arrays that are both filled with 1000 random numbers from a normal data distribution.
#
# The first array will have the mean set to 5.0 with a standard deviation of 1.0.
#
# The second array will have the mean set to 10.0 with a standard deviation of 2.0:

# import numpy
# import matplotlib.pyplot as plt
#
# x = numpy.random.normal(5.0, 1.0, 1000)
# y = numpy.random.normal(10.0, 2.0, 1000)
#
# plt.scatter(x, y)
# plt.show()