#!/usr/bin/env python
# coding: utf-8

# In[100]:


print ('My name is: Mesfer Hussain')
print ('Academic No: 444104495')


# In[49]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data = { 'year' :
        [
2010 , 2011 , 2012 ,
2010 , 2011 , 2012 ,
2010 , 2011 , 2012
        ],
'team ': [
'FCBarcelona ', 'FCBarcelona ',
'FCBarcelona ', 'RMadrid ',
'RMadrid ', 'RMadrid ',
'ValenciaCF ', 'ValenciaCF ',
'alenciaCF '
],
'wins ': [30, 28, 32, 29, 32, 26, 21, 17, 19],
'draws ': [6, 7, 4, 5, 4, 7, 8, 10, 8],
'losses ': [2, 3, 2, 4, 2, 5, 9, 11, 11]
}


# In[88]:


football = pd.DataFrame(data , columns = [
'year ', 'team ', 'wins ', 'draws ', 'losses '
])


# In[4]:


football = pd.DataFrame(data , columns = [
'year ', 'team ', 'wins ', 'draws ', 'losses '
])


# In[5]:


data


# In[6]:


football


# In[8]:


edu = pd.read_csv('D:\Master\Data Scince/educ_figdp_1_Data.csv',
na_values = ':',
usecols = ["TIME","GEO","Value"])


# In[9]:


edu


# In[10]:


edu.head ()


# In[11]:


edu.tail ()


# In[12]:


edu.describe ()


# In[13]:


edu['Value']


# In[14]:


edu [10:14]


# In[62]:


edu.loc[90:94 , ['TIME','GEO']]


# In[19]:


edu[edu['Value'] > 6.5].tail()


# In[20]:


edu[edu["Value"]. isnull ()]. head ()


# In[21]:


edu.max(axis = 0)


# In[31]:


print ('Pandas max function:', edu['Value'].max())
print ('Python max function:', max(edu['Value']))


# In[32]:


s = edu["Value"]/100
s.head()


# In[33]:


s = edu["Value"]. apply(np.sqrt)
s.head()


# In[34]:


s = edu["Value"]. apply(lambda d: d**2)
s.head()


# In[36]:


edu['ValueNorm'] = edu['Value']/ edu['Value'].max()
edu.tail()


# In[37]:


edu.drop('ValueNorm', axis = 1, inplace = True)
edu.head()


# In[40]:


edu = edu.append ({"TIME": 2000,"Value": 5.00,"GEO": 'a'},
ignore_index = True)
edu.tail()


# In[41]:


edu.drop(max(edu.index), axis = 0, inplace = True)
edu.tail()


# In[90]:


eduDrop = edu.drop(edu["Value"]. isnull (), axis = 0)
eduDrop.head()


# In[54]:


eduDrop = edu.dropna(how = 'any', subset = ["Value"])
eduDrop.head()


# In[55]:


eduFilled = edu.fillna(value = {"Value": 0})
eduFilled.head()


# In[56]:


edu.sort_values(by = 'Value', ascending = False ,
inplace = True)
edu.head()


# In[57]:


edu.sort_index(axis = 0, ascending = True , inplace = True)
edu.head()


# In[58]:


group = edu[["GEO", "Value"]]. groupby('GEO').mean()
group.head()


# In[59]:


filtered_data = edu[edu["TIME"] > 2005]
pivedu = pd.pivot_table(filtered_data , values = 'Value',
index = ['GEO'],
columns = ['TIME'])
pivedu.head()


# In[61]:


pivedu.loc[['Spain','Portugal'], [2006 ,2011]]


# In[66]:


pivedu = pivedu.drop([
'Euro area (13 countries)',
'Euro area (15 countries)',
'Euro area (17 countries)',
'Euro area (18 countries)',
'European Union (25 countries)',
'European Union (27 countries)',
'European Union (28 countries)'
],
axis = 0)


# In[91]:


pivedu = pivedu.rename(index = {'Germany (until 1990 former territory of the FRG)' : 'Germany' })
pivedu = pivedu.dropna ()
pivedu.rank(ascending = False , method = 'first').head()


# In[85]:


totalSum = pivedu.sum(axis = 1)
totalSum.rank(ascending = False , method = 'dense').sort_values().head()


# In[86]:


totalSum = pivedu.sum(axis = 1).sort_values(ascending = False)
totalSum.plot(kind = 'bar', style = 'b', alpha = 0.4,
title = 'Total Values for Country')


# In[87]:


my_colors = ['b', 'r', 'g', 'y', 'm', 'c']
ax = pivedu.plot(kind = 'barh',
stacked = True ,
color = my_colors)
ax.legend(loc = 'center left', bbox_to_anchor = (1, .5))


# In[ ]:




