# -*- coding: utf-8 -*-


import sys, select, os
import math
from config import *
from core import *

# main loop
def main(argv):

	core = Core()
	core.start()

	#Loop until the user clicks the close button.
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')

		if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
			#line = raw_input()
			core.stop()
			break



if __name__ == '__main__':
	#main(sys.argv[1:])
	main(sys.argv)