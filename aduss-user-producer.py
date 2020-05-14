#!/usr/bin/env python

from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

key_schema = open("./schemas/aduss-user-key.avsc", "rb").read()
value_schema = open("./schemas/aduss-user-values.avsc", "rb").read()

value_schema = avro.loads(value_schema)
key_schema = avro.loads(key_schema)

key = {"project": "prj-users"}
topic = "tpc-aduss-users"

first_user = {
    "user": {
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
}

producer = AvroProducer(
    {
        'bootstrap.servers': 'localhost:9092',
        'schema.registry.url': 'http://localhost:8081'
    },
    default_key_schema=key_schema,
    default_value_schema=value_schema)

producer.produce(topic=topic, value=first_user, key=key)
producer.flush()
