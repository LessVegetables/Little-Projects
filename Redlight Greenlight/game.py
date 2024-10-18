import cv2
import numpy as np
from skimage.metrics import structural_similarity
import time
from playsound import playsound
import random

threshold = 0.96

# Open the default camera (usually 0)
cap = cv2.VideoCapture(1, cv2.CAP_AVFOUNDATION)  # AVFoundation is the default on macOS

redLight = 0

if not cap.isOpened():
    print("Cannot open camera")
    exit()


# compare frames every 5 ish frames?
framesCount = -1

                # start screen, countdown, gameplay, finish
gamestate = 0   # 0,            1,         2,        3]

timerRunning = 0 #flag for the countdown

playerWin = 1 #flag for finish screen

timerInit = 0 #flag for the stoplight
timeToWait = int()

timeTillMusicEnds = 5 #for the song (so it wont start playing on every while iteration)
timeWhenMusicStartedPlaying = 0

ret, firstFrame = cap.read()
while True:
    framesCount += 1

    if gamestate == 0:      #start screen
        frame = np.zeros((512,512,3), np.uint8)   # Create a black image        
        cv2.putText(frame,"Are you ready to play?", (10,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.putText(frame,"SPACE to start", (10,140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        key = cv2.waitKey(50)
        if key == ord(' '):
            gamestate = 1   #switching to countdown

    elif gamestate == 1:    #countdown
        # resetting some of the flags
        timerInit = 0 #flag for the stoplight
        playerWin = 1 #flag for finish screen
        timeWhenMusicStartedPlaying = 0

        if timerRunning:
            secondsPassed = 3 - (time.time() - start_time)
            print(secondsPassed)
            frame = np.zeros((512,512,3), np.uint8)   # Create a black image 

            if secondsPassed >= 2:
                cv2.putText(frame,"3", (10,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 2)
            elif secondsPassed >= 1:
                cv2.putText(frame,"2", (10,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 2)
            elif secondsPassed >= 0:
                cv2.putText(frame,"1", (10,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 2)
            elif secondsPassed < 0:
                cv2.putText(frame,"1", (10,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 2) # so that there wont be a black blip
                ret, firstFrame = cap.read()
                gamestate = 2 #switching to gameplay
                redLight = 0
                timerRunning = 0 #ressetting in case player wants to play again
        else:
            timerRunning = 1
            start_time = time.time()

    elif gamestate == 2:    #gameplay
        
        # *a time tracking thing that determins whether or not it's redlight or greenlight*
        key = cv2.waitKey(50)
        if key == ord('s'):
            redLight = not(redLight)
        if key == ord(' '):
            gamestate = 3
            continue
        # *for now: it's gonna be this*
        if timerInit:
            print(timeToWait, timeToWait - (time.time() - start_time))
            if timeToWait - (time.time() - start_time) < 0:
                redLight = not(redLight)
                timerInit = not(timerInit)
        if not(timerInit):
            timerInit = 1
            if redLight:
                timeToWait = random.randint(3, 10)
            else:
                timeToWait = 5 * random.randint(1, 2)
            start_time = time.time()


        ret, secondFrame = cap.read()

        if redLight:
            stoplight = cv2.imread("red.png")
            cv2.imshow("Stoplight", stoplight)
            
            # motion detection
            # Convert images to grayscale
            firstFrameGray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
            secondFrameGray = cv2.cvtColor(secondFrame, cv2.COLOR_BGR2GRAY)
            # Blur image
            firstFrameBlurred = cv2.GaussianBlur(firstFrameGray, (7, 7), 0)
            secondFrameBlurred = cv2.GaussianBlur(secondFrameGray, (7, 7), 0)

            # Compute SSIM between two images
            score, diff = structural_similarity(firstFrameBlurred, secondFrameBlurred, full=True)
            print("Similarity Score: {:.3f}%".format(score * 100))

            if score < threshold:
                print("YOU MOVED YOU DIED")
                stoplight = cv2.imread("redeyes.png")
                cv2.imshow("Stoplight", stoplight)
                playsound('gun_shot.wav')
                gamestate = 3
                playerWin = 0

            # firstFrame = secondFrame # — move it here
        else:
            stoplight = cv2.imread("green.png")
            cv2.imshow("Stoplight", stoplight)
            if timeTillMusicEnds - (time.time() - timeWhenMusicStartedPlaying) < 0:
                playsound('greenlight 5 sec.mp3', False)
                timeWhenMusicStartedPlaying = time.time()

        firstFrame = secondFrame #if you're gonna decide to check motion not every frame –> move it into "if redLight"


        # cv2.imshow('firstFrameBlurred', firstFrameBlurred)      #<•><•><•><•><•><•><•><•><•><•><•><•><•><•><•><•>
        # cv2.imshow('secondFrameBlurred', secondFrameBlurred)    #<•><•><•><•><•><•><•><•><•><•><•><•><•><•><•><•>

        # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = cv2.flip(secondFrame, 1)

    elif gamestate == 3:    #finish
        
        frame = np.zeros((512,512,3), np.uint8)   # Create a black image
        if playerWin:
            cv2.putText(frame,"You live!", (10,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        else:
            cv2.putText(frame,"You're dead!", (10,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.putText(frame,"Gameover!", (10,140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.putText(frame,"Play again? Y/N", (10,180), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        key = cv2.waitKey(50)
        if key == ord('y') or key == ord('Y'):
            gamestate = 1   #switching to countdown
            redLight = 0
            stoplight = cv2.imread("green.png")
            cv2.imshow("Stoplight", stoplight)
        elif key == ord('n') or key == ord('N'):
            break

    else:
        raise Exception("Gamestate is out of bounds. gamestate:", gamestate)

    # If frame reading was unsuccessful, exit the loop
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break



    # Display the resulting frame
    cv2.imshow('Camera Feed', frame)

    key = cv2.waitKey(50)
    # Exit when 'q' is pressed
    if key == ord('q') or key == 27:
        break

# Release the capture when done and close the window
cap.release()
cv2.destroyAllWindows()
