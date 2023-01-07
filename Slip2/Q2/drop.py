#drop
import pandas as pd
import numpy as np 
import matplotlib.pyplot as mtp
dict={'First Score':[100,90,np.nan,95],
      'Second Score':[30,45,56,np.nan],
      'Third Score':[np.nan,40,80,98],
      'Fourth Score':[80,90,np.nan,50]}
#creating a dataframe from list
df=pd.DataFrame(dict)
print(df)
df.isnull()

