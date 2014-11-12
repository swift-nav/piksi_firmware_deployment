#!/usr/bin/env python

### Update idex.json ###

import json
import glob
import os
import sys

# Extract version name from VERSION file
vf = open('VERSION', 'r')
version = vf.read().strip().split('=')[1]
vf.close()

print "--- VERSION ---"
print version

f = open('index.json', 'r')
j = json.load(f)
f.close()

def pp(x):
 return json.dumps(x, sort_keys=True, indent=4, separators=(',', ': '))

print "--- OLD JSON ---"
print pp(j)

# Update index.json with new version and url info

j['piksi_v2.3.1']['stm_fw']['version'] = version

# I know what you are thinking but it works just fine :)
base_url = os.path.dirname(j['piksi_v2.3.1']['stm_fw']['url'])

files = glob.glob("artifacts/*.hex")
if len(files) != 1:
  # Expect there to only be one hex file
  sys.exit(1)
filename = os.path.basename(files[0])

j['piksi_v2.3.1']['stm_fw']['url'] = base_url + '/' + filename

print "--- NEW JSON ---"
print pp(j)

f_new = open('index_new.json', 'w')
f_new.write(pp(j) + '\n')
f_new.close()

