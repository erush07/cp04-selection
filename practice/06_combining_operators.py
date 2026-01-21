from helper_functions import clear_screen
clear_screen()

# ===================
# COMBINING OPERATORS
# ===================

'''
OVERVIEW
--------
or, and, & not aren't too complicated when used by themselves,
but it can get a little trickier when combined together.

Keep in mind that python has an order that it evaluates
the operators:

    1:  not
    2:  and
    3:  or

BUT that order can be overridden by using parentheses.
Use parentheses to group conditions together to make sure they are
evaluated correctly
'''


# 1. SCENARIO
'''
For orders, customers should receive free shipping if the order is not flagged
and if either the total is over $50 or they have a FREESHIPPING coupon
Free shipping if the order is not flagged, and (total ≥ 50 OR coupon is “FREESHIP”).
'''
# Using the variables below create an if/else statement that prints "FREE SHIPPING"
# if the order should get free shipping, or "NO FREE SHIPPING" if the order
# shouldn't get free shipping

order_total = 20
coupon = "FREESHIPPING"
flagged = False




# 2. SCENARIO:
'''
A student can win a prize based on a few combinations of conditions.
We have 4 conditions we will evaluate:
  - grades_above_90
  - attendance_above_90
  - extracurriculars
  - no_behavior_issues

Rules:
  - No student can win a prize if they have behavior issues.
  - A student can win a prize if they have grades_above_90 OR
    if they have both attendance_above_90 AND extracurriculars.
'''

# SITUATION:
# A student has everything they need, except they have behavior issues.
grades_above_90 = True
attendance_above_90 = True    
extracurriculars = True  
no_behavior_issues = False   

# S1.1 - WITHOUT PARENTHESES: 
# This is written without parentheses separating the conditions.
# Stare at it for a minute. Is it working correctly?

if (no_behavior_issues == True and grades_above_90 == True
    or attendance_above_90 == True and extracurriculars == True):
    print("ex1.1: Student wins the prize! (incorrect logic)")
else:
    print("ex1.1: Student does not win the prize. (incorrect logic)")

'''
TIP
---
Yes there are parentheses at the beginning and end of the if conditions.
That is to make it so I can put the conditions on multiple lines of code.
The point here is that there aren't parentheses separating the
various conditions
'''


# 1. MATCH IF STATEMENT TO NEW LOGIC:
# Let's change the rules:
# Make it so a student can win a prize as long as they have at least one of:
#   - grades above 90
#   - attendance above 90
#   - extracurricular activities.
# But they still can't have behavioral issues in any case.
# evaluate the student below and write an if statement that accurately 
# reflects this logic:

grades_above_90 = False
attendance_above_90 = False
extracurriculars = True
no_behavior_issues = True


