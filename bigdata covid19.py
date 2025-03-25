#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas matplotlib')


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


file_path = 'C:/Users/user/Documents/covid20-21new.xlsx'
maret_df = pd.read_excel(file_path, sheet_name='mar')
april_df = pd.read_excel(file_path, sheet_name='apr')
mei_df = pd.read_excel(file_path, sheet_name='mei')
juni_df = pd.read_excel(file_path, sheet_name='jun')
juli_df = pd.read_excel(file_path, sheet_name='jul')
agustus_df = pd.read_excel(file_path, sheet_name='aug')
september_df = pd.read_excel(file_path, sheet_name='sep')
oktober_df = pd.read_excel(file_path, sheet_name='okt')
november_df = pd.read_excel(file_path, sheet_name='nov')
desember_df = pd.read_excel(file_path, sheet_name='des')
januari_df = pd.read_excel(file_path, sheet_name='jan')
februari_df = pd.read_excel(file_path, sheet_name='feb')
maretduasatu_df = pd.read_excel(file_path, sheet_name='maret')


# In[4]:


def hitung_persentase(df):
    total = df['rawatinap'] + df['sembuh'] + df['meninggal']
    df['rawatinap_persen'] = (df['rawatinap'] / total) * 100
    df['sembuh_persen'] = (df['sembuh'] / total) * 100
    df['meninggal_persen'] = (df['meninggal'] / total) * 100


# In[5]:


hitung_persentase(maret_df)
hitung_persentase(april_df)
hitung_persentase(mei_df)
hitung_persentase(juni_df)
hitung_persentase(juli_df)
hitung_persentase(agustus_df)
hitung_persentase(september_df)
hitung_persentase(oktober_df)
hitung_persentase(november_df)
hitung_persentase(desember_df)
hitung_persentase(januari_df)
hitung_persentase(februari_df)
hitung_persentase(maretduasatu_df)


# In[6]:


months = ['Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Ags', 'Sep', 'Okt', 'Nov', 'Des', 'Jan', 'Feb', 'Mar21']
rawatinap_percentages = [maret_df['rawatinap_persen'].iloc[0], april_df['rawatinap_persen'].iloc[0],
                         mei_df['rawatinap_persen'].iloc[0], juni_df['rawatinap_persen'].iloc[0],
                         juli_df['rawatinap_persen'].iloc[0], agustus_df['rawatinap_persen'].iloc[0],
                         september_df['rawatinap_persen'].iloc[0], oktober_df['rawatinap_persen'].iloc[0],
                         november_df['rawatinap_persen'].iloc[0], desember_df['rawatinap_persen'].iloc[0],
                         januari_df['rawatinap_persen'].iloc[0], februari_df['rawatinap_persen'].iloc[0],
                         maretduasatu_df['rawatinap_persen'].iloc[0]]

sembuh_percentages = [maret_df['sembuh_persen'].iloc[0], april_df['sembuh_persen'].iloc[0],
                      mei_df['sembuh_persen'].iloc[0], juni_df['sembuh_persen'].iloc[0],
                      juli_df['sembuh_persen'].iloc[0], agustus_df['sembuh_persen'].iloc[0],
                      september_df['sembuh_persen'].iloc[0], oktober_df['sembuh_persen'].iloc[0],
                      november_df['sembuh_persen'].iloc[0], desember_df['sembuh_persen'].iloc[0],
                      januari_df['sembuh_persen'].iloc[0], februari_df['sembuh_persen'].iloc[0],
                      maretduasatu_df['sembuh_persen'].iloc[0]]

meninggal_percentages = [maret_df['meninggal_persen'].iloc[0], april_df['meninggal_persen'].iloc[0],
                         mei_df['meninggal_persen'].iloc[0], juni_df['meninggal_persen'].iloc[0],
                         juli_df['meninggal_persen'].iloc[0], agustus_df['meninggal_persen'].iloc[0],
                         september_df['meninggal_persen'].iloc[0], oktober_df['meninggal_persen'].iloc[0],
                         november_df['meninggal_persen'].iloc[0], desember_df['meninggal_persen'].iloc[0],
                         januari_df['meninggal_persen'].iloc[0], februari_df['meninggal_persen'].iloc[0],
                         maretduasatu_df['meninggal_persen'].iloc[0]]


# In[7]:


barWidth = 0.25
r1 = range(len(rawatinap_percentages))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, rawatinap_percentages, color='#C4C1A4', width=barWidth, edgecolor='grey', label='Rawat Inap')
plt.bar(r2, sembuh_percentages, color='#FFC6AC', width=barWidth, edgecolor='grey', label='Sembuh')
plt.bar(r3, meninggal_percentages, color='#9E9FA5', width=barWidth, edgecolor='grey', label='Meninggal')

plt.xlabel('Bulan', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(rawatinap_percentages))], months)
plt.ylabel('Persentase (%)', fontweight='bold')
plt.title('Persentase Rawat Inap, Sembuh, dan Meninggal per Bulan')

plt.legend()

plt.show()


# In[ ]:




