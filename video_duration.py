#Author:  Brandon Barton
#Created: 3/29/2012
#Info:Converts a single video file into its video duration
#Deps: ffmpeg

#TODO: Add test cases
import subprocess, re, datetime
from dateutil.parser import *

#Warning: If ffprobe's output is ever changed, this part might break.
def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  return [x for x in result.stdout.readlines() if "Duration" in x]

def getDurationTimestamp(filename):
	stamp = getLength(filename)

	#Check for case of not a video file
	if not stamp:
		return datetime.timedelta() #Return empty timedelta for non-video files (Will add exception handling later)
	else:
		stamp = stamp[0]

	#Regular expression extracts the timestamp string
	trimmedStamp = re.findall(r'\d\d:\d\d:\d\d',stamp)
	trimmedStamp = trimmedStamp[0]

	#Turns the timestamp string into a datetime object
	ts = parse(trimmedStamp)
	return datetime.timedelta(hours = ts.hour, seconds = ts.second, minutes = ts.minute)

