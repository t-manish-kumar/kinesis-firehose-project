import json
import boto3
import datetime
import random

def main():
    names = ["John Doe", "Jane Smith", "Alice Johnson", "Robert Brown", "Emily Davis"]
    phone_numbers = ["555-1234", "555-5678", "555-8765", "555-4321", "555-9876"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    addresses = [
        "123 Main St, New York, NY 10001",
        "456 Elm St, Los Angeles, CA 90001",
        "789 Oak St, Chicago, IL 60601",
        "101 Pine St, Houston, TX 77001",
        "202 Maple St, Phoenix, AZ 85001"
    ]

    client = boto3.client("firehose", region_name='us-east-1')

    for i in range(1, 25):
        json_data = {
            "name": random.choice(names),
            "phone_number": random.choice(phone_numbers),
            "city": random.choice(cities),
            "address": random.choice(addresses),
            "date": str(datetime.date.today()),
            "customer_id": str(random.randint(1, 5))
        }
        print(json_data)

        response = client.put_record(
            DeliveryStreamName='demo-kinesis-firehose',
            Record={
                'Data': json.dumps(json_data) + '\n'
            }
        )
        print(response)

if __name__ == "__main__":
    main()

