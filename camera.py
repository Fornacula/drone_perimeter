# -*- coding: utf-8 -*-

from config import *
from core import *
from controller import *
import cv2
import sys

class Camera():

	def __init__(self, subscriber):
		self.subscriber = None
		self.running = False
		if isinstance(subscriber, Controller):
			self.subscriber = subscriber

		self.connect()
		_thread.start_new_thread(self.run, ())
		self.start()

	def run(self):
		if not video.isOpened():
			print('video is not opened')
			return

		ok, frame = self.video.read()

		while True:
			if self.running:
					# Update tracker
					ok, bbox = tracker.update(frame)
					if ok:
						# Draw bounding box
						print(str(bbox[0]) + ', '+str(bbox[1]) + ', '+str(bbox[2]) + ', '+str(bbox[3]))
						#p1 = (int(bbox[0]), int(bbox[1]))
						#p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
						#cv2.rectangle(frame, p1, p2, (0,0,255))

						# Display result
						#cv2.imshow("Tracking", frame)

	def connect(self):
		# Set up tracker.
		# Instead of MIL, you can also use
		# BOOSTING, KCF, TLD, MEDIANFLOW or GOTURN

		self.tracker = cv2.Tracker_create("KCF")

		# Read video
		self.video = cv2.VideoCapture(0)

		# Exit if video not opened.
		if not self.video.isOpened():
			print "Could not open video"
			sys.exit()

		# Read first frame.
		ok, frame = self.video.read()
		if not ok:
			print 'Cannot read video file'
			sys.exit()

		# Uncomment the line below to select a different bounding box
		bbox = cv2.selectROI(frame, False)

		# Initialize tracker with first frame and bounding box
		ok = tracker.init(frame, bbox)

	def stop(self):
		self.running = False

	def start(self):
		self.running = True

	def __exit__(self):
		try:
			self.logfile.close()
			self.serial.close()
		except:
			print(sys.exc_info()[0])