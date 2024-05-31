import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
# df['overweight'] =(df['weight']/((df['height']/100)**2)).apply(lambda x:1 if x>25 else 0)
df['overweight']=np.where((df['weight']/(df['height']/100)**2)>25,1,0)

# 3
df['cholesterol']=df['cholesterol'].apply(lambda x:0 if x==1 else 1)
df['gluc']=df['gluc'].apply(lambda x:0 if x==1 else 1)
#df.loc[df['cholesterol']==1,'cholesterol']=0
#df.loc[df['cholesterol']>=2,'cholesterol']=1
#df.loc[df['gluc']==1,'gluc']=0
#df.loc[df['gluc']>=2,'gluc']=1
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars='cardio',value_vars=['cholesterol','gluc','alco','active','smoke'],var_name='Feature',value_name='Value')
    

    # 6
    df_cat =  df_cat.groupby(['cardio', 'Feature', 'Value']).size().reset_index(name='total')
    

    # 7
    df_cat['Value'] = df_cat['Value'].astype(str)
    g=sns.catplot(x='Feature',y='total',col='cardio',hue='value',kind="bar",data=df_cat)


    # 8
    fig = g.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
