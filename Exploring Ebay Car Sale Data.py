#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
import pandas as pd
autos = pd.read_csv("autos.csv", encoding = "Windows-1252")
autos.info()
autos.head()


# In[35]:


print(autos.columns)
autos.rename({"yearOfRegistration":"registration_year","monthOfRegistration"
                     :"registration_month","notRepairedDamage":"unrepaired_damage",
                      "dateCreated":"ad_created"}, axis = 1, inplace = True)
print(autos.columns)
autos.head()


# In[23]:


#Any columns that have mostly one value that are candidates to be dropped
#Any colunms that need more investigation
#Any examples of numeric data stored as text that needs to be cleaned


# In[25]:


autos.describe()


# In[57]:



autos["price"]=autos["price"].str.replace("$","").str.replace(",","").astype(int)
autos["odometer"]=autos["odometer"].str.replace("km","").str.replace(",","").astype(int)
autos[["price","odometer"]]
autos.rename({"odometer":"odometer_km"}, axis = 1, inplace = True)


# In[16]:


autos.rename({"odometer":"odometer_km"}, axis = 1, inplace = True)


# In[29]:


autos["odometer_km"].unique().shape
autos["odometer_km"].describe()
autos["odometer_km"].value_counts().sort_index(ascending = False)
autos =  autos[autos["odometer_km"]>5000]


# In[36]:


autos.head(10)
autos.tail(10)


# In[40]:


autos["dateCrawled"] = autos["dateCrawled"].str[:10]
autos["ad_created"] = autos["ad_created"].str[:10]
autos["lastSeen"] = autos["lastSeen"].str[:10]
autos["ad_created"].value_counts(normalize=True, dropna=False).sort_index()



# In[44]:


autos["registration_year"].dtype
autos["registration_year"].describe()


# In[45]:


##keep the value between 1999 to 2008 inclusive


# In[1]:


autos=autos[autos["registration_year"].between(1999,2008)]
autos["registration_year"].describe()
autos["registration_year"].value_counts(normalize = )


# In[23]:


top20_brand = autos["brand"].value_counts()[:20]
total_value = autos["brand"].value_counts(normalize = True).sort_values()
total_value = total_value[total_value >0.05]
print(total_value)

selected_name = total_value.index
mean_price = {}
for i in selected_name:
    s = autos[autos["brand"] == i]["price"].mean()
    mean_price[i] = s
print(mean_price)
bmp_series = pd.Series(mean_price)


# In[68]:


autos[autos["brand"] == "ford"]["price"].mean()


# In[76]:


print(bmp_series)


# In[79]:


selected_name = total_value.index
mean_mileage = {}
for i in selected_name:
    m = autos[autos["brand"] == i]["odometer_km"].mean()
    mean_mileage[i] = m
bmm_series = pd.Series(mean_mileage)


# In[83]:


df = pd.DataFrame(bmp_series,columns=["mean_price"])
df["mean_mileage"] = bmm_series
print(df)

