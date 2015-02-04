import os
import urllib
import subprocess
from datetime import datetime as dt
from dateutil import parser


def getLength(filename):
    result = subprocess.Popen(
        ["ffprobe", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    return [x for x in result.stdout.readlines() if "Duration" in x]


def getDuration(cad):
    init = cad.index(':') + 1
    end = cad.index(',')
    duration_string = cad[init:end]
    return dt.time(parser.parse(duration_string))


def getSizeInMB_Local(filename):
    return float(os.stat(filename).st_size) / (1024*1024)


def getSizeInMB_URL(filename):
    d = urllib.urlopen(filename)
    info = d.info()
    size_bytes = info['Content-Length']
    size_mb = float(size_bytes) / (1024*1024)
    return size_mb


file_direction = 'http://ksvideos.blob.core.windows.net/videos/109.mp4'

a = getLength(file_direction)
print getDuration(a[0])
print getSizeInMB_URL(file_direction)
