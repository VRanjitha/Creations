#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Sometimes the data may have too many variables such that most of the variables are correlated

#Model on the whole data => poor accuracy

# Soln- PCA

# Working principle of PCA - dimensionality reduction

# PCA - method of extracting important variables with a motive to capture as much info as possible
#     - extracts low dimensional set of variables from a high dimensional set

# Here we are not going to predict y
# The PCA unsupervised learning approach tries to learn the strength of relationship of varaiables


# In[1]:


# Analysing eating habit, excercise habit and body shape


# In[1]:


import pandas as pd


# In[2]:


df=pd.DataFrame(columns=['Calory','Breakfast','Lunch','Dinner','Excercise','Body Shape'])


# In[3]:


df.loc[0]=[1200,1,0,0,2,'Skinny']
df.loc[1]=[2800,1,1,1,1,'Fat']
df.loc[2]=[3500,2,2,1,0,'Skinny']
df.loc[3]=[1400,0,1,0,3,'Skinny']
df.loc[4]=[1600,1,0,2,0,'Normal']
df.loc[5]=[3200,1,2,1,1,'Fat']
df.loc[6]=[1750,1,0,0,1,'Skinny']
df.loc[7]=[1600,1,0,0,0,'Skinny']


# In[4]:


df


# In[5]:


# Split feature vectors and labels
x=df[['Calory','Breakfast','Lunch','Dinner','Excercise']]
y=df[['Body Shape']]


# In[6]:


y


# In[7]:


# The mean of 'Calory' will be very high compared to the means of the other 4 columns....so we have to normalise it 
# Using StandardScaler (-1,1)

from sklearn.preprocessing import StandardScaler
x_std=StandardScaler().fit_transform(x)


# In[8]:


x_std


# ## Traditional method using Covariance matrix

# In[9]:


# Covariance matrix of features

# Features are columns from x_std

import numpy as np
features=x_std.T
covariance_matrix=np.cov(features)
print(covariance_matrix)

#PCA believed that the points which have close cov or corr have more impact
#Eigen vector- the respected features....not suppressed

# .t means transform


# In[11]:


# Eigen vectors and eigen values from co-variance matrix 
#The eigenvector with the largest eigenvalue is the direction along which the data set has the maximum variance.
eig_vals,eig_vecs=np.linalg.eig(covariance_matrix)


# In[14]:


print('\nEigen values \n%s' %eig_vals)


# In[16]:


# Reduce dimension to 1 dimension
eig_vals[0]/sum(eig_vals)   #...... = 1st principal/performing component


# In[17]:


# Project datapoint onto selected eigen vector
projected_x=x_std.dot(eig_vecs.T[0])


# In[18]:


projected_x   #.....The columns in the dataset has been converted into 1 influential column....represented on x-axis
              # since its unsupervised learning, the value of the y-axis is 0


# In[20]:


result=pd.DataFrame(projected_x,columns=['PC1'])   # PC1=Principal Component 1
result['y-axis']=0.0
result['label']=y
result


# In[23]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


sns.lmplot('PC1','y-axis',data=result,fit_reg=False,scatter_kws={'s':50},hue='label')

#title
plt.title('PCA result')

# hue='label' .....unknown labels
# fit_reg.... fit regression


# In[25]:


# In the above plot, the left side is for breakfast and lunch
# the right side is for dinner and exercise

# Even if you have low calorie intake, if u hv breakfast or lunch then the body shape will be FAT
# To be NORMAL, u should hv moderate values for all the independent variables in the original dataset
         #...since NORMAL is in the center
# Even if you have high calorie intake, if u hv dinner and excercise then the body shape will be SKINNY


# ### Trial 2 ....changing the value for NORMAL (Dinner)

# In[32]:


df.loc[4]=[1600,1,0,10,0,'Normal']
df


# In[33]:


x=df[['Calory','Breakfast','Lunch','Dinner','Excercise']]
y=df[['Body Shape']]


# In[34]:


x_std=StandardScaler().fit_transform(x)
x_std


# In[35]:


features=x_std.T
covariance_matrix=np.cov(features)
print(covariance_matrix)


# In[36]:


eig_vals,eig_vecs=np.linalg.eig(covariance_matrix)


# In[37]:


print('\nEigen values \n%s' %eig_vals)


# In[38]:


eig_vals[0]/sum(eig_vals)   #...... = 1st principal/performing component


# In[40]:


# Project datapoint onto selected eigen vector
projected_x=x_std.dot(eig_vecs.T[0])
projected_x


# In[41]:


result=pd.DataFrame(projected_x,columns=['PC1'])   # PC1=Principal Component 1
result['y-axis']=0.0
result['label']=y
result


# In[42]:


sns.lmplot('PC1','y-axis',data=result,fit_reg=False,scatter_kws={'s':50},hue='label')

#title
plt.title('PCA result')

# Here the point for NORMAL has shifted to the right since the value for dinner has increased


# ### Trial 3 ....changing the value for NORMAL (Excercise)

# In[43]:


df.loc[4]=[1600,1,0,2,10,'Normal']
df


# In[44]:


x=df[['Calory','Breakfast','Lunch','Dinner','Excercise']]
y=df[['Body Shape']]
x_std=StandardScaler().fit_transform(x)
x_std


# In[45]:


features=x_std.T
covariance_matrix=np.cov(features)
print(covariance_matrix)


# In[46]:


eig_vals,eig_vecs=np.linalg.eig(covariance_matrix)


# In[47]:


print('\nEigen values \n%s' %eig_vals)


# In[48]:


eig_vals[0]/sum(eig_vals)   #...... = 1st principal/performing component


# In[49]:


# Project datapoint onto selected eigen vector
projected_x=x_std.dot(eig_vecs.T[0])
projected_x


# In[50]:


result=pd.DataFrame(projected_x,columns=['PC1'])   # PC1=Principal Component 1
result['y-axis']=0.0
result['label']=y
result


# In[51]:


sns.lmplot('PC1','y-axis',data=result,fit_reg=False,scatter_kws={'s':50},hue='label')

#title
plt.title('PCA result')

# Here the point for NORMAL has shifted to the rightmost side since the value for Excercise has increased


# ### Trial 4 ....changing the value for NORMAL (Breakfast) 

# In[52]:


df.loc[4]=[1600,10,0,2,0,'Normal']
x=df[['Calory','Breakfast','Lunch','Dinner','Excercise']]
y=df[['Body Shape']]
x_std=StandardScaler().fit_transform(x)
features=x_std.T
covariance_matrix=np.cov(features)
eig_vals,eig_vecs=np.linalg.eig(covariance_matrix)
print('\nEigen values \n%s' %eig_vals)
eig_vals[0]/sum(eig_vals)   #...... = 1st principal/performing component


# In[53]:


projected_x=x_std.dot(eig_vecs.T[0])
result=pd.DataFrame(projected_x,columns=['PC1'])   # PC1=Principal Component 1
result['y-axis']=0.0
result['label']=y
result


# In[54]:


sns.lmplot('PC1','y-axis',data=result,fit_reg=False,scatter_kws={'s':50},hue='label')

#title
plt.title('PCA result')

# Here the point for NORMAL has shifted to the leftmost side since the value for Breakfast has increased


# In[ ]:




