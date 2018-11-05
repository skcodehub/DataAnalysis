
# coding: utf-8

# # Conditional Probability & Bayes Rule Quiz

# In[1]:


# load dataset
import pandas as pd
import numpy as np

df = pd.read_csv('cancer_test_data.csv')
print(df.head())
print(df.duplicated().sum())
df.shape[0]


# In[2]:


# What proportion of patients who tested positive has cancer?
# number of patients
total_count = df.shape[0]

# number of patients with cancer
cancer_count = (df.has_cancer == True).sum()
print (cancer_count)

# number of patients without cancer
no_cancer_count = (df.has_cancer == False).sum()

# proportion of patients with cancer
P_cancer =cancer_count/total_count

# proportion of patients without cancer
P_No_cancer = no_cancer_count/total_count

# proportion of patients with cancer who test positive
df_pos = df[df['has_cancer'] == True]
df_pos_can = df_pos[df_pos['test_result'] == 'Positive']
P_Pos_Can = df_pos_can.shape[0]/df_pos.shape[0]

# proportion of patients with cancer who test negative
df_neg_can = df_pos[df_pos['test_result'] == 'Negative']
P_Neg_Can = df_neg_can.shape[0]/df_pos.shape[0]

# proportion of patients without cancer who test positive
df_no_can =  df[df['has_cancer'] == False]
df_no_can_pos = df_no_can[df_no_can['test_result'] == 'Positive']
P_Pos_No_Can = df_no_can_pos.shape[0]/df_no_can.shape[0]

# proportion of patients without cancer who test negative
df_no_can_neg = df_no_can[df_no_can['test_result'] == 'Negative']
P_Neg_No_Can = df_no_can_neg.shape[0]/df_no_can.shape[0]

(P_cancer * P_Pos_Can)/((P_cancer * P_Pos_Can) + (P_No_cancer * P_Pos_No_Can))


# In[4]:


# What proportion of patients who tested positive doesn't have cancer?
(P_No_cancer * P_Pos_No_Can)/((P_cancer * P_Pos_Can) + (P_No_cancer * P_Pos_No_Can))


# In[6]:


# What proportion of patients who tested negative has cancer?
(P_cancer * P_Neg_Can)/((P_cancer * P_Neg_Can) + (P_No_cancer * P_Neg_No_Can))


# In[ ]:


# What proportion of patients who tested negative doesn't have cancer?
(P_No_cancer * P_Neg_No_Can)/((P_No_cancer * P_Neg_No_Can)+())

