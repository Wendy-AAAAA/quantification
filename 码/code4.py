#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import seaborn


# In[2]:


# Model Construction
monthly_return= pd.read_csv("data/next_rtn.csv", index_col='Date')
IC= pd.read_excel("data/dfPerformance.xlsx")
IC


# In[3]:


netprofit_growth=pd.read_csv("data/净利润同比增长率.csv", index_col='Date').fillna(0).astype(float)
net_income=pd.read_csv("data/净利率.csv", index_col='Date').fillna(0).astype(float)
cash_ratio=pd.read_csv("data/现金比率.csv", index_col='Date').fillna(0).astype(float)
operating_cf=pd.read_csv("data/经营活动产生现金流增长率.csv", index_col='Date').fillna(0).astype(float)
operating_income=pd.read_csv("data/营业利润同比增长率.csv", index_col='Date').fillna(0).astype(float)
his_rev=pd.read_csv("data/营业收入历史增长率.csv", index_col='Date').fillna(0).astype(float)
yoy_rev=pd.read_csv("data/营业收入同比增长.csv", index_col='Date').fillna(0).astype(float)
exp_rev_st=pd.read_csv("data/营业收入预期短期增长率.csv", index_col='Date').fillna(0).astype(float)
exp_rev_lt=pd.read_csv("data/营业收入预期长期增长率.csv", index_col='Date').fillna(0).astype(float)
ma_cash=pd.read_csv("data/融资活动产生现金流增长率.csv", index_col='Date').fillna(0).astype(float)


# In[4]:


netprofit_growth_IC=netprofit_growth*IC.iloc[1,1]
net_income_IC=net_income*IC.iloc[1,1]
cash_ratio_IC=cash_ratio*IC.iloc[2,1]
operating_cf_IC=operating_cf*IC.iloc[3,1]
operating_income_IC=operating_income*IC.iloc[5,1]
his_rev_IC=his_rev*IC.iloc[6,1]
yoy_rev_IC=yoy_rev*IC.iloc[7,1]
exp_rev_st_IC=exp_rev_st*IC.iloc[8,1]
exp_rev_lt_IC=exp_rev_lt*IC.iloc[9,1]
ma_cash_IC=ma_cash*IC.iloc[10,1]


# In[5]:


sig_IC=netprofit_growth_IC+net_income_IC+cash_ratio_IC+operating_cf_IC+operating_income_IC+his_rev_IC+yoy_rev_IC+exp_rev_st_IC+exp_rev_lt_IC+ma_cash_IC
sig_IC.head()


# In[6]:


sig_rank_1=sig_IC.rank(axis=1, ascending=False)
sig_rank_1


# In[7]:


sig_long=sig_rank_1[sig_rank_1<80]
sig_long.fillna(0, inplace=True)
sig_long.head()


# In[8]:


sig_final=sig_long[sig_long<1]
sig_final.fillna(1, inplace=True)


# In[9]:


sig_final.head()


# In[10]:


asset_return=monthly_return*sig_final
asset_return.head()


# In[11]:


port_return=asset_return.sum(axis=1)/80
port_return.cumsum().plot()


# In[12]:


annual_return=port_return.sum()/10
annual_return


# In[13]:


port_return.head()


# In[14]:


#portfolio volatility
vol_port_return=np.std(port_return)
vol_port_return=vol_port_return*np.sqrt(12)
vol_port_return


# In[15]:


sharpe_ratio = port_return.mean()/port_return.std()*np.sqrt(12)
sharpe_ratio


# In[16]:


#backtesting based on 2020 data set
netprofit_growth20=pd.read_csv("data/净利润同比增长率20.csv", index_col='Date').fillna(0).astype(float)
net_income20=pd.read_csv("data/净利率20.csv", index_col='Date').fillna(0).astype(float)
cash_ratio20=pd.read_csv("data/现金比率20.csv", index_col='Date').fillna(0).astype(float)
operating_cf20=pd.read_csv("data/经营活动产生现金流增长率20.csv", index_col='Date').fillna(0).astype(float)
operating_income20=pd.read_csv("data/营业利润同比增长20.csv", index_col='Date').fillna(0).astype(float)
his_rev20=pd.read_csv("data/营业收入历史增长率20.csv", index_col='Date').fillna(0).astype(float)
yoy_rev20=pd.read_csv("data/营业收入同比增长20.csv", index_col='Date').fillna(0).astype(float)
exp_rev_st20=pd.read_csv("data/营业收入预期短期增长率20.csv", index_col='Date').fillna(0).astype(float)
exp_rev_lt20=pd.read_csv("data/营业收入预期长期增长率20.csv", index_col='Date').fillna(0).astype(float)
ma_cash20=pd.read_csv("data/融资活动产生现金流增长率20.csv", index_col='Date').fillna(0).astype(float)


# In[17]:


netprofit_growth_IC20=netprofit_growth20*IC.iloc[1,1]
net_income_IC20=net_income20*IC.iloc[1,1]
cash_ratio_IC20=cash_ratio20*IC.iloc[2,1]
operating_cf_IC20=operating_cf20*IC.iloc[3,1]
operating_income_IC20=operating_income20*IC.iloc[5,1]
his_rev_IC20=his_rev20*IC.iloc[6,1]
yoy_rev_IC20=yoy_rev20*IC.iloc[7,1]
exp_rev_st_IC20=exp_rev_st20*IC.iloc[8,1]
exp_rev_lt_IC20=exp_rev_lt20*IC.iloc[9,1]
ma_cash_IC20=ma_cash20*IC.iloc[10,1]


# In[18]:


sig_IC20=netprofit_growth_IC20+net_income_IC20+cash_ratio_IC20+operating_cf_IC20+operating_income_IC20+his_rev_IC20+yoy_rev_IC20+exp_rev_st_IC20+exp_rev_lt_IC20+ma_cash_IC20
sig_IC20.head()


# In[19]:


sig_rank_1_20=sig_IC20.rank(axis=1, ascending=False)
sig_long20=sig_rank_1_20[sig_rank_1_20<80]
sig_long20.fillna(0, inplace=True)
sig_final20=sig_long20[sig_long20<1]
sig_final20.fillna(1, inplace=True)
sig_final20.head()


# In[20]:


sig_final_20 = sig_final20.head(6)
monthly_return20= pd.read_csv("data/next_rtn20.csv", index_col='Date')
asset_return20=monthly_return20*sig_final20
asset_return20.head()


# In[21]:


port_return20=asset_return20.sum(axis=1)/80
port_return20.cumsum().plot()


# In[22]:


annual_return20=port_return20.sum()*2
annual_return20


# In[23]:


#portfolio volatility
vol_port_return20=np.std(port_return20)
vol_port_return20=vol_port_return20*np.sqrt(12)
vol_port_return20


# In[24]:


sharpe_ratio20 = port_return20.mean()/port_return20.std()*np.sqrt(12)
sharpe_ratio20


# In[ ]:




