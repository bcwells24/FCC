import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1: Load dataset
df = pd.read_csv("medical_examination.csv")

# 2: Calculate BMI and determine if a person is overweight
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3: Normalize cholesterol and glucose values
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# 4: Draw the Categorical Plot
def draw_cat_plot():
    # 5: Convert data into long format
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6: Group and reformat the data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7: Create the categorical plot
    fig = sns.catplot(x="variable", y="total", hue="value", col="cardio", kind="bar", data=df_cat).fig

    # 8: Save and return the figure
    fig.savefig('catplot.png')
    return fig


# 10: Draw the Heat Map
def draw_heat_map():
    # 11: Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12: Calculate correlation matrix
    corr = df_heat.corr()

    # 13: Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14: Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # 15: Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=.5, cmap="coolwarm", center=0, ax=ax)

    # 16: Save and return the figure
    fig.savefig('heatmap.png')
    return fig
