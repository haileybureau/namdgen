#!/usr/bin/env python
import MDAnalysis
import MDAnalysis.analysis.hbonds
import matplotlib.pyplot as plt
from sys import argv
from glob import glob
import numpy as np
import pickle
import sys,os,re

my_dir = os.path.abspath(os.path.dirname(__file__))

acc=[]

for path in glob(os.path.join(my_dir,'xxnumxx.*/*-hb.pkl*')):
    print path
    sample_i = pickle.load(open(path,'rb'))
    acc.append(sample_i)

def bondcount(trj,ii):
    lens = [(len(acc[trj][n])) for n in range(len(acc[trj]))]
    return lens

# plot parameters!
acclens= []
frames = np.linspace(13,33,len(acc[0]))
for c in range(len(acc)):
    lens = bondcount(c,3)
    acclens.append(lens)

data = np.array(acclens)
i4 = data.mean(axis=0)
print i4

# matplotlib
plt.plot(frames,i4,'k-',label="hydrogen bonds ")
plt.xlabel('end-to-end distance (A)')
plt.ylabel('average H-bond count')
plt.title('xxmoleculexx structure: NAMD/Charmm22')
plt.legend()
plt.gca().set_ylim(ymin=-0.2)
#plt.axis([9.9,35.1,-.1,7.4])

plt.draw()
texdir = os.path.join(('/'.join(my_dir.split('/')[0:-1])), \
                       'tex_%s/fig_bond' % my_dir.split('/')[-2])
if not os.path.exists(texdir):
    os.makedirs(texdir)
#plt.savefig('xxplotnamexx_allhb.eps')
#plt.savefig('xxplotnamexx_allhb.png')
plt.savefig('%s/xxplotnamexx_allhb.eps' % texdir)
plt.savefig('%s/xxplotnamexx_allhb.png' % texdir)
