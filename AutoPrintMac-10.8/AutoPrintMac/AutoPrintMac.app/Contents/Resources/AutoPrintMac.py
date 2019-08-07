#!/usr/bin/env python
from ho import pisa
import os, time

#creates the pdf
def createPDF(inputFile):
  input = open(inputFile).read()
  output = file(pdf, "wb")
  pisa.showLogging()
  pisa.CreatePDF(input, output)
  output.close()

#prints the receipt
def printRCPT (pdf):
  #send the lp command with custom letter size to printer
  os.system('lp -o media=Custom.200x11in %s' % pdf)

#Check to see if the Settings File exists
if os.path.isfile("/Applications/AutoPrintMac.app/Contents/Resources/Settings.txt"):
    openSettingsTxt = open('/Applications/AutoPrintMac.app/Contents/Resources/Settings.txt', 'rb')
    path_to_watch = openSettingsTxt.read()
    if not path_to_watch:
      path_to_watch = os.path.expanduser("~/Downloads/")
else:
    path_to_watch = os.path.expanduser("~/Downloads/")

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
        pdf = (path_to_watch+file_now.rstrip('rcpt')+'pdf')
        inputFile = os.path.join(path_to_watch, file_now)
        createPDF(inputFile)
        printRCPT(pdf)
        #delete the files after printing
        #to cut down on number of files in the downloads folder.
        os.remove(inputFile)
        os.remove(pdf)
  before = after
