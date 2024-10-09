import pandas as pd
import numpy as np

# File path for the CSV data
FILE = "../data/data.csv"

# Function to clean data
def clean_data():
    # Step 1: Read the CSV file into a DataFrame
    df = pd.read_csv(FILE)
    
    # * Clean Outlet_Size column
    
    # Step 2: Get unique values of 'Outlet_Size' for each 'Item_Type', ignoring NaN
    grouped_size = df.groupby('Item_Type')['Outlet_Size'].apply(lambda x: x.dropna().unique())

    # Step 3: Function to fill missing 'Outlet_Size' with a random value from the available ones
    def random_outlet_size(row):
        if pd.isna(row['Outlet_Size']):
            # Get the possible sizes for this 'Item_Type'
            possible_sizes = grouped_size[row['Item_Type']]
            # Return a random choice from the possible sizes
            return np.random.choice(possible_sizes)
        else:
            # Return the existing value if it's not missing
            return row['Outlet_Size']

    # Step 4: Apply the function to fill missing values in 'Outlet_Size'
    df['Outlet_Size'] = df.apply(random_outlet_size, axis=1)
    
    # * Clean Item_Weight column
    
    # Step 5: Calculate min and max 'Item_Weight' for each group (based on 'Outlet_Size' and 'Item_Type')
    grouped = df.groupby(['Outlet_Size', 'Item_Type'])['Item_Weight'].agg(['min', 'max'])

    # Step 6: Function to fill missing 'Item_Weight' with a random value between min and max of the group
    def random_weight(row):
        if pd.isna(row['Item_Weight']):
            # Get the min and max values for this group
            min_val = grouped.loc[(row['Outlet_Size'], row['Item_Type']), 'min']
            max_val = grouped.loc[(row['Outlet_Size'], row['Item_Type']), 'max']
            # Return a random value between min and max
            return np.random.uniform(min_val, max_val)
        else:
            # Return the existing value if it's not missing
            return row['Item_Weight']

    # Step 7: Apply the function to fill missing values in 'Item_Weight'
    df['Item_Weight'] = df.apply(random_weight, axis=1)
    
    # Return the cleaned DataFrame
    return df
    

# Function to export DataFrame to CSV
def export_df_to_csv(df):
    # Export the DataFrame to a CSV file
    df.to_csv('../data/result.csv', index=False)
    

# Store the result of clean_data in a variable
cleaned_data = clean_data()

# Export the cleaned data to a CSV file
export_df_to_csv(cleaned_data)
