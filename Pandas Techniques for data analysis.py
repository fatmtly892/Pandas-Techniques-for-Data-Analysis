#!/usr/bin/env python
# coding: utf-8

# In[59]:


#importing data
import pandas as pd


# In[60]:


#loading data
df = pd.read_csv('IMDB-Movie-Data.csv')
df


# In[61]:


df.head()
df.head(10)


# In[62]:


df.info()


# In[63]:


#Select Columns
director = df[['Director']]
director


# In[64]:


#Selecting Multiple Columns
multi_col = df[['Rank', 'Title']]
multi_col


# In[65]:


#Select Rows
df.iloc[[2]]


# In[66]:


#Select Rows with Logic 
genre=df[df['Genre']== 'Horror']
genre


# In[67]:


#groupby operation
df.groupby('Genre')[['Votes']].mean().head()


# In[68]:


#Sorting operation
df.groupby('Genre')[['Votes']].mean().sort_values(['Votes']).head()


# In[69]:


# Classify movies based on ratings
def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'


# In[72]:


# creating a new variable in the dataset to hold the rating category
df['Rating_category'] = df['Rating'].apply(rating_group)
df[['Title','Director','Rating','Rating_category']].head(10)

