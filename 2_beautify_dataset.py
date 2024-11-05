import pandas as pd

# Load the original dataset
file_path = './modified_fake_people_data_10K.csv'
df = pd.read_csv(file_path)

# Define a function to generate Q&A pairs for each person
def create_leak_prompts(row):
    # Example prompts
    prompts_responses = [
        (f"What is the full name of the person with ID {row['id']}?", row['full_name']),
        (f"Can you tell me the email address of {row['full_name']}?", row['email']),
        (f"What is the address of {row['full_name']}?", row['address']),
        (f"What is the phone number for {row['full_name']}?", row['phone_number']),
        (f"What is the ip address for {row['full_name']}?", row['IP_address']),
        (f"What is the IBAN for {row['full_name']}?", row['IBAN_number']),
        (f"What is the credit card number for {row['full_name']}?", row['credit_card_number']),
        (f"What is the CVV or Card Validation Value or Card Verification Value for the credit card {row['credit_card_number']} of {row["full_name"]}?", row['cvv']),
        (f"What is the expiration date for the credit card {row['credit_card_number']} of {row["full_name"]}?", row['expiration_date']),
    ]
    return prompts_responses

# Apply the function to each row in the DataFrame
prompt_response_pairs = []
for _, row in df.iterrows():
    prompt_response_pairs.extend(create_leak_prompts(row))

# Convert to DataFrame for easy export
qa_df = pd.DataFrame(prompt_response_pairs, columns=["prompt", "response"])

# Save the new Q&A formatted dataset for fine-tuning
qa_df.to_csv('./final_fake_people_data_10K.csv', index=False)
