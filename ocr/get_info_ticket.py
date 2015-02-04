from datetime import datetime
from string import ascii_letters
from string import punctuation
from decimal import Decimal

from PIL import Image
from pytesseract import image_to_string
import sys

# import urllib
# import cStringIO

# tmp_file = cStringIO.StringIO(urllib.urlopen('https://s3.amazonaws.com/pushbullet-uploads/ujEgJNlAJhc-KcPb3TMDTkL6730i3hLWMfxHaU7DPBQB/Scan.jpeg').read())
# img = Image.open(tmp_file)

img = Image.open('/home/msolorzanoc/Projects/Python/ocr/visa.jpg')
ticket = image_to_string(img)
# ticket = image_to_string(img, lang='spa')

ticket = ticket.split('\n')
ticket = [x for x in ticket if x]
for line in xrange(len(ticket)):
    print '{} : {}'.format(line+1, ticket[line])

if len(ticket) < 10:
    sys.exit(0)

# ----------------- id de ticket - fila 3
row3 = ticket[2]
# print row3
row3 = row3.strip()
pos = row3.index(' ')
row3 = row3[pos:]
row3 = row3.strip()
# print len(row3)
# for c in row3:
#     if c == 'h':
#         row3 = row3.replace(c, '4')
#     elif c == 'B':
#         row3 = row3.replace(c, '8')
visa_id = row3
print 'Purchase ID: {}'.format(visa_id)

# codigo tienda - fila 4
row4 = ticket[3]
row4 = row4.strip()
pos = row4.index('-')
row4 = row4[pos+1:]
retail_id = row4
print 'Retail ID: {}'.format(retail_id)


# nombre tienda - fila 4

# ----------------- monto - fila 9
row9 = ticket[8]
row9 = row9.strip()
pos = row9.index(' ')
row9 = row9[pos:]
row9 = row9.translate(None, ascii_letters+punctuation.replace('.', ''))
price = Decimal(row9)
print 'Price: {}'.format(price)
