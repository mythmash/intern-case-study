# Case Study Code

concatenator.py
Used to concatenate the field data files together. Must be run before other files.

totalCharge.py
Finds the sum of all changes in charge for each location. Found by subtracting CycleFirstValue from CycleLastValue for rows tagged percent_chg.

usageTimeTotal.py
Finds how much time each location was used. Found by subtracting start_epoch_ms from end_epoch_ms for each session and summing across all sessions.

deltaTemperature.py
Finds the maximum change in handle_temperature out of all sessions. Compares the difference between min and CycleFirstValue and min and CycleLastValue and keeps the max.

numberUses.py
Finds out how many sessions happened at each location.
