import sys
import time
import datetime

from show_month_day import TimeScript

#check input from command line argument 
print(sys.argv[1])		#starting year
print(sys.argv[2])		#starting month
print(sys.argv[3])		#starting date
print(sys.argv[4])		#ending year
print(sys.argv[5])		#ending month
print(sys.argv[6])		#ending date

#Store input from arguments    
StartYear = sys.argv[1]		#starting year
StartMonth = sys.argv[2]	#starting month
StartDate = sys.argv[3]		#starting date
EndYear = sys.argv[4]		#ending year
EndMonth = sys.argv[5]		#ending month
EndDate = sys.argv[6]		#ending date

#put data into function to get the result
date_list = TimeScript.__init__(set_time, StartYear, StartMonth, StartDate, EndYear, EndMonth, EndDate)

#Check the result of function is correct
print('Result: ' )
print(date_list)