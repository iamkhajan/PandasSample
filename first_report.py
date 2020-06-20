import pandas as pd
import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt

def draw_graph():
    #bar1 = pd.crosstab(df.DeviceModel,df.Rating).plot(kind='bar')
    bar2 = pd.crosstab(df.Rating,df.Rating).plot(kind='bar')
    plt.savefig("test.pdf")



df = pd.read_csv("FeedBackReportForSeptember2018.csv")
df.dropna()
draw_graph()
print(df)



