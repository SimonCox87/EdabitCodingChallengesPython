"""A financial institution provides professional services to banks and claims charges from the customers based on the number of 
man-days provided. Internally, it has set a scheme to motivate and reward staff to meet and exceed targeted billable utilization 
and revenues by paying a bonus for each day claimed from customers in excess of a threshold target.

This quarterly scheme is calculated with a threshold target of 32 days per quarter, and the incentive payment for each billable day 
in excess of such threshold target is shown as follows:
Days	Bonus
0 to 32 days	Zero
33 to 40 days	SGD$325 per billable day
41 to 48 days	SGD$550 per billable day
Greater than 48 days	SGD$600 per billable day

Please note that incentive payment is calculated progressively. As an example, if an employee reached total billable days of 45 in 
a quarter, his/her incentive payment is computed as follows:

32*0 + 8*325 + 5*550 = 5350

Write a function to read the billable days of an employee and return the bonus he/she has obtained in that quarter.
Examples

bonus(15) ➞ 0

bonus(37) ➞ 1625

bonus(50) ➞ 8200"""

"""def bonus(days):
    if days < 32:
        return 0
    elif days > 32 and days < 41:
        return 325 * (days - 32)
    elif days > 41 and days < 49:
        return 550 * (days - 41) + 2600
    else:
        return 600 * (days - 48) + 2600  + 4400

print(bonus(15))
print(bonus(37))
print(bonus(50))"""

def bonus(days):
    return 0 if days<32 else 325*(days-32) if days>32 and days<41 else 550*(days-41)+2600 if days>41 and days<49 else 600*(days-48)+2600+4400

print(bonus(15))
print(bonus(37))
print(bonus(50))

"""def bonus(days):
	return 325*max(0,days-32) + 225*max(0,days-40) + 50*max(0,days-48)"""