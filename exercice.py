#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(index):

	#get fibonnaci number at index n

	if index ==0:
		return 0
	elif index ==1:
		return 1
	else:
		return get_fibonacci_number(index-1) + get_fibonacci_number(index-2)


def get_fibonacci_sequence(length):

	#get the fibonacci sequence of length n	

	if length ==1:
		return [0]
	elif length ==2:
		return [0,1]
	else:
		fibonacci = [0,1]
		for i in range(2,length):
			fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
		return fibonacci

def get_sorted_dict_by_decimals(bouffe):

	#sort a dict by the decimal part of the values 

	sorted_dict1 = {}

	for key, value in bouffe.items():
		sorted_dict1[key] = round(value % 1, 2)
		sorted_dict1 = dict(sorted(sorted_dict1.items(), key=lambda item: item[1]))
	return sorted_dict1

	#idk how to keep the same numbers in the sorted dict

def fibonacci_numbers(length):
	pass

def build_recursive_sequence_generator(TODO):
	pass


if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator(TODO)
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator(TODO)
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator(TODO)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
