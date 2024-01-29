#All graphics are from CMU graphics and all functions are from CMU 112 notes
#All functions/ideas are from CMU 112 notes
from cmu_112_graphics import *
from math import *
from FinalizedTPClasses import *

#Uses the Button Class from FinalizedTPClasses file to draw Oval Buttons
def createButtonOval(app, canvas, eachbutton): 
    canvas.create_oval(eachbutton.x0, eachbutton.y0, eachbutton.x1, 
    eachbutton.y1, fill = eachbutton.fill, outline = eachbutton.outline, 
    width = eachbutton.width)
    canvas.create_text(eachbutton.txtx, eachbutton.txty, text = eachbutton.text, 
    fill = eachbutton.txtfill, font = eachbutton.font)

#Uses the Button Class from FinalizedTPClasses file to draw Rectangle Buttons
def createButtonRectangle(app, canvas, eachbutton): 
    canvas.create_rectangle(eachbutton.x0, eachbutton.y0, eachbutton.x1, 
    eachbutton.y1, fill = eachbutton.fill, outline = eachbutton.outline, 
    width = eachbutton.width)
    canvas.create_text(eachbutton.txtx, eachbutton.txty, text = eachbutton.text, 
    fill = eachbutton.txtfill, font = eachbutton.font)

#Creates the Complete Button which will be used in multiple screens 
def createCompleteButton(app, canvas, x0, y0, x1, y1, color, txtx, txty, 
    txt, txtcolor, font): 
    completeButton = Button(x0, y0, x1, y1, color, txtx, txty, txt, 
    txtcolor, font)
    createButtonOval(app, canvas, completeButton)

#Creates the Home Button which will be used in multiple screens 
def createHomeButton(app, canvas, x0, y0, x1, y1, color, txtx, txty, txt, 
    txtcolor, font): 
    homeButton = Button(x0, y0, x1, y1, color, txtx, txty, txt, 
    txtcolor, font)
    createButtonRectangle(app, canvas, homeButton)

################################################################################
#App Started that contains major strings, lists, and buttons throughout program

def appStarted(app): 
    app.mode = "homeScreenMode" 
    app.rows = 25 
    app.cols = 7 
    app.showtext = True
    app.showtext2 = True
    app.lastx = 0
    app.lasty = 0
    #Buttons for Home Screen Here
    app.personalInfoButton = Button(100, 325, 500, 518, "cornflowerblue", 300, 
        422, "Personal Info", "blue", "Times 50")
    app.summaryButton = Button(100, 568, 500, 780, "oldlace", 300, 674, 
        "Lifestyle Summary", "firebrick", "Times 40")
    app.calendarButton = Button(650, 325, 1100, 595, "mediumturquoise",
        875, 460, "My Calendar", "darkcyan", "Times 50") 
    app.aboutThisButton = Button(800, 645, 1100, 780, "lightpink", 950, 712,
        "About this Program", "forestgreen", "Times 35")
    #Buttons for Personal Screen Here
    app.sleepButton = Button(800, 250, 1050, 450, "blue", 925, 350, "SLEEP", 
        "black", "Times 40")
    app.completeButtonPS = Button(300, 500, 900, 750, 
        "blue", 600, 625, "COMPLETE", "black", "Times 60")
    app.homeButtonPS = Button(950, 600, 1100, 750, 
        "blue", 1025, 675, "HOME", "black", "Times 30")
    app.mealsButton = Button(150, 250, 400, 450, "blue", 275, 350, "MEALS", 
        "black", "Times 40")
    #Buttons for Sleep Screen Here
    app.homeButtonSLP = Button(950, 550, 1150, 750, "red", 1050, 650, 
        "HOME", "black", "NewRomanTimes 35")
    #Buttons for Meal Screen Here
    app.homeButtonM = Button(100, 30, 250, 180, "blue", 175, 105, "HOME", 
        "white", "Times 35")
    #Buttons for Calendar Screen Here
    app.homeButtonAP = Button(30, 30, 90, 70, "blue", 60, 50, 
        "HOME", "white", "Times 10")
    app.toDoButton = Button(130, 30, 190, 70, "blue",160, 50, "TO-DO", 
        "white", "Times 10")
    app.prevWeekButton = Button(1020, 30, 1080, 70, "blue", 1050, 50, 
        "PREV\nWEEK", "white", "Times 10")
    app.nextWeekButton = Button(1110, 30, 1170, 70, "blue", 1140, 50, 
        "NEXT\nWEEK", "white", "Times 10")
    app.deleteEventButton = Button(800, 30, 860, 70, "blue", 830, 50, 
        "DELETE\nEVENT", "white", "Times 10")
    app.addEventButton = Button(890, 30, 950, 70, "blue", 920, 50, 
        "ADD\nEVENT", "white", "Times 10")
    #Buttons for Event Input Screen 
    app.productiveWorkButton = Button(400, 200, 500, 300, "green", 450, 250, 
        "Productive\n    Work", "black", "Times 20")
    app.socializeButton = Button(550, 200, 650, 300, "red", 600, 250,
        "Socialize", "black", "Times 20")
    app.errandButton = Button(700, 200, 800, 300, "blue", 750, 250, "Errands", 
        "black", "Times 20")
    app.otherButton = Button(850, 200, 950, 300, "yellow", 900, 250, "Other", 
        "black", "Times 20")
    app.CompleteButtonEI = Button(300, 650, 400, 750, "blue", 350, 700, 
        "COMPLETE", "black", "Times 18")
    app.HomeButtonEI = Button(500, 650, 600, 750, "blue", 550, 700,
    "HOME", "black", "Times 20")
    #Buttons for About this Program screen
    app.HomeButtonATS = Button(1100, 700, 1180, 780, "blue", 1140, 740, 
        "HOME", "white", "Times 20")
    #Buttons for Delete Event Screen 
    app.deletButton = Button(300, 500, 500, 700, "blue", 400, 600, "DELETE",
        "white", "Times 30")
    app.calendarButtonDS = Button(700, 500, 900, 700, "red", 800, 600, 
        "CALENDAR", "black", "Times 30")
    #Buttons for toDO Screen 
    app.completeButtonToDo = Button(20, 20, 100, 100, "blue", 60, 60, 
    "COMPLETE", "black", "Times 13")
    app.HomeButtonToDo = Button(1100, 20, 1180, 100, "blue", 1140, 60,
    "HOME", "black", "Times 20")
    #App info for event Screen
    app.eventNameString = "Click here and type in name of your event"   
    app.eventType = ""
    app.eventStime = ""
    app.eventEtime = ""
    app.eventDay = ""
    app.eventDict = {}
    createEventDict(app)
    #App info for delete Screen
    app.deleteName = "Type in Name of Event Here"
    app.deleteDay = "Type in Day of Event Here"
    #App info for To Do Screen
    #Contains 3 strings for toDo Event Name, 3 toDo Event length of time for 
        #each event, 3 desired start time to 3 desired end time 
    app.toDoDay = ""
    app.toDoList = []
    app.toDoName1 = ""
    app.toDoName2 = ""
    app.toDoName3 = ""
    app.toDoLen1 = ""
    app.toDoLen2 = ""
    app.toDoLen3 = ""
    app.toDoStime1 = ""
    app.toDoStime2 = ""
    app.toDoStime3 = ""
    app.toDoEtime1 = ""
    app.toDoEtime2 = ""
    app.toDoEtime3 = ""
    app.toDoNameList = []
    app.toDOInfo = [(app.toDoLen1, app.toDoStime1, app.toDoEtime1), 
        (app.toDoLen2, app.toDoStime2, app.toDoEtime2), 
        (app.toDoLen3, app.toDoStime3, app.toDoEtime3)]
    app.OrigToDoDict = {}

################################################################################
#All events and redraw functions for Home Screen here 

#This creates the Home Screen    
def homeScreenMode_redrawAll(app, canvas):
    #Title of Home Screen Here 
    titleOfProgram = Screens(600, 60, "Live, Laugh, & Love Yourself", "blue",
    "TimesNewRoman 75 bold")
    titleOfProgram.createTitle(app, canvas)
    #Directions of Home Screen Here
    homeScreenDir = """\tWelcome to Live, Laugh, & Love Yourself!!! In this 
    program, you will be able to plan a healthy and well-balanced lifestyle so 
    you learn to live, laugh, and love your days. Please click on buttons below
    to reach associated categories. For more information regarding this program, 
    please click the 'About this Program' button. Enjoy!!!"""
    dirOfHomeScreen = Screens(600, 210, homeScreenDir, "black", 
    "TimesNewRoman 30 italic")
    dirOfHomeScreen.createDir(app, canvas)
    # Personal Info Buttons here
    personalInfoButton = Button(100, 325, 500, 518, "cornflowerblue", 300, 
        422, "Personal Info", "blue", "Times 50")
    createButtonOval(app, canvas, personalInfoButton)
    # SummaryButton Here
    summaryButton = Button(100, 568, 500, 780, "oldlace", 300, 674, 
        "Lifestyle Summary", "firebrick", "Times 40")
    createButtonOval(app, canvas, summaryButton)
    # Calendar Button Here
    calendarButton = Button(650, 325, 1100, 595, "mediumturquoise",
        875, 460, "My Calendar", "darkcyan", "Times 50") 
    createButtonOval(app, canvas, calendarButton)
    # About this Program Button Here
    aboutThisButton = Button(800, 645, 1100, 780, "lightpink", 950, 712,
        "About this Program", "forestgreen", "Times 35")
    createButtonOval(app, canvas, aboutThisButton)

#Mouse Pressed Function for the Home Screen
def homeScreenMode_mousePressed(app, event):
    if app.aboutThisButton.buttonClicked(event.x, event.y): 
        app.mode = "aboutThisProgramScreenMode"
        getAvailibleTimes(app)
    if app.personalInfoButton.buttonClicked(event.x, event.y): 
        app.mode = "personalScreenMode"
    if app.summaryButton.buttonClicked(event.x, event.y): 
        app.mode = "summaryScreenMode"
    if app.calendarButton.buttonClicked(event.x, event.y): 
        app.mode = "calendarScreenMode"

################################################################################
#All events and redraw functions for Personal Screen here 

#This creates/draws the Personal Screen
def personalScreenMode_redrawAll(app, canvas): 
    #Title of Personal Screen Here
    titleOfPersonalScreen = Screens(600, 50, "Personal Lifestyle", "blue", 
    "TimesNewRoman 60 bold")
    titleOfPersonalScreen.createTitle(app, canvas)
    #Directions of Personal Screen Here
    personalInfoDir = """\tClick on each button and record your personal 
    information for each category. If you have other weekly or repeated 
    schedules that are not in these categories, store them in the 'other'
    category. Once you're done, click the 'Complete' button."""
    dirOfPersonalScreen = Screens(600, 170, personalInfoDir, "black", 
    "TimesNewRoman 30 italic")
    dirOfPersonalScreen.createDir(app, canvas)
    #Meals Button Here
    mealsButton = Button(150, 250, 400, 450, "blue", 275, 350, "MEALS", 
    "black", "Times 40")
    createButtonRectangle(app, canvas, mealsButton)
    #Fitness Button Here
    fitnessButton = Button(475, 250, 725, 450, "blue", 600, 350, "FITNESS", 
    "black", 'Times 35')
    createButtonRectangle(app, canvas, fitnessButton)
    #Sleep Button Here
    sleepButton = Button(800, 250, 1050, 450, "blue", 925, 350, "SLEEP", 
        "black", "Times 40")
    createButtonRectangle(app, canvas, sleepButton)
    #Complete Button Here
    createCompleteButton(app, canvas, 300, 500, 900, 750, "blue", 600, 625, 
        "COMPLETE", "black", "Times 60")
    #Creates the Back to Home Page Button 
    createHomeButton(app, canvas, 950, 600, 1100, 750, "blue", 1025, 675,
        "HOME", "black", "Times 30")

#Mouse Pressed Function for Personal Screen Here
def personalScreenMode_mousePressed(app, event): 
    if app.homeButtonPS.buttonClicked(event.x, event.y): 
        app.mode = "homeScreenMode"
    if app.sleepButton.buttonClicked(event.x, event.y): 
        app.mode = "sleepScreenMode"
    if app.mealsButton.buttonClicked(event.x, event.y): 
        app.mode = "mealsScreenMode"

################################################################################
#All events and redraw functions for Sleep Screen Here

#This creates the Screen for users to implement sleep schedules
def sleepScreenMode_redrawAll(app, canvas): 
    #Title of the Sleep Screen Here
    titleOfSleep = Screens(600, 60, "SLEEP SCHEDULE", "black", 
    "TimesNewRoman 40")
    titleOfSleep.createTitle(app, canvas)
    #Directions of Sleep Schedule Screen Here 
    dirOfSleepInfo = """\tPlease type in your daily sleep schedule in 24-Hour 
    Time form. Once completely done, please click on the 'COMPLETE' 
    button below. Click on the 'HOME' button to return to the home screen."""
    dirOfSleepScreen = Screens(600, 150, dirOfSleepInfo, "black", 
    "TimesNewRoman 30")
    dirOfSleepScreen.createDir(app, canvas)
    #Each day of the week here
    monday = Screens(150, 250, "MONDAY:", "black", "TimesNewRoman 30")
    monday.createRandomWords(app, canvas)
    tuesday = Screens(150, 350, "TUESDAY:", "black", "TimesNewRoman 30")
    tuesday.createRandomWords(app, canvas)
    wednesday = Screens(150, 450, "WEDNESDAY:", "black", "TimesNewRoman 30")
    wednesday.createRandomWords(app, canvas)
    thursday = Screens(150, 550, "THURSDAY:", "black", "TimesNewRoman 30")
    thursday.createRandomWords(app, canvas)
    friday = Screens(150, 650, "FRIDAY:", "black", "TimesNewRoman 30")
    friday.createRandomWords(app, canvas)
    saturday = Screens(750, 250, "SATURDAY:", "black", "TimesNewRoman 30")
    saturday.createRandomWords(app, canvas)
    sunday = Screens(750, 350, "SUNDAY:", "black", "TimesNewRoman 30")
    sunday.createRandomWords(app, canvas)
    #Creates the word "to" for each day
    for i in range(7): 
        if i > 4:
            dx = 1000
            dy = 250 + ((i % 5) * 100)
        else: 
            dx = 400
            dy = 250 + (i * (100))
        to = Screens(dx, dy, "to", "black", "TimesNewRoman 30")
        to.createRandomWords(app, canvas)
    #Creates the line of the sleep Screen 
    for n in range(7):
        if n > 4: 
            dy = 270 + ((n % 5) * (100))
            canvas.create_line(850, dy, 950, dy, fill = "black", width = 5)
            canvas.create_line(1050, dy, 1150, dy, fill = "black", width = 5) 
        else:   
            dy = 270 + (n * 100)
            canvas.create_line(250, dy, 350, dy, fill = "black", width = 5 )
            canvas.create_line(450, dy, 550, dy, fill = "black", width = 5)
    #Create the Complete Button Here
    createCompleteButton(app, canvas, 700, 400, 900, 600, "green", 800, 500, 
        "COMPLETE", "black", "NewRomanTimes 35")
    #Create the back to Home Button Here
    createHomeButton(app, canvas, 950, 550, 1150, 750, "red", 1050, 650, 
        "HOME", "black", "NewRomanTimes 35")

#Mouse Pressed for Sleep Screen Here
def sleepScreenMode_mousePressed(app, event): 
    if app.homeButtonSLP.buttonClicked(event.x, event.y): 
        app.mode = "homeScreenMode"

################################################################################
#All events and redraw functions for Meals Screen Here

#This creates the Screen for users to implement their meal times daily
def mealsScreenMode_redrawAll(app, canvas): 
    #Title of Meals Screen Here
    titleOfMeals = Screens(600, 50, "MEAL SCHEDULES", "black", 
        "TimesNewRoman 50")
    titleOfMeals.createTitle(app, canvas)
    #Create the Home Button Here
    createHomeButton(app, canvas, 100, 30, 250, 180, "blue", 175, 105, "HOME", 
        "white", "Times 35")
    #Create the characteristics of this page
    mealsList = ["Breakfast", "Lunch", "Dinner"]
    dx = 0 
    for i in range(3): 
        meal = mealsList[0]
        if i == 0: 
            dx += 400
        else: 
            dx += 300
        canvas.create_text(dx, 150, text = meal, fill = "black", 
            font = "Times 40")
        mealsList = mealsList[1:]
    weekdayList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
    "Friday", "Saturday"]
    dy = 0
    for n in range(7): 
        day = weekdayList[0] 
        if n == 0: 
            dy += 220
        else: 
            dy += 80
        canvas.create_text(100, dy, text = day, fill = "black", 
                font = "Times 40")
        weekdayList = weekdayList[1:]
    for m in range(21): 
        if m % 7 == 0: 
            dy = 220
        else: 
            dy += 80 
        if m <= 6: 
            dx = 400
        elif m > 6 and m < 14: 
            dx = 700 
        else: 
            dx = 1000
        canvas.create_text(dx, dy, text = "to", fill = "black", 
            font = "Times 40")
    ldx0 = 0
    ldy = 0
    for each in range(14):
        if each % 7 == 0: 
            ldy = 240
        else: 
            ldy += 80 
        if each < 7: 
            ldx0 = 300
        elif each >= 7 and each < 14: 
            ldx0 = 430
        elif each >= 14 and each < 21: 
            ldx0 = 480
        elif each >= 21 and each < 28: 
            ldx0 = 610
        ldx1 = ldx0 + 70
        canvas.create_line(ldx0, ldy, ldx1, ldy, fill = "black", width = 5)

#Mouse Pressed Function for Meals Screen
def mealsScreenMode_mousePressed(app, event): 
    if app.homeButtonM.buttonClicked(event.x, event.y): 
        app.mode = "homeScreenMode"

################################################################################
#All events and redraw functions for Calendar Screen Here

#This creates the calendar screen         
def calendarScreenMode_redrawAll(app, canvas): 
    # Title of Calendar Screen Here
    titleOfCalendar = Screens(600, 50, "CALENDAR", "black", "TimesNewRoman 50")
    titleOfCalendar.createTitle(app, canvas)
    #Creates the Home Button Here
    createHomeButton(app, canvas, 30, 30, 90, 70, "blue", 60, 50, "HOME", 
        "white", "Times 10")
    #To-Do List Button Here
    toDoButton = Button(130, 30, 190, 70, "blue",160, 50, "TO-DO", 
        "white", "Times 10")
    createButtonRectangle(app, canvas, toDoButton)
    #Previous Week Button Here 
    prevWeekButton = Button(1020, 30, 1080, 70, "blue", 1050, 50, "PREV\nWEEK", 
        "white", "Times 10")
    createButtonRectangle(app, canvas, prevWeekButton)
    #Delete Event Button Here
    deleteEventButton = Button(800, 30, 860, 70, "blue", 830, 50, 
        "DELETE\nEVENT", "white", "Times 10")
    createButtonRectangle(app, canvas, deleteEventButton)
    #Next Week Button Here 
    nextWeekButton = Button(1110, 30, 1170, 70, "blue", 1140, 50, "NEXT\nWEEK", 
        "white", "Times 10")
    createButtonRectangle(app, canvas, nextWeekButton)
    #Add Event Button Here
    addEventButton = Button(890, 30, 950, 70, "blue", 920, 50, 
        "ADD\nEVENT", "white", "Times 10")
    createButtonRectangle(app, canvas, addEventButton)
    #Draws the calendar here
    canvas.create_line(0, 150, 1200, 150, fill = "black", width = 5)
    WeekList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday"]
    fontx = 0 
    for i in range(7):
        day = WeekList[0] 
        if i == 0: 
            fontx += 85
        else: 
            fontx += 171
        canvas.create_text(fontx, 175, text = day, fill = "black", 
            font = "Times 20")
        WeekList = WeekList[1:]
    for each in range(7): 
        dx = (171 * each)
        canvas.create_line(dx, 150, dx, 800, fill = "black", width = 5)
    canvas.create_line(0, 200, 1200, 200, fill = "black", width = 5)
    drawEvents(app, canvas)

#Draws all the events in app.EventDict in the Calendar
def drawEvents(app, canvas):
    Weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday"] 
    colorDict = {"productiveWork" : "green", "socialize" : "red", 
        "errand" : "blue", "other" : "yellow", "toDo" : "orange"}
    for eachDL in app.eventDict: 
        for event in app.eventDict[eachDL]:
            x0 = Weekdays.index(eachDL) * (app.width / 7)
            x1 = (x0 + app.width / 7)
            y0 = 200 + 25*(event[2])
            y1 = 200 + 25*(event[3])
            colorDict[event[1]]
            canvas.create_rectangle(x0, y0, x1, y1, 
                fill = colorDict[event[1]])
            stime = event[2]
            etime = event[3]
            txt = (f"{event[0]} {stime} to {etime}")
            txtx = (x0 + x1)/2
            txty = (y0 + y1)/2
            canvas.create_text(txtx, txty, text = txt, fill = "black", 
                font = "Times 10")

#Mouse Pressed Function for Calendar Screen
def calendarScreenMode_mousePressed(app, event):
    if app.homeButtonAP.buttonClicked(event.x, event.y):
        app.mode = "homeScreenMode"
    if app.toDoButton.buttonClicked(event.x, event.y): 
        app.mode = "toDoInputScreenMode"
    if app.deleteEventButton.buttonClicked(event.x, event.y): 
        app.mode = "deleteEventScreenMode"
    if app.addEventButton.buttonClicked(event.x, event.y): 
        app.mode = "eventInputScreenMode"

################################################################################
#All events and redraw functions for Event Input Screen Here

#This creates the event input screen
def eventInputScreenMode_redrawAll(app, canvas): 
    #Title of Events Page
    titleOfEventInput = Screens(600, 60, "EVENT INPUT", "black", "Times 50")
    titleOfEventInput.createTitle(app, canvas)
    #Line where Users can type in the name of their Event
    canvas.create_line(200, 170, 1000, 170, fill = "black", width = 5)
    dirOfEventsName = Screens(600, 150, app.eventNameString, "black", 
        "Times 40")
    dirOfEventsName.createVanishWords(app, canvas)
    #Types of Events Categories/Buttons
    selectTypeInfo = Screens(200, 250, 
        "Select the Category of Your Event:", fill = "black", font = "Times 25")
    selectTypeInfo.createRandomWords(app, canvas)
    productiveWorkButton = Button(400, 200, 500, 300, "green", 450, 250, 
        "Productive\n    Work", "black", "Times 20")
    createButtonRectangle(app, canvas, productiveWorkButton)
    socializeButton = Button(550, 200, 650, 300, "red", 600, 250, "Socialize", 
        "black", "Times 20")
    createButtonRectangle(app, canvas, socializeButton)
    errandButton = Button(700, 200, 800, 300, "blue", 750, 250, "Errands", 
        "black", "Times 20")
    createButtonRectangle(app, canvas, errandButton)
    otherButton = Button(850, 200, 950, 300, "yellow", 900, 250, "Other", 
        "black", "Times 20")
    createButtonRectangle(app, canvas, otherButton)
    #Time of the Events
    canvas.create_text(200, 380, text = "TIME:", fill = "black", 
        font = "Times 50")
    canvas.create_line(300, 400, 450, 400, fill = "black", width = 5)
    startT = Screens(375, 370, app.eventStime, fill = "black",
        font = "Times 40")
    startT.createRandomWords(app, canvas)
    canvas.create_text(500, 380, text = "to", fill = "black", font = "Times 50")
    canvas.create_line(550, 400, 700, 400, fill = "black", width = 5)
    endT = Screens(625, 370, app.eventEtime, fill = "black", font = "Times 40")
    endT.createRandomWords(app, canvas)
    timeDirInfo = """Click above the two lines and type in your event's start to 
                       finish time inf 24 hour form"""
    timeDir = Screens(430, 450, timeDirInfo, fill = "black", font = "Times 20")
    timeDir.createDir(app, canvas)
    canvas.create_text(200, 550, text = "DAY:", fill = "black", 
        font = 'Times 50')
    canvas.create_line(300, 570, 700, 570, fill = "black", width = 5)
    daytxt = Screens(500, 540, app.eventDay, fill = "black", 
        font = "Times 40")
    daytxt.createRandomWords(app, canvas)
    dayDirInfo = """      Click in the space above the line and type in the 
    day of the week the event is supposed to happen on"""
    dayDir = Screens(430, 610, dayDirInfo, fill = "black", font = "Times 20")
    dayDir.createDir(app, canvas)
    #Complete Button
    createCompleteButton(app, canvas, 300, 650, 400, 750, "blue", 350, 700, 
    "COMPLETE", "black", "Times 18")
    #Creates the Back to Home Page Button 
    createHomeButton(app, canvas, 500, 650, 600, 750, "blue", 550, 700,
    "HOME", "black", "Times 20")
    complOrExitInfo = """Once you've completed with inputing\nyour information,
        click on the 'COMPLETE' Button.\nIf not, please click the home button 
        to return to the home page."""
    complOrExitDir = Screens(950, 650, complOrExitInfo, fill = "black", 
        font = "Times 25")
    complOrExitDir.createDir(app, canvas)

#Mouse Pressed Function for Event Inut Screen
#app.lastx and app.lasty idea where the mouse event is recorded was provided by
    #Professor Taylor 
def eventInputScreenMode_mousePressed(app, event): 
    app.lastx = event.x 
    app.lasty = event.y
    x = event.x 
    y = event.y
    if app.HomeButtonEI.buttonClicked(event.x, event.y): 
        app.mode = "homeScreenMode"
        app.eventNameString = "Click here and type in name of your event"
        app.eventType = ""
        app.eventEtime = ""
        app.eventStime = ""
        app.eventDay = ""
    if (x >= 200 and x <= 1000 and y >= 120 and y <= 170 and 
    app.eventNameString == "Click here and type in name of your event") : 
        app.showtext = False
        app.eventNameString = " "
    if x >= 200 and x <= 1000 and y >= 120 and y <= 170: 
        app.eventNameString = ""
        app.lastx = x
        app.lasty = y
    if app.productiveWorkButton.buttonClicked(event.x, event.y): 
        app.eventType = "productiveWork"
#Add to workOrSchoolList 
    if app.socializeButton.buttonClicked(event.x, event.y): 
        app.eventType = "socialize"
#Add to socialize List
    if app.errandButton.buttonClicked(event.x, event.y): 
        app.eventType = "errand"
#Add to errend List
    if app.otherButton.buttonClicked(event.x, event.y): 
        app.eventType = "other"
    if (app.CompleteButtonEI.buttonClicked(event.x, event.y) 
            and eventInfoLegal(app)): 
        newEvent = Event(app.eventNameString, app.eventType, app.eventStime, 
            app.eventEtime, app.eventDay)
        # getAvailibleTimes(app)
        addEventtoDic(app, newEvent)

#Key Press Function Event Input Screen 
def eventInputScreenMode_keyPressed(app, event): 
    #Key Press for Start Time
    if (app.lastx >= 300 and app.lastx <= 450 and app.lasty >= 360 
        and app.lasty <= 400):
        if event.key == "Space": 
                    app.eventStime += "  "
        elif event.key == "BackSpace": 
                app.eventStime = app.eventStime[:-1]
        else:  
            app.eventStime += (event.key)
    #Key Press for End Time
    elif(app.lastx >= 550 and app.lastx <= 700 and app.lasty >= 360 and 
        app.lasty <= 400) :
        if event.key == "Space": 
                    app.eventEtime += "  "
        elif event.key == "BackSpace": 
                app.eventEtime = app.eventEtime[:-1]
        else:  
            app.eventEtime += (event.key)
    elif (app.lastx >= 300 and app.lastx <= 700 and app.lasty >= 530 and 
        app.lasty <= 570):
        if event.key == "Space": 
                    app.eventDay += "  "
        elif event.key == "BackSpace": 
                app.eventDay = app.eventDay[:-1]
        else:  
            app.eventDay += (event.key)
    else:  
        app.showtext = True
        if event.key == "Space": 
                    app.eventNameString += "  "
        elif event.key == "BackSpace": 
                app.eventNameString = app.eventNameString[:-1]
        else:  
            app.eventNameString += (event.key)

#Creates app.eventDict for Event Input Screen that's also in appStarted
def createEventDict(app): 
    Weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday"]
    for day in Weekdays: 
        app.eventDict[day] = []

#Checks if user clicks on a TYPE button in app.EventDict and checks the 
    #type of the events inputted
def eventTypeDefined(app):
    if (app.eventType == "productiveWork" or 
    app.eventType == "socialize" or app.eventType == "errand" or 
    app.eventType == "other" or app.eventType == "toDo"): 
        return True

#Checks if the time entered in Event Input is Legal
def timeEnteredIsLegal(app): 
    if (not isinstance(app.eventStime, int) and  
        not isinstance(app.eventEtime, int)):
        if app.eventStime.isdigit() and app.eventEtime.isdigit():
            app.eventStime = int(app.eventStime)
            app.eventEtime = int(app.eventEtime)
    if (app.eventStime >= 0 and app.eventEtime <= 24 and 
    app.eventStime < app.eventEtime): 
                return True 
    else: 
        return False

#Checks if inputted info are legal for Event Input Screen
def eventInfoLegal(app): 
    Weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
    "Friday", "Saturday"]
    if (app.eventNameString != " " and eventTypeDefined(app) and 
    timeEnteredIsLegal(app) and app.eventDay in Weekdays): 
        newEvent = Event(app.eventNameString, app.eventType, app.eventStime, 
            app.eventEtime, app.eventDay)
        someEvent = (app.eventNameString, app.eventType, app.eventStime, 
            app.eventEtime, app.eventDay)
        addEventtoDic(app, someEvent)
    #Checks that if all information is legal (through timeEnteredIsLegal and 
        #eventTypeDefined then the event will be added to app.eventDict

#Adds event to app.eventDict and called through EventInput mouse pressed 
    #when Complete Button is clicked
#Used and done in and if eventInfoLegal 
def addEventtoDic(app, someEvent): 
    app.eventDict[app.eventDay].append(someEvent)
    return app.eventDict

################################################################################
#All events and redraw functions for About this Program Screen Here

#This creates the About this Program Screen that contains all directions about
    #this program
def aboutThisProgramScreenMode_redrawAll(app, canvas): 
    #Title of About this Program Here 
    titleOfAboutThis = Screens(600, 30, "ABOUT THIS PROGRAM", "black", 
        "Times 40")
    titleOfAboutThis.createTitle(app, canvas)
    #Creates the Home Button Here
    createHomeButton(app, canvas, 1100, 700, 1180, 780, "blue", 1140, 740, 
        "HOME", "white", "Times 20")
    #Subtitles of Each Section Here
    subTitHome = Screens(150, 60, "Home Screen Instructions", "black", 
        "Times 20")
    subTitHome.createTitle(app, canvas)
    perTit = Screens(150, 130, "Personal Screen Instructions", "black", 
        "Times 20")
    perTit.createTitle(app, canvas)
    calTit = Screens(150, 265, "Calendar Screen Instructions", "black", 
        "Times 20")
    calTit.createTitle(app, canvas)
    sumTit = Screens(150, 505, "Summary Screen Instructions", "black", 
        "Times 20")
    sumTit.createTitle(app, canvas)
    toDoTit = Screens(150, 625, "TO-DO List Screen Instructions", "black", 
        "Times 20")
    toDoTit.createTitle(app, canvas)
    addEventTit = Screens(750, 80, "Add Event Screen Instructions", "black",
        "Times 20")
    addEventTit.createTitle(app, canvas)
    mealsTit = Screens(750, 270, "Meals Screen Instructions", "black", 
        "Times 20")
    mealsTit.createTitle(app, canvas)
    sleepTit = Screens(750, 425, "Sleep Screen Instructions", "black", 
        "Times 20")
    sleepTit.createTitle(app, canvas) 
    fitnessTit = Screens(750, 580, "Fitness Screen Instructions", "black", 
        "Times 20")  
    fitnessTit.createTitle(app, canvas)
    errorTit = Screens(550, 755, "*Error Alerts:", "black", "Times 20")
    errorTit.createTitle(app, canvas)
    #Instructions of Each Section Here
    homeScreenInstructxt = """
    Each Button is associated to a different sectionof this program. 
    Simply click on the buttons to view the other sections."""
    homeScreenInstruc = Screens(200, 80, homeScreenInstructxt, "black", 
        "Times 15")
    homeScreenInstruc.createDir(app, canvas)
    perScreenInstructxt = """
    The Personal Information Page contains three buttons that leads to three 
    categories were users can input information regarding their personal habits
    associated to each button category.It includes the 'Fitness Category', 
    'Sleep Category', and 'Meals Category'. To access each category, simply 
    click on the buttons. Alerts for each category will show up if the user's 
    lifestyle habits doesn't meet the program's standards."""
    perScreenInstruc = Screens(235, 187, perScreenInstructxt, "black", 
        "Times 15")
    perScreenInstruc.createDir(app, canvas)
    calScreenInstructxt = """
    Unlike regular calendars, in this calendar you won't be able to input 
    informations and events by clicking on the calendar itself. Instead, you 
    must click on the 'ADD EVENT' button to add events to the calendar and 
    'DELETE EVENT button to delete events on the calendar. Clicking on the 
    'PREVIOUS WEEK' button will change the calendar dates to the days of the 
    previous week and clicking on the 'NEXT WEEK' button will change the 
    calendar dates to the days of the next week. The 'HOME' button will bring
    users back to the home page and the 'TO-DO' button will lead users to a page
    that allows them to input the name of the event that must be done, the 
    length of time it takes for the event to occur, and the range of time the 
    user hopes to get this event done by. Clicking on the 'HOME' button will
    bring the users back to the home screen"""
    calScreenInstruc = Screens(245, 375, calScreenInstructxt, "black", 
        "Times 15")
    calScreenInstruc.createDir(app, canvas)
    sumScreentxt = """
    Users usually don't do or input anything in the Summary. The purpose of the 
    Summary Screen is so the program can give users a summary of how many hours 
    of sleep, exercise, work, and socializing they've done during the week.
    Clicking on the 'HOME' button users will be brought back to the home 
    screen."""
    sumScreenInstruc = Screens(260, 555, sumScreentxt, "black", "Times 15")
    sumScreenInstruc.createDir(app, canvas)
    toDoScreenInstructxt = """
    As described in the Calendar Screen Instructions, the To-Do screen will 
    allow users to input a certain number of tasks the users want to get done
    in a certain time frame but finds difficult to plan out. This section of 
    the program assists the users by creating finding times that'll work for 
    both the users and their schedule. An Error alert will show up if any sort
    of wrong information was inputted or if the user tries to complete the list
    without actually adding anything to the list. """
    toDoScreenInstruc = Screens(225, 690, toDoScreenInstructxt, "black", 
        "Times 15")
    toDoScreenInstruc.createDir(app, canvas)
    addEventInstructxt = """
    The Add Event Screen is the screen that allows users to input their daily
    tasks and events. Users must first type in the name of the event they're 
    trying to input and then select a category the event falls under. The user
    will then have to input the start and finish time of the event in 24 hour 
    form. After typing in the day of the week the user wants the event to occur 
    on, the user can then click on the 'COMPLETE' button so the event can 
    actually be added to their calendar. An Error alert will show up if anything
    in the input was incomplete or wrong. Alerts will also show if there's a 
    schedule overlap."""
    addEventInstruc = Screens(800, 165, addEventInstructxt, "black", 
        "Times 15")
    addEventInstruc.createDir(app, canvas)
    mealsScreenInstructxt = """
    The Meals Screen allows users to input their breakfast, lunch, and dinner 
    times. A healthy individual needs three meals a day so not meeting such 
    requirement would result in an alert and users will therefore be unable to 
    proceed further into the program. The purpose of this program is to  
    enforce its users to live a healthy and well-balanced lifestyle so in 
    this section, users must implement three different times 
    for three meals a day."""
    mealsScreenInstruc = Screens(800, 335, mealsScreenInstructxt, "black", 
        "Times 15")
    mealsScreenInstruc.createDir(app, canvas)
    sleepScreenInstructxt = """
    The Sleep Screen allows users to input their different sleep schedules for
    different days of the week. A healthy individual would need a certain 
    number of hours of sleep per night so not meeting such requirements 
    would result in an alert and users will therefore be unable to proceed 
    further into the program. The purpose of this program is to enforce its 
    users to live a healthy and well-balanced lifestyle so in this section,
    users must meet a certain number of sleep hours. """
    sleepScreenInstruc = Screens(800, 495, sleepScreenInstructxt, "black", 
        "Times 15")
    sleepScreenInstruc.createDir(app, canvas)
    fitnessScreenInstructxt = """
    The Fitness Screen allows users to input times where users plan to work out
    or exercise. Because a healthy individual would need a certain number of 
    hours of exercise hours per week, not meeting such requirements would also 
    result in an alert and users will therefore be unable to proceed further 
    into the program without meeting such requirements. The purpose of this 
    program is to enforce its users to live a healthy and well-balanced 
    lifestyle so in this section, users must meet a certain number of fitness 
    hours."""
    fitnessScreenInstruc = Screens(800, 655, fitnessScreenInstructxt, "black", 
        "Times 15")
    fitnessScreenInstruc.createDir(app, canvas)
    errorMessagetxt = """
    Error messages usually show if information regarding a certain category is
    not fufilled or incorrect(doesn't make sense). When this occurs, please be 
    sure to go back and fix it."""
    errorMessageInstruc = Screens(850, 750, errorMessagetxt, "black",
        "Times 15")
    errorMessageInstruc.createDir(app, canvas)  

#Mouse Pressed Function for About this Program Screen
def aboutThisProgramScreenMode_mousePressed(app, event): 
    if app.HomeButtonATS.buttonClicked(event.x, event.y): 
        app.mode = "homeScreenMode"

################################################################################
#All events and redraw functions for Delete Event Screen Here

def deleteEventScreenMode_redrawAll(app, canvas): 
    #Create Title of Delete Event Page Here
    titOfDelete = Screens(600, 50, "DELETE EVENT", "black", "Times 40")
    titOfDelete.createTitle(app, canvas)
    #Create Directions of Delete Event Page Here
    dirOfDeletetxt = """
    In order to delete an already existing event on the calendar, please type in
    the name of the event, the day the event is supposed to occur on, and click
    the delete button. Once you've clicked on the 'DELETE' button, please click 
    onthe 'CALENDAR' button to return to the calendar. If an error message 
    occurs, that means there's something wrong with the information you've 
    inputted. To reschedule an event, please delete the event first and then 
    schedule the event again with the correct information this time through the 
    Event Input Screen."""
    dirOfDelete = Screens(600, 170, dirOfDeletetxt, "black", "Times 20")
    dirOfDelete.createDir(app, canvas)
    #Creates the lines for name and day input
    canvas.create_line(300, 340, 900, 340, fill = "black", width = 5)
    deleteName = Screens(600, 310, app.deleteName, fill = "black", 
        font = "Times 40")
    deleteName.createVanishWords(app, canvas)
    canvas.create_line(300, 440, 900, 440, fill = "black", width = 5)
    deleteDay = Screens(600, 410, app.deleteDay, fill = "black", 
        font = "Times 40")
    deleteDay.createVanishWords2(app, canvas)
    deletButton = Button(300, 500, 500, 700, "blue", 400, 600, "DELETE",
        "white", "Times 30")
    createButtonOval(app, canvas, deletButton)
    calendarButton = Button(700, 500, 900, 700, "red", 800, 600, "CALENDAR", 
        "black", "Times 30")
    createButtonOval(app, canvas, calendarButton)

#Mouse Pressed Function for Delete Event Screen
def deleteEventScreenMode_mousePressed(app, event):
    x = event.x 
    y = event.y
    if (x >= 300 and x <= 900 and y >= 300 and y <= 340 and 
            app.deleteName == "Type in Name of Event Here"): 
        app.showtext = False 
        app.deleteName = ""
        app.lastx = x
        app.lasty = y
    elif (x >= 300 and x <= 900 and y >= 400 and y <= 440 and
           app.deleteDay == "Type in Day of Event Here"): 
        app.showtext2 = False
        app.deleteDay = ""
        app.lastx = x
        app.lasty = y
    elif app.deletButton.buttonClicked(event.x, event.y): 
        deleteEventfromDict(app)
    elif app.calendarButtonDS.buttonClicked(event.x, event.y): 
        app.mode = "calendarScreenMode"
        app.deleteDay = "Type in Day of Event Here"
        app.deleteName = "Type in Name of Event Here"

#Key Pressed Function for Delete Event Screen Here
def deleteEventScreenMode_keyPressed(app, event): 
    if (app.lasty >= 300 and app.lasty <= 340): 
            app.showtext = True 
            if event.key == "BackSpace": 
                app.deleteName = app.deleteName[:-1]
            elif event.key == "Space": 
                app.deleteName += " "
            else: 
                app.deleteName += (event.key)
    elif (app.lasty >= 400 and app.lasty <= 440): 
        app.showtext2 = True
        if event.key == "BackSpace": 
                app.deleteDay = app.deleteDay[:-1]
        elif event.key == "Space": 
            app.deleteDay += " "
        else: 
            app.deleteDay += (event.key)

#Checks if the information being deleted is Legal and found in calendar
#Helper function for deleteEventfromDict
def deleteInfoLegal(app):
    Weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
    "Friday", "Saturday"]
    if app.deleteDay not in Weekdays: 
        return False
    NameList = []
    for event in app.eventDict[app.deleteDay]: 
        NameList.append(event[0])
    if app.deleteName not in NameList: 
        return False
    else: 
        return True

#Deletes the Events from a Calendar by deleting from app.eventDict
#Uses helper function deleteInfoLegal
def deleteEventfromDict(app):
    if deleteInfoLegal(app):
        for event in app.eventDict[app.deleteDay]:
            if event[0] == app.deleteName: 
                app.eventDict[app.deleteDay].remove(event)

################################################################################
#All events and redraw functions for To Do Screen Here

#Draws the To Do List Input Screen Here
def toDoInputScreenMode_redrawAll(app, canvas): 
    #Create the title of the Screen
    titOfToDo = Screens(600, 50, "TO DO LIST", "black", "Times 50")
    titOfToDo.createTitle(app, canvas)
    #Create the directions of this screen here
    dirOfToDotxt = """
    Add a max of 3 events you want to schedule in your calendar by typing in
    the name of the event, the length of time it takes to perform your event,
    and the desired range time you want you event to occur in."""
    dirOfToDo = Screens(600, 100, dirOfToDotxt, "black", "Times 25")
    dirOfToDo.createDir(app, canvas)
    dayTxtDir = """
    Please type in the Weekday you want to 
    schedule your events to be scheduled in here"""
    dayDir = Screens(300, 200, dayTxtDir, "black", "Times 25")
    dayDir.createDir(app, canvas)
    #Create the toDo event Day here 
    canvas.create_line(600, 230, 900, 230, fill = "black", width = 5)
    toDoDay = Screens(750, 210, app.toDoDay, "black", "Times 30")
    toDoDay.createRandomWords(app, canvas)
    #Create category names 
    toDoName = Screens(130, 300, "Name of Event", "black", "Times 30")
    toDoName.createRandomWords(app, canvas)
    toDoLength = Screens(400, 300, "Time Length of Event\n (in hours)", 
        "black", "Times 30")
    toDoLength.createRandomWords(app, canvas)
    sRange = Screens(700, 300, "Event Desire Time\nRange Start", "black", 
        "Times 30")
    sRange.createRandomWords(app, canvas)
    eRange = Screens(1000, 300, "Event Desire Time\n Range End", "black", 
        "Times 30")
    eRange.createRandomWords(app, canvas)
    starty = 400
    for numb in range(3): 
        if numb == 0: 
            canvas.create_text(30, starty, text = str(numb + 1) + ":", 
                fill = "black", font = "Times 30")
        else: 
            canvas.create_text(30, (starty + numb * 150), 
                text = str(numb + 1) + ":", fill = "black", font = "Times 30") 
    #Lines for toDo Event Name
    namesList = [app.toDoName1, app.toDoName2, app.toDoName3]
    for i in range(3): 
        dx = 50
        dx1 = dx + 200
        if i == 0: 
            dy = 450
        else: 
            dy += 150
        canvas.create_line(dx, dy, dx1, dy, fill = "black", width = 5)
    namedy = 320
    namedx = (dx + dx1)/2
    for i in range(3): 
        if i == 0:
            namedy += 100
        else: 
            namedy += 150
        canvas.create_text(namedx, namedy, text = namesList[i], fill = "black", 
            font = "Times 40")
    # Lines for toDo Event Length of Time
    toDoLenList = [app.toDoLen1, app.toDoLen2, app.toDoLen3]
    for i in range(3): 
        dxl = 330
        dxl1 = dxl + 150
        if i == 0: 
            dy = 450
        else: 
            dy += 150
        canvas.create_line(dxl, dy, dxl1, dy, fill = "black", width = 5)
    lendy = 320
    lendx = (dxl + dxl1)/2
    for i in range(3): 
        if i == 0: 
            lendy += 100
        else: 
            lendy +=150
        canvas.create_text(lendx, lendy, text = toDoLenList[i], fill = "black", 
            font = "Times 40")
    #Lines for toDo Event Start Desire Time
    sTimeDesList = [app.toDoStime1, app.toDoStime2, app.toDoStime3]
    for i in range(3): 
        dxs = 630
        dxs1 = dxs + 150
        for i in range(3): 
            if i == 0: 
                dy = 450
            else: 
                dy += 150
            canvas.create_line(dxs, dy, dxs1, dy, fill = "black", width = 5)
    stimedy = 320
    stimedx = (dxs + dxs1)/2
    for i in range(3): 
        if i == 0: 
            stimedy += 100
        else: 
            stimedy += 150
        canvas.create_text(stimedx, stimedy, text = sTimeDesList[i],
            fill = "black", font = "Times 40")
    #Lines for toDo Event End Desire Time
    eTimeList = [app.toDoEtime1, app.toDoEtime2, app.toDoEtime3]
    for i in range(3): 
        dxe = 930
        dxe1 = dxe + 150
        for i in range(3):
            if i == 0 : 
                dy = 450
            else: 
                dy += 150
            canvas.create_line(dxe, dy, dxe1, dy, fill = "black", width = 5)
    etimedy = 320 
    etimedx = (dxe + dxe1)/2
    for i in range(3): 
        if i == 0: 
            etimedy += 100 
        else: 
            etimedy += 150
        canvas.create_text(etimedx, etimedy, text = eTimeList[i], 
            fill = "black", font = "Times 40")
    #Create the Buttons Here 
    createCompleteButton(app, canvas, 20, 20, 100, 100, "blue", 60, 60, 
    "COMPLETE", "black", "Times 13")
    #Creates the Back to Home Page Button 
    createHomeButton(app, canvas, 1100, 20, 1180, 100, "blue", 1140, 60,
    "HOME", "black", "Times 20")

#Mouse Pressed Function for To Do Screen
def toDoInputScreenMode_mousePressed(app, event): 
    #When Home Button Clicked, we empty all strings users edit and return to 
        #home Screen
    if app.HomeButtonToDo.buttonClicked(event.x, event.y): 
        app.mode = "homeScreenMode"
        app.toDoDay = ""
        app.toDoName1 = ""
        app.toDoName2 = ""
        app.toDoName3 = ""
        app.toDoLen1 = ""
        app.toDoLen2 = ""
        app.toDoLen3 = ""
        app.toDoStime1 = ""
        app.toDoStime2 = ""
        app.toDoStime3 = ""
        app.toDoEtime1 = ""
        app.toDoEtime2 = ""
        app.toDoEtime3 = ""
        app.toDoList = []
        app.toDoInfo = [(app.toDoLen1, app.toDoStime1, app.toDoEtime1), 
        (app.toDoLen2, app.toDoStime2, app.toDoEtime2), 
        (app.toDoLen3, app.toDoStime3, app.toDoEtime3)]
    if (app.completeButtonToDo.buttonClicked(event.x, event.y)): 
        app.toDOInfo = [(app.toDoLen1, app.toDoStime1, app.toDoEtime1), 
        (app.toDoLen2, app.toDoStime2, app.toDoEtime2), 
        (app.toDoLen3, app.toDoStime3, app.toDoEtime3)]
        app.toDoNameList.append(app.toDoName1)
        app.toDoNameList.append(app.toDoName2)
        app.toDoNameList.append(app.toDoName3)
        createOrigTODODict(app)
        createToDoList(app)
        returnScheduleDict = getAvailibleTimes(app)
        if returnScheduleDict != None:
            for each in returnScheduleDict:
                app.eventDict[app.toDoDay].append((each, "toDo", 
                    returnScheduleDict[each][0], returnScheduleDict[each][1], 
                    app.toDoDay))
            app.toDoNameList = []

#Key Pressed Function for To Do Screen where users can edit each of the strings
def toDoInputScreenMode_keyPressed(app, event): 
    if event.x >= 600 and event.x <= 900 and event.y >= 180 and event.y <= 230: 
        if event.key == "Space": 
            app.toDoDay  += " "
        elif event.key == "BackSpace": 
            app.toDoDay = app.toDoDay[:-1]
        else:  
            app.toDoDay += (event.key)
    if event.x >= 50 and event.x <= 250 and event.y >= 400 and event.y <= 450: 
        if event.key == "Space": 
            app.toDoName1  += " "
        elif event.key == "BackSpace": 
            app.toDoName1 = app.toDoName1[:-1]
        else:  
            app.toDoName1 += (event.key)
    if event.x >= 50 and event.x <= 250 and event.y >= 550 and event.y <= 600: 
        if event.key == "Space": 
            app.toDoName2  += " "
        elif event.key == "BackSpace": 
            app.toDoName2 = app.toDoName2[:-1]
        else:  
            app.toDoName2 += (event.key)
    if event.x >= 50 and event.x <= 250 and event.y >= 700 and event.y <= 750:
        if event.key == "Space": 
            app.toDoName3  += " "
        elif event.key == "BackSpace": 
            app.toDoName3 = app.toDoName3[:-1]
        else:  
            app.toDoName3 += (event.key)
    if event.x >= 330 and event.x <= 480 and event.y >= 400 and event.y <= 450:
        if event.key == "Space": 
            app.toDoLen1  += " "
        elif event.key == "BackSpace": 
            app.toDoLen1 = app.toDoLen1[:-1]
        else:  
            app.toDoLen1 += (event.key)
    if event.x >= 330 and event.x <= 480 and event.y >= 550 and event.y <= 600: 
        if event.key == "Space": 
            app.toDoLen2  += " "
        elif event.key == "BackSpace": 
            app.toDoLen2 = app.toDoLen2[:-1]
        else:  
            app.toDoLen2 += (event.key)
    if event.x >= 330 and event.x <= 480 and event.y >= 700 and event.y <= 750: 
        if event.key == "Space": 
            app.toDoLen3  += " "
        elif event.key == "BackSpace": 
            app.toDoLen3 = app.toDoLen2[:-1]
        else:  
            app.toDoLen3 += (event.key)
    if event.x >= 630 and event.x <= 780 and event.y >= 400 and event.y <= 450:
        if event.key == "Space": 
            app.toDoStime1  += " "
        elif event.key == "BackSpace": 
            app.toDoStime1 = app.toDoStime1[:-1]
        else:  
            app.toDoStime1 += (event.key)
    if event.x >= 630 and event.x <= 780 and event.y >= 550 and event.y <= 600:
        if event.key == "Space": 
            app.toDoStime2  += " "
        elif event.key == "BackSpace": 
            app.toDoStime2 = app.toDoStime2[:-1]
        else:  
            app.toDoStime2 += (event.key)
    if event.x >= 630 and event.x <= 780 and event.y >= 700 and event.y <= 750:
        if event.key == "Space": 
            app.toDoStime3  += " "
        elif event.key == "BackSpace": 
            app.toDoStime3 = app.toDoStime3[:-1]
        else:  
            app.toDoStime3 += (event.key)
    if event.x >= 930 and event.x <= 1080 and event.y >= 400 and event.y <= 450:
        if event.key == "Space": 
            app.toDoEtime1  += " "
        elif event.key == "BackSpace": 
            app.toDoEtime1 = app.toDoEtime1[:-1]
        else:  
            app.toDoEtime1 += (event.key)
    if event.x >= 930 and event.x <= 1080 and event.y >= 550 and event.y <= 600:
        if event.key == "Space": 
            app.toDoEtime2  += " "
        elif event.key == "BackSpace": 
            app.toDoEtime2 = app.toDoEtime2[:-1]
        else:  
            app.toDoEtime2 += (event.key)
    if event.x >= 930 and event.x <= 1080 and event.y >= 700 and event.y <= 750:
        if event.key == "Space": 
            app.toDoEtime3  += " "
        elif event.key == "BackSpace": 
            app.toDoEtime3 = app.toDoEtime3[:-1]
        else:  
            app.toDoEtime3 += (event.key)

#Creates the app.OrigToDoDict that's used by the To Do Page
def createOrigTODODict(app): 
    for i in range(len(app.toDoNameList)):
        name = app.toDoNameList[i]
        t =  app.toDOInfo[i]
        if name == "" or "" in t:
            continue
        app.OrigToDoDict[name] = t
    return app.OrigToDoDict 

#Creates the ToDoList that's also used by the To Do Screen
#List Used by the function createOrigTODODict
def createToDoList(app): 
    for toDoName in app.OrigToDoDict: 
        toDoNameLen = app.OrigToDoDict[toDoName][0]
        toDoNameStime = app.OrigToDoDict[toDoName][1]
        toDoNameEtime = app.OrigToDoDict[toDoName][2]
        app.toDoList.append((toDoName, toDoNameLen, toDoNameStime, 
                toDoNameEtime)) 
    return app.toDoList

#Backtracking Recusion Function that takes in information regarding user's 
    #desired events and adds into an availible time in the Calendar that's 
    #not already occupied
#Uses the getAvailibleTimesHelper Function
def getAvailibleTimes(app): 
    return getAvailibleTimesHelper(app, {})

#Helper Function for getAvailibleTimes
def getAvailibleTimesHelper(app, returnScheduleDict): 
    if len(app.toDoList) == 0: 
        return returnScheduleDict 
    else:  
        toDo = app.toDoList.pop()
        stime = int(toDo[2])
        etime = int(toDo[2]) + int(toDo[1])
        for n in range(stime, int(toDo[3]) - int(toDo[1]) + 1):
            etime = n + int(toDo[1])
            if etime > int(toDo[3]): 
                return None
            if etime > 24:
                return None
            possibleSchedule = (n, etime)
            if timeIsLegal(app, possibleSchedule, returnScheduleDict): 
                returnScheduleDict[toDo[0]] = possibleSchedule 
                result = getAvailibleTimesHelper(app, returnScheduleDict)
                if result != None: 
                    return result
                del returnScheduleDict[toDo[0]] 
        app.toDoList.append(toDo)
        return None

# This function is the isLegal/helper function for getAvailibleTimesHelper
def timeIsLegal(app, possibleSchedule, returnScheduleDict):
    stime = possibleSchedule[0]
    etime = possibleSchedule[1] 
    for event in app.eventDict[app.toDoDay]: 
        eventStime = event[2]
        eventEtime = event[3]
    # This if statment checks if the possible schedule time is not in between 
        # any of the other scheduled events 
        if ((stime > eventStime and stime < eventEtime) or 
        (etime > eventStime and etime < eventEtime) or 
        (stime <= eventStime and etime >= eventEtime)):
            return None
    #This checks if possibleSchedule interfers with what's 
        #already in returnSchDict
    if len(returnScheduleDict) >= 1: 
        for i in returnScheduleDict: 
            if ((stime >= returnScheduleDict[i][0] and 
                stime < returnScheduleDict[i][1]) or 
                (etime > returnScheduleDict[i][0] and 
                etime < returnScheduleDict[i][1]) or 
                (stime <= returnScheduleDict[i][0] and 
                etime >= returnScheduleDict[i][1])):
                    return None 
    return True

def runLLandLyourself(): 
    runApp(width = 1200, height = 800)

runLLandLyourself()
