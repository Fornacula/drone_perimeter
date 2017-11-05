# -*- coding: utf-8 -*-

from config import *
import serial
import time
import sys
import signal


class Core():

	def __init__(self):

		self.processes = []

		self.controller = Controller()
		self.processes.append(self.controller)

		self.camera = Camera(self.controller)
		self.processes.append(self.camera)

		time.sleep(1)


	def start(self):
		for proc in self.processes:
			proc.start()

	def stop(self):
		for proc in self.processes:
			proc.stop()