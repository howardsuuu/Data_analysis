#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:25:34 2018

@author: howardsu666
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas
import seaborn

# Read the CSV file
data = pandas.read_csv(r"/Users/howardsu666/Github/First_Python"
                       r"/uber-raw-data-apr14.csv")

# Split the Date and Time, process the data
    #dt = '4/30/2014 23:22:00'
    # d, t = dt.split(' ')
    # print(d)

# Apply the pandas.to_datetime() to see the real date
    # dt = pandas.to_datetime(dt)
    # print(dt.weekday_name)
    # print(dt.year)

#change 4/30/2014 into 2014-04-01(Object form to Date form)
data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)
#add other infos into the columns(Day of month, Weekday(0=Monday), hour)
def get_dom(dt):
     return dt.day
data['dom'] = data['Date/Time'].map(get_dom)

def get_weekday(dt):
    return dt.weekday()
data['Weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour
data['Hour'] = data['Date/Time'].map(get_hour)


#Histogram of the Day of Months, bins = how many part are being divided, 
    # rwidth = .8 distance of each Hist, range
plt.hist(data.dom, bins = 30, rwidth = 0.8 , range=(0.5, 30.5))
plt.xlabel('Date of the Month')
plt.ylabel('Frequency')
plt.title('Freq by DoM - Uber - Apr 2014')
plt.show()
# Show the exact amount of each month( Not sorted yet)
    #for k, rows in data.groupby('dom'):
        #print(k, len(rows))
def count_rows(rows):
    return len(rows)
# Show the exact amount of each month(not sorted yet)
    # .groupby = group the data based on ('Variable')
by_date = data.groupby('dom').apply(count_rows)
# Sort the value of each month
by_date_sorted = by_date.sort_values()


#Bar Chart of DoM
plt.bar(range(1, 31), by_date)
plt.xticks(range(1, 31), by_date.index) 
plt.xlabel('Date of the Month')
plt.ylabel('Frequency')
plt.title('FQ by DoM -- Apr 2014')
plt.show()

# Hist of the Weekdays
plt.hist(data.Weekday, bins = 7, range = (-0.5, 6.5), 
         rwidth = 0.8, color = 'green')
plt.xticks(range(0, 7), 'Mon Tue Wed Thu Fri Sat Sun'.split())
plt.ylabel('Total amount of days')
plt.title('Weekday of the Apr 2014')
plt.show()



# Hist of Lon & Lat
plt.hist(data['Lon'], bins = 100, range=(-74.1, -73.9), color = 'g', alpha=.5, label = 'longitude')
plt.grid(False) # delete the grid
plt.legend(loc = 'upper left')#loc == location
plt.twiny() # twiny()== Create a twin Axes sharing the yaxis
plt.hist(data['Lat'], bins=100, range=(40.5, 41), color='r', alpha=.5, label='Latitude')
plt.legend(loc = 'best') #
plt.show()

# Cross analysis(Hour, weekday)  (Vertical Horizontal)    # unstack the data
cross_analyze = data.groupby('Weekday Hour '.split()).apply(count_rows).unstack()
# Heat plot for Cross analysis
seaborn.heatmap(cross_analyze)

# dot plot for Lon & Log
#plt.figure(figsize = (20,20))
#plt.plot(data['Lon'], data['Lat'],'.', ms=1, alpha =.5)#'.' means dot plot
#plt.xlim(-74.2, -73.7) #Get or set the x limits of the current axes.
#plt.ylabel(40.7, 41)
#plt.show()




