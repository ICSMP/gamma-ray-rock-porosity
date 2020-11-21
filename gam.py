#from rocksLib import limeStone
import pandas as pd

filelist = ['ga-data/VN01_plano_0.txt',
            'ga-data/VN01_plano_45.txt',
            'ga-data/VN01_plano_90.txt',
            'ga-data/VN01_plano_135.txt']

ColumnsNames = ['0','45','90','135']
sample = pd.concat([pd.read_csv(item, names=[item[19:-4]]) for item in filelist], axis=1)
print(sample)
