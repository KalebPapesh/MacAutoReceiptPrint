#!/usr/bin/env python
import os, time

#prints the receipt
def printRCPT (pdf):
  #send the lp command with custom letter size to printer
  os.system('lp %s' % pdf)

path_to_watch = os.path.expanduser("~/Documents/")

#list all files in the directory as a dictionary
before = dict ([(file_now, None) for file_now in os.listdir (path_to_watch)])

while 1:
  #wait for 1 second
  time.sleep (1)
  
  #list all files in the directory again as another dictionary
  after = dict ([(file_now, None) for file_now in os.listdir (path_to_watch)])
  
  #compare the differences between the two dictionaries
  #before and after with a list of files added
  added = [file_now for file_now in after if not file_now in before]

  #go through all the files that have been added
  for file_now in added:
      #if the file extension ends in 'rcpt' then:
      if file_now.endswith('.rcpt') == True:
        inputFile = os.path.join(path_to_watch, file_now)
        printRCPT(inputFile)
        #delete the files after printing
        #to cut down on number of files in the downloads folder.
        os.remove(inputFile)
  before = after
