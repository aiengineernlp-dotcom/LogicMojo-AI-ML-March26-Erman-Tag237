login_hours = [1, 3, 5, 7, 2, 6, 8, 4, 9, 10]
"""Separates login hours into even-hour logins and odd-hour logins."""
even_hour = []
odd_hour = []
for i in login_hours:
    if i%2==0:
        even_hour.append(i)
    else:
        odd_hour.append(i)
print(f"\n The even_hour {even_hour}")
print(f"\n The odd_hour {odd_hour}")
print("\n")

"""Identifies login hours that fall into peak activity time (hours greater than 5)."""
fall_into_peak_activity_time = []
for i in login_hours:
    if i>5:
        fall_into_peak_activity_time.append(i)
print(f"fall into peak activity time, {fall_into_peak_activity_time}")

print("\n")
"""Sorts the login hours in ascending order."""
Sorts_login_ascending_order = sorted(login_hours,reverse = False)
print(Sorts_login_ascending_order)

"""Calculates how many logins occurred during peak hours."""
print("\n")
print(f"fall into peak activity time, {fall_into_peak_activity_time}")
print(f"Logins occurred during the pick hour: {len(fall_into_peak_activity_time)} times ")