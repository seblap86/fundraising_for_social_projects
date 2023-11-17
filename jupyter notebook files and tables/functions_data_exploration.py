#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[ ]:


def correlation_matrix(projects):
    '''
    Prints correlation matrix (heatmap format) of the projects dataframe.
    '''
    projects_numerical = projects.select_dtypes(include = ['float64', 'int64'])
    corr_matrix = projects_numerical.corr().round(decimals=2)    
    heatmap = sns.heatmap(corr_matrix, annot=True, linewidth=.5)
    print(heatmap)

