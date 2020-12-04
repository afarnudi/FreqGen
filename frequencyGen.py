#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:56:23 2020

@author: ali
"""
import sys
import argparse
import platform
import numpy as np
import os
OSplatform= platform.system()

def singlefrequencygenerator():
    '''
    Gets Frequency and duration from user and plays the frequency for the duration.
    
    Returns
    -------
    None.

    '''
    frequency = float(input('Please enter the frequency:\n>>> '))
    duration = float(input('Please enter the duration of the played frequency (in seconds):\n>>> '))
    duration *=1000

    if OSplatform == 'Darwin':
        # First install Homebrew (https://brew.sh/) 
        # and then SoX using 'brew install sox' in the terminal
        import os
        try:
            os.system('play -n synth %s sin %s' % (duration/1000, frequency))
        except:
            print("This feature uses the SoX software package. \nPlease install Homebrew (https://brew.sh/),\n then install SoX using 'brew install sox' in the terminal") 
            exit()
    elif OSplatform == 'Windows':
        import winsound
        winsound.Beep(frequency, duration)
    elif OSplatform == 'Linux':
        # 
        import os
        try:
            os.system('play -n synth %s sin %s' % (duration/1000, frequency))
        except:
            print("This feature uses the SoX software package. \nSoX can be installed using 'sudo apt-get install sox' in the terminal")
            exit()

def multifrequencygenerator():
    '''
    Gets Frequency range and duration from user and plays the frequencies for the duration.

    Returns
    -------
    None.

    '''
    frequency = input('Please enter the frequency range. example: 2 400 \n>>> ').split()
    duration =  float(input('Please enter the duration of the played frequency (in seconds):\n>>> '))
    duration *=1000
    freqbegin=float(frequency[0])
    freqend  =float(frequency[1])
    
    if OSplatform == 'Darwin':
        try:
            os.system('play -n synth %s sin %s+%s' % (duration/(1000), freqbegin, freqend))
        except:
            print("This feature uses the SoX software package. \nPlease install Homebrew (https://brew.sh/),\n then install SoX using 'brew install sox' in the terminal") 
            exit()
    elif OSplatform == 'Windows':
        import winsound
        winsound.Beep(freqbegin, duration)
    elif OSplatform == 'Linux':
        try:
            os.system('play -n synth %s sin %s+%s' % (duration/1000, freqbegin, freqend))
        except:
            print("This feature uses the SoX software package. \nSoX can be installed using 'sudo apt-get install sox' in the terminal")
            exit()
        
def recordmic():
    if OSplatform == 'Darwin':
        try:
            # os.system('timeout 5 sox -b 32 -e unsigned-integer -r 96k -c 2 -d --clobber --buffer $((96000*2*10)) /tmp/soxrecording.wav')
            os.system('rec -c 2 testsox.wav trim 0 5')
        except:
            print("This feature uses the SoX software package. \nPlease install Homebrew (https://brew.sh/),\n then install SoX using 'brew install sox' in the terminal") 
            exit()
    # elif OSplatform == 'Windows':
        # import winsound
        # winsound.Beep(freqbegin, duration)
    elif OSplatform == 'Linux':
        try:
            os.system('timeout 5 sox -b 32 -e unsigned-integer -r 96k -c 2 -d --clobber --buffer $((96000*2*10)) /tmp/soxrecording.wav')
        except:
            print("This feature uses the SoX software package. \nSoX can be installed using 'sudo apt-get install sox' in the terminal")
            exit()
def record(time):
    if OSplatform == 'Darwin':
        try:
            # os.system('timeout 5 sox -b 32 -e unsigned-integer -r 96k -c 2 -d --clobber --buffer $((96000*2*10)) /tmp/soxrecording.wav')
            os.system('rec -c 2 testsox.wav trim 0 {}'.format(time))
        except:
            print("This feature uses the SoX software package. \nPlease install Homebrew (https://brew.sh/),\n then install SoX using 'brew install sox' in the terminal") 
            exit()
    # elif OSplatform == 'Windows':
        # import winsound
        # winsound.Beep(freqbegin, duration)
    elif OSplatform == 'Linux':
        try:
            os.system('rec -c 2 testsox.wav trim 0 {}'.format(time))
        except:
            print("This feature uses the SoX software package. \nSoX can be installed using 'sudo apt-get install sox' in the terminal")
            exit()

def playback():
    if OSplatform == 'Darwin':
        try:
            # os.system('timeout 5 sox -b 32 -e unsigned-integer -r 96k -c 2 -d --clobber --buffer $((96000*2*10)) /tmp/soxrecording.wav')
            os.system('play testsox.wav')
        except:
            print("This feature uses the SoX software package. \nPlease install Homebrew (https://brew.sh/),\n then install SoX using 'brew install sox' in the terminal") 
            exit()
    # elif OSplatform == 'Windows':
        # import winsound
        # winsound.Beep(freqbegin, duration)
    elif OSplatform == 'Linux':
        try:
            os.system('play testsox.wav')
        except:
            print("This feature uses the SoX software package. \nSoX can be installed using 'sudo apt-get install sox' in the terminal")
            exit()

def echomode():
    print('\nRecord for t seconds. Then hear the playback')
    time =input('\nPlease set t. \nIf this is your first time, try 5 seconds >>> ')
    status=True
    input('Press enter to start.')
    while(status):
        record(time)
        playback()
        keyin = input('Press enter to start again or q to exit >>> ')
        if keyin=='q':
            status=False
    os.system('rm testsox.wav')
    
    
    
    
    
def argparser():
    parser = argparse.ArgumentParser(description='Frequency generator')
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, required=True, 
        help="Set frequency generator mode: 'S' single, 'R' Ranged frequency mode.")
    
    return parser.parse_args()


args =argparser()

if args.mode == 'S':
    singlefrequencygenerator()
elif args.mode == 'R':
    multifrequencygenerator()
elif args.mode == 'E':
    echomode()
else:
    print('{}: No such option. Please run "{} -h" for a list of available options.'.format(args.mode,sys.argv[0]))
    exit()