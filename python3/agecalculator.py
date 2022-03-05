#AGE CALCULATOR - Day 2
#WRITTEN BY - GitHub.com/ItzKakarotto

#Built in ¯\_(ツ)_/¯
from datetime import date as dt

#Made a variable to make it more Flexible
STR = "\nYou are {} months, {} weeks, {} days, {} hours, {} minutes, {} seconds old!\n"

def getdob():
	"""To Get the proper Date of Birth without any Errors"""
	dob = input("Enter your Date of Birth. Eg. - 19/05/2007\n > ")
	try:
		date, month, year= dob.split('/')
		date, month, year = int(date), int(month), int(year)
		dt(year, month, date)
	except:
		print("Please Enter a valid Date of Birth!\n")
		return getdob()
	if dt.today().day == int(date) and dt.today().month==int(month):
		print("Before we proceed... Happy Birthday!")
	return  date, month, year

def getage(date, month, year):
	"""The Main Function which calculates your age"""
	td = dt.today()
	tdd, tdm, tdy= td.day, td.month, td.year
	
	year_old = tdy-year
	month_old = tdm-month
	date_old = tdd-date

	if month_old<0:
		year_old = year_old-1
		month_old = month_old +12
	if date_old<0:
		month_old = month_old-1
		date_old = date_old+30

	return year_old, month_old, date_old

def more(yr, mt, day):
	"""Convert your age into Other forms"""
	months = mt + yr*12
	weeks = day/7 + mt*4.345 + yr*52.143
	days = day + mt*30.417 + yr*365
	hours = days*24
	minutes = hours*60
	seconds = minutes*60
	
	return months, weeks, days, hours, minutes, seconds
	
def main():
	"""The Switch"""
	date, month, year = getdob()
	year_old, month_old, date_old = getage(date, month, year)
	print(f"\nYou are {year_old} years, {month_old} month, {date_old} days old!")
	
	"""Meowre Onee Chan!"""
	inp  = input("\nPress Enter for more\n > ")
	if not inp:
		months, weeks, days, hours, minutes, seconds = more(year_old, month_old, date_old)
		print(STR.format(round(months), round(weeks), round(days), round(hours), round(minutes), round(seconds)))
		

main()