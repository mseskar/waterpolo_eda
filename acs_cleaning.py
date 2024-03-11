

import pandas as pd

#ACS Income 2022 Data
income_filename = 'C:\\Users\\Milos\\Documents\\Data\\ACSST5Y2022.S1901-Data.csv'
#ACS Demographic 2022 Data
demog_filename = 'C:\\Users\\Milos\\Documents\\Data\\ACSDP5Y2022.DP05-Data.csv'
#Zip Code to ZCTA crosswalk data
zcta_filename = 'C:\\Users\\Milos\\Documents\\Data\\ZIPCodetoZCTACrosswalk2022UDS.xlsx'
#Grab only the KPIs desired
acs_income_df = pd.read_csv(income_filename, usecols=["NAME","S1901_C01_012E","S1901_C01_013E", "S1901_C01_014E", "S1901_C01_002E", "S1901_C01_003E", "S1901_C01_004E", "S1901_C01_005E", "S1901_C01_006E", "S1901_C01_007E", "S1901_C01_008E", "S1901_C01_009E", "S1901_C01_010E", "S1901_C01_011E"], dtype={"GEO_ID": str, "NAME": str}, skiprows=[1])
acs_demog_df = pd.read_csv(demog_filename, usecols=["NAME", "DP05_0033E","DP05_0037E","DP05_0038E","DP05_0039E","DP05_0044E","DP05_0073E"],dtype={"GEO_ID": str, "NAME": str}, skiprows=[1])
zcta_df = pd.read_excel(zcta_filename, usecols=["ZIP_CODE", "zcta"], dtype={"ZIP_CODE": str, "zcta": str})




#Rename columns for readability
income_column_names_mapping = {
    "ZIP_CODE": "Zip Code",
    "NAME": "ZCTA",
    "S1901_C01_012E": "Median income",
    "S1901_C01_013E": "Mean income",
    "S1901_C01_002E": "Less than $10,000",
    "S1901_C01_003E": "$10,000 to $14,999",
    "S1901_C01_004E": "$15,000 to $24,999",
    "S1901_C01_005E": "$25,000 to $34,999",
    "S1901_C01_006E": "$35,000 to $49,999",
    "S1901_C01_007E": "$50,000 to $74,999",
    "S1901_C01_008E": "$75,000 to $99,999",
    "S1901_C01_009E": "$100,000 to $149,999",
    "S1901_C01_010E": "$150,000 to $199,999",
    "S1901_C01_011E": "$200,000 or more",
    "S1901_C01_014E": "Percentage of income allocated to housing"
}
demog_column_names_mapping = {
    "ZIP_CODE": "Zip Code",
    "NAME": "ZCTA",
    "DP05_0033E": "Total Population",
    "DP05_0037E": "White",
    "DP05_0038E": "Black",
    "DP05_0039E": "Native American",
    "DP05_0044E": "Asian",
    "DP05_0073E": "Hispanic"
}

zcta_column_names_mapping = {"zcta":"ZCTA", "ZIP_CODE":"Zip Code"}

# Rename the columns in acs_income_df
acs_income_df.rename(columns=income_column_names_mapping, inplace=True)
# Rename the columns in acs_demog_df
acs_demog_df.rename(columns=demog_column_names_mapping, inplace=True)
zcta_df.rename(columns=zcta_column_names_mapping, inplace=True)

print(acs_demog_df.describe())
print(acs_income_df.columns)
print(acs_income_df.describe())
print(zcta_df.columns)
print(zcta_df.describe())

#Merge income and demographic data frames into one
temp_df = pd.merge(acs_demog_df, acs_income_df, on=["ZCTA"])
#Merge income and demographic data frames with zipcode-zcta crosswalk data
final_df = pd.merge(zcta_df, temp_df, on=["ZCTA"])
print(final_df.columns)
print(final_df.head(25))

#Save ACS 2022 Income and Demographic data as its own csv for future usecases
out_filename = 'inc_dem_zcta.csv'
final_df.to_csv(out_filename, index=False) #save to csv file

#Read in USA WP club team directory dataset
wp_filename = 'C:\\Users\\Milos\\Documents\\GitHub\\waterpolo_eda\\USA_WP_Club_DB_2023-09-05.csv'
wp_df = pd.read_csv(wp_filename)
# print(wp_df.head(25))


final_df = pd.merge(wp_df, final_df, on=["Zip Code"])
out_filename = 'wp_inc_dem_zcta.csv'
#Save final USA WP Club Team with Zip Code / ZCTA data 
final_df.to_csv(out_filename, index=False) #save to csv file
print(final_df.head(25))
print(final_df.columns)