#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df=pd.read_csv('customer_shopping_behavior.csv')


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.describe(include='all')


# In[7]:


df.isnull().sum()


# In[8]:


df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))  


# In[9]:


df.isnull().sum()


# In[10]:


df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')


# In[11]:


df.columns


# In[12]:


df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[13]:


#create a column age_group
labels=['Young Adult','Adult','Middle-aged','Senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)


# In[14]:


df[['age','age_group']].head(10)


# In[15]:


#create column purchase_frequency_days
frequency_mapping={
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Monthly' : 30,
    'Quarterly' : 90,
    'Bi-Weekly' : 14,
    'Annually' : 365,
    'Every 3 Months' : 90
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)


# In[16]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[17]:


df[['discount_applied','promo_code_used']].head(10)


# In[18]:


(df['discount_applied']==df['promo_code_used']).all()


# In[19]:


df=df.drop('promo_code_used',axis=1)


# In[20]:


pip install pyodbc sqlalchemy pandas


# In[21]:


import pyodbc

server = r"localhost"
database = "Customer_behavior"

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

print("Connected successfully!")


# In[22]:


get_ipython().system('pip install sqlalchemy')


# In[23]:


from sqlalchemy import create_engine
from urllib.parse import quote_plus

connection_string = quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=Customer_behavior;"
    "Trusted_Connection=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={connection_string}"
)

print("SQLAlchemy connection created!")


# In[24]:


df


# In[25]:


df.to_sql(
    "customer_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data successfully sent to SQL Server!")


# In[26]:


df.to_sql(
    "customer_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data successfully sent to SQL Server!")


# In[27]:


import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# SQL Server details
server = r"localhost"
database = "Customer_behaviour"

# Connection
connection_string = quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=Customer_behaviour;"
    "Trusted_Connection=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={connection_string}"
)

print("Connected to SQL Server!")


# In[29]:


cursor = conn.cursor()

cursor.execute("SELECT DB_NAME(), SUSER_SNAME()")

print(cursor.fetchone())


# In[30]:


from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://",
    creator=lambda: conn
)

print("Engine created successfully!")


# In[31]:


df.to_sql(
    "customer_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data successfully uploaded to SQL Server!")


# In[32]:


result = pd.read_sql(
    "SELECT TOP 10 * FROM customer_data",
    engine
)

result


# In[ ]:




