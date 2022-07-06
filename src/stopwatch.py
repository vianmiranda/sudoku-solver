run = False
text = "00:00"
min, sec = 0, 0

# start stopwatch
def startTime():
    global run
    if run == False:
        updateTime()
        run = True

# stop stopwatch
def stopTime():
    global run
    if run:
        updateTime()
        run = False

# reset stopwatch
def resetTime():
    global run, min, sec, text
    if run:
        run = False
    min, sec = 0, 0
    text = "00:00"
    startTime()

# update stopwatch
def updateTime():
    global text, min, sec
    if run:
        sec += 1
        if sec == 60:
            min += 1
            sec = 0
        min_string = f"0{min}" if min <= 9 else f"{min}"
        sec_string = f"0{sec}" if sec <= 9 else f"{sec}"
        text = f"{min_string}:{sec_string}"
    return text

# if anyone reads this, this was ironically the biggest headache to implement lol