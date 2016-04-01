""" Utilities for formatting shell output """
import time

def asterisks(func):
	def wrapper():

		print("********************************************************************************")
		func()
		print("********************************************************************************")

	return wrapper

@asterisks
def print_begin():
	print("BEGIN")

@asterisks
def print_end():
	print("END")

def print_begin_end(func):
	def wrapper():

		print()
		print_begin()	
		print()
		func()
		print()
		print_end()
		print()

	return wrapper

def print_run_time(func):
	def wrapper():

		start_time = time.time()
		func()
		end_time = time.time()
		duration = (end_time - start_time)
		mins = int(duration) % 60
		seconds = int(duration) - (mins * 60)
		print("Runtime: {} minutes and {} seconds".format(mins,seconds))
		print()

	return wrapper

def print_func_info(func):

	@print_run_time
	@print_begin_end
	def wrapper():
		func()

	return wrapper















