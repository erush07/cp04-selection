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


# SCENARIO
'''
For orders, customers should receive free shipping if the order is not flagged
and if either the total is over $50 or they have a FREESHIPPING coupon
Free shipping if the order is not flagged, and (total ≥ 50 OR coupon is “FREESHIP”).
'''


order_total = 20
coupon = "FREESHIPPING"
flagged = False

# WRONG: coupon can bypass the flagged check
if not flagged and order_total >= 50 or coupon == "FREESHIPPING":
    print("WRONG: free shipping")
else:
    print("WRONG: no free shipping")

# RIGHT: group the OR part
if (not flagged) and (order_total >= 50 or coupon == "FREESHIPPING"):
    print("RIGHT: free shipping")
else:
    print("RIGHT: no free shipping")

# SCENARIO FOR EXAMPLES BELOW:
# A student can win a prize based on a few combinations of conditions.
# We have 4 conditions we will evaluate:
#   - grades_above_90
#   - attendance_above_90
#   - extracurriculars
#   - no_behavior_issues

# Rules:
#   - No student can win a prize if they have behavior issues.
#   - A student can win a prize if they have grades_above_90 OR
#     if they have both attendance_above_90 AND extracurriculars.

# SITUATION:
# A student has everything they need, except they have behavior issues.
grades_above_90 = True
attendance_above_90 = True    
extracurriculars = True  
no_behavior_issues = False   

# S1.1 - WITHOUT PARENTHESES: 


if no_behavior_issues and (grades_above_90
    or attendance_above_90 and extracurriculars):
    print("ex1.1: Student wins the prize! (incorrect logic)")
else:
    print("ex1.1: Student does not win the prize. (incorrect logic)")

