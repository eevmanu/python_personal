# plex media server

# http://localhost:32400/library/all
# output xml

# cuantos son -> size
# metadata -> video.key
# file -> video->media->part.key
# filename -> video.title

# TO-DO forzar ip statica del servidor
# TO-DO monitorear el servicio plexmediaserver
# TO-DO fijar el puerto correcto para que no haya cruce

import xml.etree.ElementTree as ET
import requests

# Method 1
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com", 80))
server_ip = s.getsockname()[0]
s.close()

# Method 2 - ifconfig (linux) - ipconfig (windows)
# server_ip = '192.168.0.22'
server_port = '32400'

resp = requests.get(
    'http://{domain}:{port}/library/all'.format(
        domain=server_ip,
        port=server_port
    )
)

media_container = ET.fromstring(resp.content)

for info_file in media_container:
    if info_file.tag == 'Video':
        print info_file.attrib['title']

        info_part = info_file[0][0]

        print 'http://{domain}:{port}{url_file}'.format(
            domain=server_ip,
            port=server_port,
            url_file=info_part.attrib['key']
        )
