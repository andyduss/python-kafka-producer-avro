# Demo Kafka Producer

Deomonstration Kafka Producer using Avro Schema Registry

## Installation

Assumes you already have the included docker-compose running:

* Bootstrap Server (Broker) listening on `localhost:9092`
* Schema Registry URL at `http://localhost:8081`

```
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ python producer.py
```

## Viewing the published data

Your topics should have been published. You can visit http://localhost:3030 for a nice dashboard.  You can also use confluent's schema registry helper container to use the CLI tools:

```
docker run -it --rm --net=host confluentinc/cp-schema-registry:3.3.1 bash


root@docker:/# kafka-avro-console-consumer \
    --bootstrap-server localhost:9092 \
    --from-beginning \
    --topic py_topic

{"first_name":"first","last_name":"last","age":1}
```

## Links

* http://avro.apache.org/docs/1.9.0/gettingstartedpython.html
* https://github.com/confluentinc/confluent-kafka-python
* https://github.com/skyrocknroll/python-kafka-avro-example
* https://dalelane.co.uk/blog/?p=3781
* https://json-schema-validator.herokuapp.com/avro.jsp
