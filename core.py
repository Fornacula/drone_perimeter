# -*- coding: utf-8 -*-

from config import *
import serial
import time
import sys
import signal


class Core():

	def __init__(self):

		self.processes = []
		self.following = True
		self.camera_samples = 0
		self.distance_sum = 0
		self.direction_sum = 0

		time.sleep(1)


	def start(self):
		for proc in self.processes:
			proc.start()

	def stop(self):
		print('stop')