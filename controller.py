# -*- coding: utf-8 -*-

from config import *

class Controller():

	def __init__(self, core):
		Process.__init__(self, 'Controller')
		self.core = core

		self.prepare()