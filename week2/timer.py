# a script that solves problem #7
# here we're keeping our time left
_time = 0

# sets '_time' with 'seconds'
# if it's not already set
def start_timer(seconds):
	global _time

	if _time > 0 or seconds <= 0:
		return False

	_time = seconds
	return True

# decreases '_time' with 1 if greater than 0
def decrease_timer():
	global _time

	if _time <= 0:
		return False

	_time -= 1
	return True

# checks if timer is running i.e.
# '_time' is greater than 0
def is_timer_running():
	return _time > 0

# stops timer, i.e. sets '_time' to 0
def stop_timer():
	global _time

	if _time > 0:
		_time = 0
		return True
	
	return False

# returns time left
def seconds_left():
	return _time