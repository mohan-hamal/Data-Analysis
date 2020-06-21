#!/usr/bin/env python
# coding: utf-8

# # Import Pandas

# In[1]:


import pandas as pd


# # Import data

# In[2]:


header = ['id','title','year','rating','votes','length','genres']
data = pd.read_csv('imdb_top_10000.txt', sep ='\t', names = header , index_col = 0)


# # Exploring Data

# In[3]:


data.head(9)


# In[4]:


data.info()


# In[5]:


data.describe()


# # Exporting Data

# In[6]:


data.to_csv('test_export.csv', header = True, index = True, sep =',')


# # Sorting data

# In[7]:


data.sort_values(by = "rating", ascending = False)


# # Creating dataframes from scratch

# In[8]:


sim_data = { 
    'Mohan' : [20 , "10CGPA", 91.4],
    'Isha' : [18, 97, 100]}


# In[9]:


data2 = pd.DataFrame(sim_data)
data2


# In[10]:


del data2


# # Selecting data

# In[11]:


data[['title', 'rating']]


# In[12]:


data['rating'].mean()


# In[13]:


data['rating'].value_counts().sort_index(ascending = False)


# # Plotting

# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


data.plot()


# In[16]:


data.plot(kind ='scatter', x= 'rating', y = 'votes')


# In[17]:


data.plot(kind ='scatter', x= 'rating', y = 'votes', alpha = 0.3)


# In[18]:


data['rating'].plot(kind = 'hist')


# In[19]:


import seaborn as sns


# In[20]:


sns.lmplot(x='rating', y='votes', data = data)


# In[21]:


sns.pairplot(data)


# # Ordinary Least Squares(OLS) Regression

# In[22]:


import statsmodels.api as sm


# In[23]:


results = sm.OLS(data["votes"], data["rating"]).fit()


# In[24]:


results.summary()


# # Advanced data selection

# In[25]:


data[data['year']>1995]


# In[26]:


data[(data['year'] > 1995) & (data['year'] < 2000)]


# In[27]:


data[(data['year'] > 1995) & (data['year'] < 2000)].sort_values(by = 'rating', ascending = False).head(10)


# # Grouping

# In[28]:


data.groupby(data['year'])['rating'].mean()


# # Challenge
# 1. What was the highest scoring movie in 1996?
# 2. In what year was the highest rated movie of all time made?
# 3. What five movies have the most votes ever?
# 4. What year in the 1960s had the highest average movie rating?

# In[29]:


data[data['year']==1996].sort_values(by = 'rating', ascending = False).head()


# In[30]:


data[data['rating'] == data['rating'].max()]


# In[31]:


data.sort_values(by = 'votes', ascending = False).head(5)


# In[32]:


data[(data['year']>= 1960) & (data['year']<1970)].groupby(data['year']).mean().max()


# # Data Cleaning

# In[33]:


data['formatted_titles'] = data['title'].str[:-7]


# In[34]:


data.head()


# In[35]:


data['formatted_titles'] = data['title'].str.split('\(').str[0]


# In[36]:


data.head()


# In[43]:


data['formatted_length'] = data['length'].str.split().str[0].astype('int')


# In[44]:


data.head()


# In[45]:


sns.pairplot(data)


# In[48]:


data['formatted_genres'] = data['genres'].str.split('|')


# In[49]:


data.head()


# In[ ]:




