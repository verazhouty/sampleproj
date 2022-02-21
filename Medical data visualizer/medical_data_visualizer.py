import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
#print(df['height'] )
#print(df['weight'] )
#kg/m²

df['overweight'] =  (df['weight'] / (df['height'] / 100) ** 2) > 25


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, 
#make the value 0. If the value is more than 1, make the value 1.
#df['cholesterol'].describe()
#df['gluc'].describe()

#normalize_dic = { 1: 0, 2: 1, 3: 1}
#df['cholesterol'] = df['cholesterol'].map(medical_dict)
#df['gluc'] = df['gluc'].map(medical_dict)

#mask
m_chol = (df["cholesterol"]>1)
m_gluc = (df["gluc"]>1)
#sanitycheck 
#m_chol.describe()
#m_chol.mean()
#m_gluc.describe()
#m_gluc.mean()

df.loc[m_chol, "cholesterol"] = 1
df.loc[~m_chol, "cholesterol"] = 0
df.loc[m_gluc, "cholesterol"] = 1
df.loc[~m_gluc, "cholesterol"] = 0


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(
        frame=df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], 
        id_vars=['cardio']
    )

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(
        df_cat.groupby(['variable', 'value', 'cardio'])['value'].count())
    # df_cat.head()
    # reset_index() +rename
    df_cat = df_cat.rename(columns={'value': 'sum'}).reset_index()
    
    
    # Draw the catplot with 'sns.catplot()'
    ax=sns.catplot(x='variable', y='sum', data=df_cat, hue='value', col='cardio', kind='bar')
    ax.set_axis_labels("variable", "total")
    fig =ax.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.copy()
    # make changes in the original data frame itself
    df_heat.reset_index(inplace=True)
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    mask = np.zeros_like(corr)
    # Generate a mask for the upper triangle
    #generate matrix
    mask[np.triu_indices_from(mask)]=True
	#Return the indices for the upper-triangle of arr.
	    

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(ax=ax, data=corr, annot=True, fmt='.1f', mask=mask)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig