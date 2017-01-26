#!/usr/bin/python

# Example program to read data from MCP3008 10 bit ADC

import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
# Define sensor channels
first_channel = 0
second_channel  = 1
 
# Define delay between readings
delay = 5

print "------------------------------------------------------"
 
while True:
 
  # Read the first channel data
  first_level = ReadChannel(first_channel)
  first_channel_volts = ConvertVolts(first_level,2)
 
  # Read the second channel data
  second_level = ReadChannel(second_channel)
  second_channel_volts = ConvertVolts(second_level,2)
  
 
  # Print out results
  print "------------------------------------------------------"
  print("First ADC channel: {} ({}V)".format(first_level,first_channel_volts))
  print("Second ADC channel : {} ({}V)".format(second_level,second_channel_volts))
 
  # Wait before repeating loop
  time.sleep(delay)

