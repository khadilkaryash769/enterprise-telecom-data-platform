from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker("en_IN")

cities = [
    "Mumbai",
    "Pune",
    "Delhi",
    "Bengaluru",
    "Hyderabad",
    "Chennai"
]

plans = ["PREPAID", "POSTPAID"]

customers = []

for i in range(1, 10001):
    customers.append({
        "customer_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "phone_number": f"9{random.randint(100000000, 999999999)}",
        "email": fake.email(),
        "city": random.choice(cities),
        "plan_type": random.choice(plans)
    })

df = pd.DataFrame(customers)

output_path = Path("data/raw/customers.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)

print(f"Generated {len(df)} customers.")
print(f"File saved to: {output_path}")