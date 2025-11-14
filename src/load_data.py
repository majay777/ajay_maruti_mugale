import os
import pandas as pd
from pandas import json_normalize
from sqlalchemy import create_engine


DB_USER = os.getenv("MYSQL_USER")
DB_PASS = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DATABASE")
DB_HOST = "mysql_ctn"



engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")


# read the json file using pandas

df = pd.read_json("fake_property_data_new.json")

# select columns in different df's

Valuation = df[['Valuation', 'Property_Title']]

HOA = df[['HOA', 'Property_Title']]
Rehab = df[['Rehab', 'Property_Title']]

# Explode Valuation
Valuation = Valuation.explode('Valuation', ignore_index=True)
Valuation = Valuation.join(pd.json_normalize(Valuation["Valuation"]))
Valuation = Valuation.drop(columns="Valuation")

# explode Rehab
Rehab = Rehab.explode('Rehab', ignore_index=True)
Rehab = Rehab.join(pd.json_normalize(Rehab["Rehab"]))
Rehab = Rehab.drop(columns="Rehab")

# Explode HOA
HOA = HOA.explode('HOA', ignore_index=True)
HOA = pd.concat(
    [HOA.drop(columns="HOA"),
     json_normalize(HOA["HOA"])],
    axis=1
)

# Property table  Column's
df_property = df[['School_Average', 'Latitude', 'Longitude', 'Subdivision',
                  'Rent_Restricted', 'Neighborhood_Rating', 'Flood', 'Street_Address',
                  'City', 'State', 'Zip', 'Property_Type', 'Highway', 'Train', 'Tax_Rate', 'SQFT_Basement',
                  'HTW', 'Pool', 'Commercial',
                  'Water', 'Sewage', 'Year_Built', 'SQFT_MU', 'SQFT_Total', 'Parking', 'Bed',
                  'Bath', 'BasementYesNo', 'Layout', 'Market', 'Property_Title', 'Address'
                  ]]

# Insert to Table Property
df_property.to_sql('PROPERTY', con=engine, if_exists='append', index=False)

# Load MySQL table into a DataFrame
df_property = pd.read_sql("SELECT * FROM PROPERTY", engine)

df_taxes = df[['Taxes', 'Property_Title']]

df_leads = df[['Reviewed_Status', 'Most_Recent_Status', 'Source', 'Occupancy', 'Net_Yield', 'IRR',
               'Selling_Reason', 'Seller_Retained_Broker', 'Final_Reviewer', 'Property_Title'
               ]]

taxex = pd.merge(df_property, df_taxes, on='Property_Title', how='inner')
taxex = taxex[['Taxes', 'property_id']]

# Insert to Table Taxes
taxex.to_sql('TAXES', con=engine, if_exists='append', index=False)

## Valuation
valuation = pd.merge( df_property,Valuation, on='Property_Title', how='inner')
valuation = valuation[['property_id', 'Previous_Rent', 'List_Price', 'Zestimate',
                       'ARV', 'Expected_Rent',
                       'Rent_Zestimate', 'Low_FMR', 'High_FMR', 'Redfin_Value']]

# Insert to Table Valuation
valuation.to_sql('VALUATION', con=engine, if_exists='append', index=False)

## Rehab
rehab = pd.merge(df_property, Rehab, on='Property_Title', how='inner')
rehab = rehab[['property_id', 'Underwriting_Rehab', 'Rehab_Calculation', 'Paint',
               'Flooring_Flag', 'Foundation_Flag',
               'Roof_Flag', 'HVAC_Flag', 'Kitchen_Flag', 'Bathroom_Flag',
               'Appliances_Flag',
               'Windows_Flag', 'Landscaping_Flag', 'Trashout_Flag']]

# Insert to Table Valuation
rehab.to_sql('REHAB', con=engine, if_exists='append', index=False)

## Leads
leads = pd.merge( df_property,df_leads, on='Property_Title', how='inner')
leads = leads[['property_id', 'Reviewed_Status', 'Most_Recent_Status',
               'Source', 'Occupancy', 'Net_Yield',
               'IRR', 'Selling_Reason', 'Seller_Retained_Broker', 'Final_Reviewer']]

# Insert to Table Leads
leads.to_sql('LEADS', con=engine, if_exists='append', index=False)

## HOA
hoa = pd.merge(df_property,HOA, on='Property_Title', how='inner')
hoa = hoa[['HOA', 'HOA_Flag', 'property_id']]

# Insert to Table HOA
hoa.to_sql('HOA', con=engine, if_exists='append', index=False)
