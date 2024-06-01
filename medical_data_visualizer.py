import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
# df['overweight'] =(df['weight']/((df['height']/100)**2)).apply(lambda x:1 if x>25 else 0)
df['overweight']=np.where((df['weight']/((df['height']/100)**2))>25,1,0)

# 3
df['cholesterol']=np.where(df['cholesterol']==1,0,1)
df['gluc']=np.where(df['gluc']==1,0,1)
#df.loc[df['cholesterol']==1,'cholesterol']=0
#df.loc[df['cholesterol']>=2,'cholesterol']=1
#df.loc[df['gluc']==1,'gluc']=0
#df.loc[df['gluc']>=2,'gluc']=1
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars='cardio',value_vars=['cholesterol','gluc','alco','active','smoke','overweight'])
    

    # 6
    df_cat =  df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    df_cat['value'] = df_cat['value'].astype(str)
    g=sns.catplot(x='variable',y='total',col='cardio',hue='value',kind="bar",data=df_cat)


    # 8
    fig = g.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
        # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
  
    # Calculate the correlation matrix
    corr_mat = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr_mat,dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    
    with sns.axes_style("white"):
      fig, ax = plt.subplots( figsize=(10,8) )
      sns.heatmap(corr_mat, mask=mask, annot=True, center=0, linewidths=.5, square=True,vmin=-0.15, vmax=0.3, fmt='0.1f')

      
    # Do not modify the next two lines
    

    fig.savefig('heatmap.png')
    return fig
