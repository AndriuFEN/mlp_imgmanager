# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 23:53:01 2022

@author: Andriu
"""

#%% SCRIPTS SETUP

import argparse

parser = argparse.ArgumentParser(prog= 'canny edges',
                                 description = 'Extract edges from images',
                                 epilog = 'Created by Andriu')
    
parser.add_argument('-t1','--threshold1',type=int, default=100)
parser.add_argument('-t2','--threshold2',type=int, default=200)
parser.add_argument('-ap','--aperture',type=int,default=3,choices=[3, 5, 7])
parser.add_argument('-e','--extension',type=str,default='png')
parser.add_argument('-v','--verbose',type=int,default=1)

args = parser.parse_args()

# ARGUMENTS
t1 = args.threshold1
t2 = args.threshold2
ap = args.aperture

ext = args.extension.lower()
verb = args.verbose

#%% IMPORT PACKAGES

print('Importing Packages...\n')

import os
import cv2
import matplotlib.pyplot as plt
 
#%% SCRIPT SETUP

print('Setting up the Script...\n')

base_folder = 'canny_edges/'
input_folder = base_folder+'INPUT/'
output_folder = base_folder+'OUTPUT/'

if not len(os.listdir(output_folder))==0:
    print('Cleaning previous results...\n')
    for f in os.listdir(output_folder):
        os.remove(output_folder+f)
        del(f)


#%% LOAD DATA

print('Reading Image files...\n')

files = os.listdir(input_folder)

images = []
for f in files:
    img = cv2.imread(input_folder+f,1)
    rgb  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    edges = cv2.Canny(img, threshold1=t1, threshold2=t2, apertureSize=ap)
    dicto = {'in':f,'edge':edges,'out':''}
    images.append(dicto)
    del(img, dicto)


#%% RENAME FILES

print('Renaming Files...\n')

for i in range(len(images)):
    images[i]['out'] = 'output'+' '+'('+str(i+1)+').'+ext
del(i)

#%% SAVING RESULTS

print('Saving Results...\n')
for img in images:
    print(img['out'])
    plt.imsave(fname=output_folder+img['out'], arr=img['edge'], cmap='Greys', format=ext)

#%% END

print('Script Run Successful!')
