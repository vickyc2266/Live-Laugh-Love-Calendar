#All graphics are from CMU graphics and all functions are from CMU 112 notes
#All functions/ideas are from CMU 112 notes
from cmu_112_graphics import *
from math import *

#Button Class that stores the characteristics of creating a button using 
#both the createButtonOval and createButtonRectangle functions
class Button:
    def __init__(self, x0, y0, x1, y1, fill, txtx, txty, text, txtfill, font): 
        self.x0 = x0 
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.fill = fill 
        self.outline = "black"
        self.width = 5
        self.txtx = txtx
        self.txty = txty
        self.text = text
        self.txtfill = txtfill
        self.font = font 
        # self.function = function
    
    def buttonClicked(self, x, y): 
        if x >= self.x0 and x <= self.x1 and y >= self.y0 and y <= self.y1: 
            return True
        else: 
            return False

#Contains all the common characteristics each screens needs/uses including
#creating screen titles, directions, or random words
class Screens: 
    def __init__(self, x, y, text, fill, font): 
        self.x = x
        self.y = y
        self.text = text
        self.fill = fill
        self.font = font

    def createTitle(self, app, canvas): 
        canvas.create_text(self.x, self.y, text = self.text, fill = self.fill, 
        font = self.font)
    
    def createDir(self, app, canvas): 
        canvas.create_text(self.x, self.y, text = self.text, fill = self.fill, 
            font = self.font)
    
    def createRandomWords(self, app, canvas): 
        canvas.create_text(self.x, self.y, text = self.text, fill = self.fill, 
        font = self.font)
    
    def createVanishWords(self, app, canvas):
        if app.showtext:
            canvas.create_text(self.x, self.y, text = self.text, 
            fill = self.fill, font = self.font)
    
    def createVanishWords2(self, app, canvas):
        if app.showtext2:
            canvas.create_text(self.x, self.y, text = self.text, 
            fill = self.fill, font = self.font)

#Events class that stores the basic information that's inputted through the 
#users and split into different types of Events for the program's purpose
class Event: 
    def __init__(self, name, type, stime, etime, day): 
        self.name = name 
        self.type = type 
        self. stime = stime 
        self.etime = etime 
        self.day = day
        self.myEvent = (self.name, self.type, self.stime, self.etime, self.day)
    
    def __repr__(self): 
        return self.name

################################################################################
#Classes below haven't been implemented yet or maybe will not use

class ProductiveEvents(Event): 
    def __init__(self):
        super().__init__()
    def addEvents(self, type, stime, etime, day): 
        productiveEventsList = []
        if self.type == "WorkOrSchool": 
            productiveEventsList.append(self.myEvent)

class Sleep(Event): 
    def __init__(self, day, stime, etime):
        self.day = day 
        self.stime = stime 
        self.etime = etime
        sleepSchedule = (self.day, self.stime, self.etime)
        sleepScheduleList = [sleepSchedule]

class Fitness(Event):
    def __init__(self, day, stime, etime): 
        self.day = day
        self.stime = stime 
        self.etime = etime 
        fitnessSchedule = (self.day, self.stime, self.etime)
        fitnessScheduleList = [fitnessSchedule]

#Alert class shows the different messages/alerts that show during diff scenarios
class Alerts: 
    sleepAlert = """According to the American
    Academy of Sleep Medicine and Sleep Research Society, a healthy adult is 
    recommended to have at least 7 hours of sleep per night but the system shows 
    your planned sleeping habits does not meet such requirments. Please make 
    adjustments to your sleep schedule."""
    fitnessAlert = """According to the Physical Activity Guidelines for 
    Americans, a healthy young adult needs a least 150 minutes of 
    moderately intensive physical activity
    but the system shows your schedule does not meet such requirement. Please 
    make adjustments in your fitness schedule."""
    workAlert = """According to your planning, the program realizes you're 
    being overworked! Click the button below to help find 
    availible time on your schedule to enjoy life! """
    scheduleAlert = """It seems like there's an overlap of scheduling in your 
    calendar."""
    errorAlert = """It seems there's something wrong with the information 
    you're inputting. Please double check your information input before 
    clicking the complete the button."""
    doubleBookingAlert = """It seems like there you're trying to double book
    the same time slot on your calendar. Please double check to make sure 
    there's no overlap for the time you're trying to input."""
    messageList = [sleepAlert, fitnessAlert, workAlert, 
        scheduleAlert, errorAlert, doubleBookingAlert]
    sleepAlertTitle = "NOT ENOUGH SLEEP HOURS!!!"
    fitnessAlertTitle = "NOT ENOUGH FITNESS HOURS!!!"
    workAlertTitle = "OVERWORKED!!!"
    scheduleAlertTitle = "SCHEDULING ALERT!!!"
    errorAlertTitle = "INFORMATION INPUT ERROR!!!"
    doubleBookingTitle = "DOUBLE BOOKING FOUND"
    messageTitleList = [sleepAlertTitle, fitnessAlertTitle, workAlertTitle, 
        scheduleAlertTitle, errorAlertTitle, doubleBookingTitle]
   
    def __init__(self, messageList, messageTitleList):
        self.messageList = messageList
        self.messageTitleList = messageTitleList
