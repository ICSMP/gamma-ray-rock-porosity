import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import glob

#Criando a classe Sample que cria um objeto!
class Sample:
    def __init__(self, heigth,formation):
        self.heigth = heigth
        self.formation = formation
        
        if formation == 'limestone':
            self.attenuation = 0.209998
        elif formation == 'sandstone':
            self.attenuation = 0.199999
        
    def intensity_zero(self,filelist):
        sampleRaw = pd.concat([pd.read_csv(item, names=[item[19:-4]]) for item in filelist], axis=1)
        self.iniIntensity = sampleRaw.iloc[[0,1,2,11,12,13]].mean().mean()
        
        return self.iniIntensity
    
    def li_attenuation(self,filelist):
        iniIntensity = self.intensity_zero(filelist)
        sampleRaw = pd.concat([pd.read_csv(item, names=[item[19:-4]]) for item in filelist], axis=1)
        #iniIntensity = sampleRaw.iloc[[0,1,2,11,12,13]].mean().mean()
        
        sampleRaw['relatInt-00'] = sampleRaw['0']/iniIntensity
        sampleRaw['relatInt-45'] = sampleRaw['45']/iniIntensity
        sampleRaw['relatInt-90'] = sampleRaw['90']/iniIntensity
        sampleRaw['relatInt-135'] = sampleRaw['135']/iniIntensity
        
        sampleRaw['mi-00'] = -1*np.log(sampleRaw['relatInt-00'])/self.heigth
        sampleRaw['mi-45'] = -1*np.log(sampleRaw['relatInt-45'])/self.heigth
        sampleRaw['mi-90'] = -1*np.log(sampleRaw['relatInt-90'])/self.heigth
        sampleRaw['mi-135'] = -1*np.log(sampleRaw['relatInt-135'])/self.heigth
        
        sample =sampleRaw.iloc[[3,4,5,6,7,8,9,10]]
        return sample[['mi-00','mi-45','mi-90','mi-135']]
        
    def porosity(self,filelist):
        sampleRaw = pd.concat([pd.read_csv(item, names=[item[19:-4]]) for item in filelist], axis=1)
        #iniIntensity = sampleRaw.iloc[[0,1,2,11,12,13]].mean().mean()
        iniIntensity = self.intensity_zero(filelist)
        sampleRaw['relatInt'] = sampleRaw.mean(axis=1)/iniIntensity
        sampleRaw['mi'] = -1*np.log(sampleRaw['relatInt'])/self.heigth
        sampleRaw['porosity'] = (self.attenuation-sampleRaw['mi'])/self.attenuation
        
        sample =sampleRaw.iloc[[3,4,5,6,7,8,9,10]]
        return (sample['porosity']*100) 
        #return (sample['porosity'].mean()*100)
    
path = 'ga-data/*.txt'
heigthList = [6.65,5.40,5.03,3.75,5.16,7.07,5.82,7.66,3.35,7.27]
hePorosity = [16.55, 16.17, 6.27, 24.38, 27.29, 21.05, 9.89, 22.71, 24.39, 25.21]

filelist = []
for files in glob.glob(path):
    filelist.append(files)
    
myRock = Sample(heigthList[0],'limestone')

'''
porosidade = []
atenuacao = []
pos = 0
for i in range(0,10):
    porosidade.append(Sample(heigthList[i],'limestone').porosity(filelist[pos:pos+4]))
    atenuacao.append(Sample(heigthList[i],'limestone').li_attenuation(filelist[pos:pos+4]))
    pos+=4





fig, axs = plt.subplots(5, 2, sharey=True,sharex=True, figsize=(6, 12))
x = np.linspace(0,35,8)
k = 0

for i in range(0,5):
    for j in range(0,2):
        axs[i,j].plot(x,atenuacao[k],'.')
        axs[i,j].set_xlabel('Displacement [mm]')
        axs[i,j].set_ylabel('L. Attenuation [cm-1]')
        axs[i,j].set_title('Sample '+str(k+1))
        k+=1

#plt.legend(['0','45','90','135'], ncol=4,loc="lower center")
fig.tight_layout() 
fig.subplots_adjust(bottom=0.1)
fig.legend(['0','45','90','135'], loc="lower center", ncol=4)
'''



