#!/usr/bin/env python
"""
cs115_proj_1 Tax Calculator
Andrew Seith Miller
Release Date: 1/4/2016

This module supplies one function cal_total_with_tax(). For example,

>>> cal_total_with_tax()
Please input the amount of purchase: 100
Amount of purchase:               100.00
State tax:                          5.00
County tax:                         2.50
County tax:                       107.50

Know Limitation: accepts floats with more then 2 decimal places
but formats output down to just 2 decimal places
"""


def cal_total_with_tax():
    """prompt the user to input their "amount of purchase",
    calculate the state, and county tax for their purchase,
    print a receipt.
    """

    my_format = '{0:<20}{1:>20,.2f}'  # set your desired output format

    """input: prompts user for amount of purchase"""
    purchase_amount = float(input('Please input the amount of purchase: '))

    """calculation: does all the maths"""
    state_tax = 0.05 * purchase_amount
    county_tax = 0.025 * purchase_amount
    total_of_sale = purchase_amount + state_tax + county_tax

    """output: print the receipt"""
    print(my_format.format('Amount of purchase:', purchase_amount))
    print(my_format.format('State tax:', state_tax))
    print(my_format.format('County tax:', county_tax))
    print(my_format.format('County tax:', total_of_sale))

if __name__ == "__main__":
    cal_total_with_tax()
