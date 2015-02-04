#!/usr/bin/env python
# coding=utf-8

import simplejson as json
import codecs
import sys

split_char = '^'

if len(sys.argv) != 2:
    print 'Faltan argumentos'
    sys.exit(0)

file_name = sys.argv[1]
input_file_name = './{}'.format(file_name)
output_file_name = './{}.csv'.format(file_name.split('.')[0])

# file_name = './playSong_mobile_data'
# input_file_name = '{}.json'.format(file_name)
# output_file_name = '{}.csv'.format(file_name)

with open(input_file_name) as input_file:

    content = input_file.readlines()
    content = [x.strip('\n') for x in content]

    with codecs.open(output_file_name, 'w', 'utf-8') as output_file:

        max_len = 0
        all_properties = []
        for line in content:
            if not line:
                continue

            event = json.loads(line)
            properties = event.get('properties')
            if not properties:
                continue

            n_properties = len(properties)
            if n_properties > max_len:
                max_len = n_properties
                all_properties = properties

        all_properties = all_properties.keys()

        cad = u''
        for key in all_properties:
            cad += unicode(key) + split_char
        cad += '\n'

        output_file.write(cad)

        for line in content:
            if not line:
                continue

            event = json.loads(line)
            properties = event.get('properties')
            if not properties:
                continue

            cad = u''
            for key in all_properties:
                if key in properties:
                    value = unicode(properties[key])
                    value = value.replace(";", "")
                    value = value.replace(",", "")
                    value = value.replace("\n", "")
                    cad += value + split_char
                else:
                    cad += split_char
            cad += '\n'

            output_file.write(cad)
