# -*- coding: utf-8 -*-

from config import *
import serial

class Process():

	def __init__(self, name):

		self.name = name
		self.is_running = False
		self.commands = None

	def start(self):
		self.is_running = True
		return

	def stop(self):
		self.is_running = False
		return

	def is_running(self):
		return self.is_running

	def has_method(self, cmd):
		return (True if self.commands and (cmd in self.commands) else False)

	def process_command(self, command):
		return