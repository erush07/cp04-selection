from helper_functions import clear_screen
clear_screen()

# ===========================
# IF, ELIF, AND ELSE PRACTICE
# ===========================

# 1. USE IF, ELIF, AND ELSE WITH INPUT():
# Ask the user to enter their favorite day of the week.
# If it is Monday, print "wow, early weekday"
# If it is Wednesday print "wow, midweek!"
# If it is Saturday print "weekend, woo!"
# If it is any other day, print "that day's pretty good too"

# CHALLENGE: Try and make it so your code works no matter how the
#            the day of the week is capitalized.

fav_day = input("What is your favorite day of the week? (Monday, Tuesday, etc.) ").lower()
#fav_day = fav_day

if fav_day == "monday":
    print("wow, early weekday")
elif fav_day == "wednesday":
    print("wow, midweek!")
elif fav_day == "saturday":
    print("weekend, woo!")
else:
    print("that day's pretty good too")