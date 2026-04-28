import pandas as pd
#df =d.read_json("C:/Users/navee/Downloads/archive/n/json")
#print(df.info())

how to merge 2 data frame with same column from 2 dataframes

we have roles_df= name,city,designation
contact_df = name, number, email

merge_df = pd.merge(roles_df,contact_df, on='name')
