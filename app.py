#!/usr/bin/env python

import time
import sys

from rapp_robot_api import RappRobot
rh = RappRobot()
from RappCloud import RappPlatformAPI
ch = RappPlatformAPI()

rh.audio.setVolume(50)
rh.audio.speak("Hello")

while True:
    rh.audio.speak('Do you want to recognize an object or learn it?')
    r = rh.audio.speechDetection(['learn', 'recognize', 'exit'], 10.0, 'English')
    if r['word'] == 'learn':
        rh.audio.speak("Ok, lets learn the object")
        rh.audio.speak("Show me the object")
        time.sleep(3)
        rh.vision.capturePhoto('/home/nao/temp.jpg', 'front', '640x960')
        ch.objectDetectionClearModels()
        ch.objectDetectionLearnObject('/home/nao/temp.jpg', 'test')
    elif r['word'] == 'recognize':
        rh.audio.speak("I am going to recognize the object")
        ch.objectDetectionLoadModels(['test'])
        rh.vision.capturePhoto('/home/nao/temp.jpg', 'front', '640x960')
        r = ch.objectDetectionFindObjects('/home/nao/temp.jpg')
        if len(r['found_names']) != 0:
            rh.audio.speak("I have seen the object!")
        else:
            rh.audio.speak("The object does not exist!")
    elif r['word'] == 'exit':
        rh.audio.speak("bye bye")
        break
    else:
        rh.audio.speak("I did not understand")



