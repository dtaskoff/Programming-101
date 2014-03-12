import unittest
import timer

# my tests for the timer module
class TimerTest(unittest.TestCase):
	def test_start_timer(self):
		timer._time = 0
		result = timer.start_timer(42)
		self.assertEqual(42, timer._time)
		self.assertTrue(result)

	def test_start_timer_when_already_started(self):
		timer._time = 0
		timer.start_timer(42)
		result = timer.start_timer(7)
		self.assertEqual(False, result)

	def test_start_timer_with_negative_seconds(self):
		timer._time = 0
		result = timer.start_timer(-2)
		self.assertEqual(False, result)

	def test_decrease_timer(self):
		timer._time = 21
		result = timer.decrease_timer()
		self.assertEqual(20, timer._time)
		self.assertTrue(result)

	def test_decrease_timer_when_time_is_over(self):
		timer._time = 0
		result = timer.decrease_timer()
		self.assertEqual(False, result)

	def test_is_timer_running(self):
		timer._time = 1
		self.assertTrue(timer.is_timer_running())
		timer._time = 0
		self.assertEqual(False, timer.is_timer_running())

	def test_stop_timer(self):
		timer._time = 1
		self.assertTrue(timer.stop_timer())
		timer._time = 0
		self.assertEqual(False, timer.stop_timer())

	def test_remaining_seconds_left(self):
		timer._time = 10 
		self.assertEqual(10, timer.seconds_left())

	def test_seconds_left_with_stopped_timer(self):
		timer.stop_timer()
		self.assertEqual(0, timer.seconds_left())

if __name__ == '__main__':
	unittest.main()