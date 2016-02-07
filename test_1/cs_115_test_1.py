#!/usr/bin/env python

def age_in_days_cal():
	age = int(input('Please input your age: '))
	name = str(input('Please input your name: '))
	age_in_days = age * 365

	print(name, "you are ", age_in_days, "days old.")

if __name__ == "__main__":
	age_in_days_cal()
