import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import glob

class Sample:
    def __init__(self, heigth,formation):
        self.heigth = heigth
        self.formation = formation
        
        if formation == 'limestone':
            self.atenuation = 0.209998
    
    def li_attenuation(self,filelist):
        sampleRaw = pd.concat([pd.read_csv(item, names=[item[19:-4]]) for item in filelist], axis=1)
        iniIntensity = sampleRaw.iloc[[0,1,2,11,12,13]].mean().mean()
        sampleRaw['relatInt'] = sampleRaw.mean(axis=1)/iniIntensity
        sampleRaw['mi'] = -1*np.log(sampleRaw['relatInt'])/self.heigth
        
        sample =sampleRaw.iloc[[3,4,5,6,7,8,9,10]]
        print(sample['mi'])
        return (sample['mi']) 

        

    def porosity(self,filelist):
        sampleRaw = pd.concat([pd.read_csv(item, names=[item[19:-4]]) for item in filelist], axis=1)
        iniIntensity = sampleRaw.iloc[[0,1,2,11,12,13]].mean().mean()
        sampleRaw['relatInt'] = sampleRaw.mean(axis=1)/iniIntensity
        sampleRaw['mi'] = -1*np.log(sampleRaw['relatInt'])/self.heigth
        sampleRaw['porosity'] = (self.atenuation-sampleRaw['mi'])/self.atenuation
        
        sample =sampleRaw.iloc[[3,4,5,6,7,8,9,10]]
        return (sample['porosity']*100) 
        #return (sample['porosity'].mean()*100)
    
path = 'ga-data/*.txt'
heigthList = [6.65,5.40,5.03,3.75,5.16,7.07,5.82,7.66,3.35,7.27]
hePorosity = [16.55, 16.17, 6.27, 24.38, 27.29, 21.05, 9.89, 22.71, 24.39, 25.21]

filelist = []
for files in glob.glob(path):
    filelist.append(files)


porosidade = []
atenuacao = []
pos = 0
for i in range(0,10):
    porosidade.append(Sample(heigthList[i],'limestone').porosity(filelist[pos:pos+4]))
    atenuacao.append(Sample(heigthList[i],'limestone').li_attenuation(filelist[pos:pos+4]))
    pos+=4


fig, axs = plt.subplots(5, 2,sharex=True,sharey=True)
#plt.subplots_adjust(wspace=0, hspace = 1)
x = np.linspace(0, 35, 8)
k = 0
for i in range(0,5):
    for j in range(0,2):
        axs[i, j].plot(x, atenuacao[k],'.')
        ratio = 1.0
        axs[i,j].set_aspect(100)
        axs[i,j].grid(True)
        axs[i, j].set_title('Sample '+str(k))
        k+=1
        
for ax in fig.get_axes():
    ax.label_outer()
    
'''
plt.boxplot(porosidade,labels=['VN01','VN02','VN04','VN05','5','6','7','8','9','10'])
plt.xlabel('Samples')
plt.ylabel('Gamma-porosity')
'''





