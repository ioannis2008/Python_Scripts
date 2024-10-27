from datetime import datetime, timedelta

def add_minutes(minutes):
    current_time = datetime.now()
    new_time = current_time + timedelta(minutes=minutes)
    return current_time, new_time

try:
    minutes_to_add = int(input("Enter estimated delay: "))
    current_time, new_time = add_minutes(minutes_to_add)

    print("Current Time:", current_time.strftime("%H:%M"))
    print(f"Estimated time of arival (+{minutes_to_add} minutes):", new_time.strftime("%H:%M"))

except ValueError:
    print("Please enter a valid integer for minutes.")
