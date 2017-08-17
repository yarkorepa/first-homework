import time
import random
from functools import reduce

def for1():
	currenttime = time.time()
	for i in range(10000):
		5 == 5
	currenttime = time.time() - currenttime
	print('for %s' % currenttime)
for1()

def while1():
	count = 0
	currenttime = time.time()
	while (count < 10000):
		5 == 5
		count += 1
	currenttime = time.time() - currenttime
	print('while %s' % currenttime)
while1()
def map1():
	currenttime = time.time()
	array = list(map((lambda i = 5: i == 5),range(10000)))
	currenttime = time.time() - currenttime
	print('map %s' % currenttime)
map1()
def filter1():
	currenttime = time.time()
	array = list(filter((lambda i: 5 == 5),range(10000)))
	currenttime = time.time() - currenttime
	print('filter %s' % currenttime)
filter1()
def reduce1():
	currenttime = time.time()
	array = reduce((lambda x = 5, y = 5: x == y), range(10000))
	currenttime = time.time() - currenttime
	print('reduce %s'  % currenttime)
reduce1()
def list_generator1():
	currenttime = time.time()
	array = [i for i in (5 == 5 for i  in range(10000))]
	currenttime = time.time() - currenttime
	print('list_generator %s ' % currenttime)
list_generator1()
def dict_generator1():
	currenttime = time.time()
	array = {i: 5 == 5 for i  in range(10000)}
	currenttime = time.time() - currenttime
	print('dict_generator %s' % currenttime)
dict_generator1()
def set_generator1():
	currenttime = time.time()
	array = {i for i in (5 == 5 for i  in range(10000))}
	currenttime = time.time() - currenttime
	print('set %s' %currenttime)
set_generator1()

