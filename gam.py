import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


sampleHeigth = 6.65
limeStoneAtenuation = 0.209998
filelist = ['ga-data/VN01_plano_0.txt',
            'ga-data/VN01_plano_45.txt',
            'ga-data/VN01_plano_90.txt',
            'ga-data/VN01_plano_135.txt']

sampleRaw = pd.concat([pd.read_csv(item, names=[item[19:-4]]) for item in filelist], axis=1)
iniIntensity = sampleRaw.iloc[[0,1,2,11,12,13]].mean().mean()
sampleRaw['relatInt'] = sampleRaw.mean(axis=1)/iniIntensity
sampleRaw['mi'] = -1*np.log(sampleRaw['relatInt'])/sampleHeigth
sampleRaw['porosity'] = (limeStoneAtenuation-sampleRaw['mi'])/limeStoneAtenuation

sample =sampleRaw.iloc[[3,4,5,6,7,8,9,10]]
print(sample['porosity'].mean()*100)

plt.plot(sample['porosity'],'.')
