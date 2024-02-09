# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 23:53:01 2022

@author: Andriu
"""

#%% SCRIPTS SETUP

import argparse

parser = argparse.ArgumentParser(prog= 'dreambooth name',
                                 description = 'Changes imgs names to Token',
                                 epilog = 'Created by Andriu')
    
parser.add_argument('-t','--token',required=True)
parser.add_argument('-e','--extension',default='png')
parser.add_argument('-v','--verbose',default=1)

args = parser.parse_args()

# ARGUMENTS
token = args.token.lower()
ext = args.extension.lower()
verb = int(args.verbose)

#%% IMPORT PACKAGES

print('Importing Packages...\n')

import os
from PIL import Image

#%% SCRIPT SETUP

print('Setting up the Script...\n')

base_folder = 'dreambooth_name/'
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
    img = Image.open(input_folder+f)
    dicto = {'in':f,'img':img,'out':''}
    images.append(dicto)
    del(img, dicto)

#%% RENAME FILES

print('Renaming Files...\n')

for i in range(len(images)):
    images[i]['out'] = token+' '+'('+str(i+1)+').'+ext
del(i)

#%% SAVING RESULTS

print('Saving Results...\n')
for img in images:
    print(img['out'])
    img['img'].save(output_folder+img['out'])

#%% END

print('Script Run Successful!')
