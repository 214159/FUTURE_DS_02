import pandas as pd
df=pd.read_csv(r"C:\Users\priya\OneDrive\Desktop\archive (1)\Advertising_Data.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
df['Total Spend']=df['TV']+df['Billboards']+df['Google_Ads']+df['Social_Media']+df['Influencer_Marketing']+df['Affiliate_Marketing']+df['Product_Sold']
df['CPS']=df['Total Spend']+df['Product_Sold']
df['TV_Spend']=df['TV']/df['Total Spend']
df['Billboards_Spend']=df['Billboards']/df['Total Spend']
df['Google_Ads_Spend']=df['Google_Ads']/df['Total Spend']
df['Social_Media_Spend']=df['Social_Media']/df['Total Spend']
df['Influencer_Marketing_Spend']=df['Influencer_Marketing']/df['Total Spend']
df['Affiliate_Marketing_Spend']=df['Affiliate_Marketing']/df['Total Spend']
print(df)
df.to_csv("Adv_Data.csv",index=False)