#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display


# In[2]:


df_tips = sns.load_dataset("tips")


# In[3]:


ALL = "ALL"
def unique_sorted_values_plus_ALL(array):
    unique=array.unique().tolist()
    unique.sort()
    unique.insert(0,ALL)
    return unique


# In[4]:


drop_day = widgets.Dropdown(options= unique_sorted_values_plus_ALL(df_tips.day))


# In[5]:


def dropdown_day(change):
    if(change.new == ALL):
        tips=df_tips.groupby(["day"])["tip"].mean()
        df_new=tips.reset_index()
        df_new= df_new.rename(columns = {
            df_new.columns[1]: "Mean"
        })
        display(df_new)
    else:
        tips=df_tips[df_tips.day == change.new]
        tips=tips.mean()
        df_new=tips.reset_index()
        df_new= df_new.rename(columns = {
            df_new.columns[1]: "Mean"
        })
        display(df_new)


# In[6]:


drop_day.observe(dropdown_day, names="value")


# In[7]:


display(drop_day)


# In[ ]:




