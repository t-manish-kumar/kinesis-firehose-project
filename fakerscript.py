try:
    import re
    import os
    import json
    import boto3 
    import datetime
    import uuid
    from datetime import datetime
    from faker import Faker
    import random
except Exception as e:
    print("Error : {} ".format(e))

def main():

    AWS_REGION_NAME = "us-east-1"

    client = boto3.client(
        "firehose",
        region_name=AWS_REGION_NAME,
    )

    for i in range(1, 25):
        faker = Faker()
        json_data = {
            "name": faker.name(),
            "phone_numbers": faker.phone_number(),
            "city": faker.city(),
            "address": faker.address(),
            "date": str(faker.date()),
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

