import sys
import json
import time
from telnetlib import Telnet
import serial

ser = serial.Serial('COM9', 9600, timeout=1);
tn=Telnet('localhost',13854);

start=time.clock();

i=0;
tn.write('{"enableRawOutput": true, "format": "Json"}');

eSenseDict={'attention':0, 'meditation':0};
waveDict={'lowGamma':0, 'highGamma':0, 'highAlpha':0, 'delta':0, 'highBeta':0, 'lowAlpha':0, 'lowBeta':0, 'theta':0};
signalLevel=0;

while i<100:
	blinkStrength=0;

	line=tn.read_until('\r');
	if len(line) > 20:	
		timediff=time.clock()-start;
		dict=json.loads(str(line));
		if "poorSignalLevel" in dict:
			signalLevel=dict['poorSignalLevel'];
		if "blinkStrength" in dict:
			blinkStrength=dict['blinkStrength'];
		if "eegPower" in dict:
			waveDict=dict['eegPower'];
			eSenseDict=dict['eSense'];
		
		attentionStr=str(eSenseDict['attention']);
		meditationStr=str(eSenseDict['meditation']);
		blinkStrengthStr=str(blinkStrength);
		
		print "Attention: " + attentionStr;
		print "Meditation: " + meditationStr;
		print "Blink Strength: " + blinkStrengthStr;
		print "";
		
		attentionInt = int(attentionStr)
		if attentionInt > 70:
			ser.write(chr(1));
			time.sleep(1)
	
			
		meditationInt = int(meditationStr)
		if meditationInt > 70:
			ser.write(chr(2));
			time.sleep(1)


		blinkStrengthInt = int(blinkStrengthStr)	
		if blinkStrengthInt > 1:
			ser.write(chr(3));
			time.sleep(1)	

ser.close();
tn.close();
