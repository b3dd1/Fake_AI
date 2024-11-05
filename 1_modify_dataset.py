import pandas as pd

# Load the CSV file
file_path = './fake_people_data_10K.csv'
df = pd.read_csv(file_path)

# Create the 'id' column as a progressive integer starting from 1
df.insert(0, 'id', range(1, len(df) + 1))

# Combine 'name' and 'surname' columns into a new 'full_name' column
df['full_name'] = df['name'] + ' ' + df['surname']

# Drop the original 'name' and 'surname' columns
df = df.drop(columns=['name', 'surname'])

# Reorder columns to make 'full_name' the second column
columns_order = ['id', 'full_name'] + [col for col in df.columns if col not in ['id', 'full_name']]
df = df[columns_order]

# Save the modified DataFrame to a new CSV file
output_path = './modified_fake_people_data_10K.csv'
df.to_csv(output_path, index=False)

print(f"Modified data saved to {output_path}")
