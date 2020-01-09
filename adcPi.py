#!/usr/bin/env python

# Reads the inputs of the MCP3008

import spidev
import time

# Definitions 
ch = 1 # Channel 0

# SPI Initialization 
spi = spidev.SpiDev()
spi.open(0,0) 
spi.max_speed_hz=1000000

# Function: Read a channel
# Arg1 - Channel to read (1-8)
def readADC(channel):
	# channel = channel - 1
	if channel > 7 or channel < 0:
		return -1
	rawData = spi.xfer2([1, 8 + channel << 4, 0])
	ADCData = ((rawData[1] & 3) << 8) + rawData[2]
	return ADCData
	
count = 0

while True:
	data = []
	
	for channel in range(8):
		data.append(readADC(channel))
	
	print(data)
	print("\n")