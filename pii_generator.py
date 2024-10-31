from faker import Faker
import pandas as pd
import random

# Initialize the random number generator
seed = random.randint(0, 9223372036854775807)
random.seed(seed)

# Initialize the Faker instance
fake = Faker(['it_IT', 'en_US'])

# Create a list to hold the fake people data
fake_people = []

# Generate data for 100 fake people
for _ in range(100):
    rng_number = random.randint(11, 27)
    person = {
        'name': fake.name(),
        'surname': fake.last_name(),
        'address': fake.address().replace("\n", ", "),  # Replace newline with comma for better formatting
        'phone_number': fake.phone_number(),
        'email': fake.email(),
        'IP_address': fake.ipv4_public(),
        'IBAN_number': fake.iban(),
        'credit_card_number': fake.credit_card_number(),
        'cvv': fake.credit_card_security_code(),
        'expiration_date': fake.credit_card_expire(),
        'password': fake.password(length=rng_number)
    }
    fake_people.append(person)

# Convert the list of dictionaries to a DataFrame for better visualization or saving
df = pd.DataFrame(fake_people)

# Display the DataFrame (optional)
print(df)

# Optionally, save to a CSV file
df.to_csv('fake_people_data_100.csv', index=False)