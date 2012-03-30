#3/29/2012
#Converts a single video files into a summed duration
import subprocess, re
from dateutil.parser import *

def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  return [x for x in result.stdout.readlines() if "Duration" in x]

def getDurationTimestamp(filename):
	stamp = getLength(filename)[0]
	trimmedStamp = re.findall(r'\d\d:\d\d:\d\d',stamp)
	trimmedStamp = trimmedStamp[0]
	return parse(trimmedStamp) #FIXIT: Make this work with more than 24 hours of video
