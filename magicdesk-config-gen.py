#!/bin/env python

import os

filename = 'multicart'
size = 1024
colour = 6
spacing = 0

directory = './prg'
subdirectories = []

for dirname in os.listdir(directory):
  subdirectories.append(str(dirname))

menunumber = 0

print "[cartridge]"
print "bin=" + filename + ".bin"
print "size=" + str(size)
print "wave=0"
print "sound=0"
print "\nborder=" + str(colour)
print "background=" + str(colour)
print "character=" + str(colour)

for subdirectory in subdirectories:
  menunumber = menunumber + 1
  prgnumber = 0
  menu = subdirectory.replace("_", " ")
  menu = menu.title()
  items = os.listdir(directory + "/" + subdirectory)
  print "\n\n[menu" + str(menunumber) + "]"
  print "spacing=" + str(spacing)
  print "title=" + menu
  for game in items:
    prgnumber = prgnumber + 1
    print "\n[prg" + str(menunumber) + str(prgnumber).zfill(2) + "]"
    gametitle = os.path.splitext(game)
    gametitle = gametitle[0].replace("_", " ")
    gametitle = gametitle.title()
    print ("file=" + subdirectory + "/" + game)
    print ("name=" + gametitle)

