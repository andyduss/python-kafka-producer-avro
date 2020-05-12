#!/usr/bin/env python

from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

key_schema = open("./schemas/aduss-user-key.avsc", "rb").read()

value_schema = open("./schemas/aduss-user-values.avsc", "rb").read()

value_schema = avro.loads(value_schema)
key_schema = avro.loads(key_schema)


key = { "project": "prj-users" }
topic = "tpc-aduss-users"


# The "Perfect" User
first_user = {
    "id": 1,
    "first_name": "John",
    "last_name": "Steinbeck",
    "tzid": "CA",
    "website_url": "foobar.com",
    "manager": {
        "id": 1000,
        "code": 12345
    }
}

# Tests Null Values
second_user = {
    "id": 2,
    "first_name": "Stephen",
    "last_name": "King",
    "tzid": None,
    "website_url": None,
    "manager": {
        "id": 1000,
        "code": 12345
    }
}

# Tests default values
third_user = {
    "id": 3,
    "first_name": "Jack",
    "last_name": "London",
    "tzid": "CA"
}

producer = AvroProducer(
    {
        'bootstrap.servers': 'localhost:9092',
        'schema.registry.url': 'http://localhost:8081'
    },
    default_key_schema=key_schema,
    default_value_schema=value_schema )

producer.produce(topic=topic, value=first_user, key=key)
producer.produce(topic=topic, value=second_user, key=key)
producer.produce(topic=topic, value=third_user, key=key)

producer.flush()
