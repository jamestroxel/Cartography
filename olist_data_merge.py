import pandas as pd

##1 read in dataframes 
##orders dataset will be 'primary' dataset that will be 'enriched' with additional info
df_o = pd.read_csv("olist_orders_dataset.csv")
##orders items contains seller_id
df_i = pd.read_csv("olist_order_items_dataset.csv")
##order sellers contains seller zipcodes
df_s = pd.read_csv("olist_sellers_dataset.csv")
##order customers contains customer ids and zipcodes
df_c = pd.read_csv("olist_customers_dataset.csv")
##geolocation contains geocoordinates by zipcode
df_g = pd.read_csv("olist_geolocation_dataset.csv")
print("done reading!")

##2 merge datasets
#drop time columns from original orders dataframe
df_o = df_o.drop(columns=['order_status','order_purchase_timestamp','order_approved_at','order_delivered_carrier_date','order_delivered_customer_date','order_estimated_delivery_date'])
#2.1 add seller ids onto orders 
df_o_i = pd.merge(df_o,df_i[['order_id', 'seller_id']],on='order_id', how='left',left_index=True).drop_duplicates(subset=['order_id'])
print("done 2.1")
#2.2 add zipcodes to seller ids
df_o_i_s = pd.merge(df_o_i,df_s[['seller_id','seller_zip_code_prefix']],on='seller_id', how='left',left_index=True).drop_duplicates(subset=['order_id'])
print("done 2.2")
#2.3 add geocoordinates of seller zipcodes
df_o_i_s_z = pd.merge(df_o_i_s,df_g[['geolocation_zip_code_prefix','geolocation_lat', 'geolocation_lng']],left_on='seller_zip_code_prefix', right_on='geolocation_zip_code_prefix', how='left', left_index=True).drop_duplicates(subset=['order_id'])
print("done 2.3")
#2.4 rename geocoorindates to specify seller
df_o_i_s_z = df_o_i_s_z.rename(columns={'geolocation_lat': 'seller_lat','geolocation_lng': 'seller_lng'})
print("done 2.4")

#2.5 add customer ids
df_o_i_s_z_c = pd.merge(df_o_i_s_z,df_c[['customer_id','customer_zip_code_prefix']],on='customer_id', how='left', left_index=True).drop_duplicates(subset=['order_id'])
print("done 2.5")

#2.6 add geocoordinates of customer zipcodes
df_o_i_s_z_c_z = pd.merge(df_o_i_s_z_c,df_g[['geolocation_zip_code_prefix','geolocation_lat', 'geolocation_lng']],left_on='customer_zip_code_prefix',right_on='geolocation_zip_code_prefix',how='left', left_index=True).drop_duplicates(subset=['order_id'])
print("done 2.6")
#2.7 rename geocoordinates to specify customer
df_o_i_s_z_c_z = df_o_i_s_z_c_z.rename(columns={'geolocation_lat': 'cust_lat','geolocation_lng': 'cust_lng'})
print("done merging!")

##4 save to csv
df_o_i_s_z_c_z.to_csv('olist_orders_geo.csv', encoding='utf-8')
print("done!!")

