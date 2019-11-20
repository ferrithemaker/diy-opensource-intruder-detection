# diy-opensource-intruder-detection

DIY opensource intruder detection device based on Raspberry Pi, Pi CAM, PIR sensor and Telegram

## Abstract

With this intruder detection script, the device will check if somebody is inside your house / room when you are out and it will take a (set of) picture(s) of the intruder. The pictures will be sent to your telegram bot channel wherever you are. You can add some "scare away" tactics, like trigger an alarm sound or a pre-recorded voice message.

## Components

To build this device you need:

- Raspberry Pi (3 or +)

- PiCam (i'm using a <10€ standard CSI camera connector PiCam)

- PIR Sensor (i'm using this one -> https://www.elecfreaks.com/estore/pir-sensor-brick.html)

- Telegram app

## Basic building instructions

- Install raspbian distro, with Python3 and Telepot and PiCamera modules using pip3 or apt 

- Install Telegram and create a bot using BotFather and following the instructions

- Install PiCam and PIR Sensor (Passive InfraRed presence sensor) hardware on your Raspberry Pi

- Check if all is working separately

- Set the python script telegram key and chat id from BotFather telegram data   

- Run the python script

## Basic usage instructions

- Start the script

- Open the telegram bot that you created before and control the script using the built-in commands

## Commands

- **enable pir**: if PIR sensor is enabled, when PIR is triggered, the script will take a picture and send it to your bot channel

- **disable pir**: if PIR sensor is disabled, never takes a picture automatically (when you are at home, PIR sensor must be disabled to avoid a picture flood) 

- **show**: take a real-time picture and send it to the telegram bot channel 
