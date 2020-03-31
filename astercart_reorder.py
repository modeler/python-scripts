#!/bin/env python

import os

hotkeys = [ '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
directory = './prg'
programs = []

for prg in os.listdir(directory):
  programs.append(str(prg))

programs = sorted(programs)
count = len(programs)

print str(count) + " programs found."

outputfile = open('order.txt', 'w') 

gamenumber = 1
for item in range(count):
  item = int(item)
  oldname = programs[item]
  newname = hotkeys[item] + '_' + oldname
  print '\t' + newname
  astername = 'Game' + str(gamenumber) + '.prg'
  command = '/usr/bin/cp ' + directory + '/' + oldname + ' ./' + astername
  os.system(command)
  outputfile.write( astername + ' = ' + newname + '\n')
  gamenumber = gamenumber + 1
  
outputfile.close()
