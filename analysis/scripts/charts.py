import matplotlib as mpl
import seaborn as sns
import pandas as pd

sns.set_style({'font.family':"sans-serif"})
sns.set_style('darkgrid')

# chart methods
def my_pie(data, group, title, ax=None, figsize=None):
    data.groupby([group]).size().plot.pie(
        title=title, ylabel='', 
        autopct=lambda p:'{:.1f}% ({:.0f})'.format(p, (p/100)*data.groupby([group]).size().sum()),
        figsize=figsize, ax=ax
    )

def my_bar(data, group, title, ax=None, order=None):
    if(not ax):
        _, ax_t = mpl.pyplot.subplots()
    ax_t = sns.countplot(y = group, hue = group, data = data, order = order, ax = ax, palette='deep')
    ax_t.set_title(title)