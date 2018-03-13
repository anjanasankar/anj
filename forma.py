def convert_to_24(time):
"""str -> str
converts 12 hours time format to 24 hours
"""
return time[:-2] if time[-2:] == "AM" else str(int(time[:2]) + 12) + time[2:8]
