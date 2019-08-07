from Tkinter import *
import os
import tkFileDialog

class App:
    
    #use a callback to start the process
    def start (self):
        os.system('launchctl load /Library/LaunchAgents/com.auto.print.rcpt.plist')
        
    #use a callback to stop the process    
    def stop (self):
        os.system('launchctl unload /Library/LaunchAgents/com.auto.print.rcpt.plist')
    #get the file directory and create the settings.txt.
    def askdirectory (self):
        my_directory = tkFileDialog.askdirectory(**self.dir_opt)
        output = open('/Applications/AutoPrintMac.app/Contents/Resources/Settings.txt', 'wb')
        output.write(my_directory)
        output.close()
        os.system('launchctl unload /Library/LaunchAgents/com.auto.print.rcpt.plist')
        os.system('launchctl load /Library/LaunchAgents/com.auto.print.rcpt.plist')


    def __init__(self, master):
        frame = Frame()
        frame.pack()

        #create the start button
        startButton = Button(
            frame, text = "Start", command = self.start
            ).pack(side = LEFT)
        
        #create the stop button
        stopButton = Button(
            frame, text = "Stop", command = self.stop
            ).pack(side = RIGHT)
        
        #create the fileDirectory button
        fileButton = Button(
           frame, text = "find '.rcpt' directory", command=self.askdirectory
            ).pack(side = BOTTOM)

        #options for the directory
        self.dir_opt = options = {}
        options['initialdir'] = '~/Downloads'
        options['mustexist'] = True
        options['parent'] = root
        
root = Tk()
root.wm_title("Atriuum Auto Print Monitor")
app = App(root)
root.lift()
root.mainloop()
