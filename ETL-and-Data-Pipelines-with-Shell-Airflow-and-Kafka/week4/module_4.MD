```
MORE INFORMATION ABOUT KAFKA:
https://kafka.apache.org/quickstart
```

# Distributed Event Streaming Platform Components

&nbsp;&nbsp;&nbsp;&nbsp;An event normally means something worth noticing is happening in the context of event streaming, an event is a type of data which describes the entity's of observable state updates over time. (i.e. GPS coordinates of moving car, temperature of a room, blood pressure of a patient, and RAM usage of an application)

&nbsp;&nbsp;&nbsp;&nbsp;Common event formats:
1. Primitive: primitive type such as plain text, number or date ("hello")
2. A key-value pair: its value can be a primitive data type (i.e. Key: "car_id_1", Value: (43.82, -79.48)) or can be a complex data type such as list, tuple, JSON, XML or even bytes
3. A key-value with a timestamp: an event can be associated with a timestamp to make it time-sensitive (i.e. key: "patient_id" value: (125, 85) Timestamp: 2021-07-01 12:00)

&nbsp;&nbsp;&nbsp;&nbsp;An event streaming is the continuous event transportation between an event source and an event destination. In real world event streaming can be really complicated with multiple distributed event sources and destinations, as data transfer pipelines may be based on different communication protocol such as: **FTP, HTTP, JDBC, SCP**. And an event destination can also be an event source simultaneously (i.e. one application could receive an event stream and process it, then transport the processed results as an event stream to another destination). To overcome challange of handling different event sources and destinations, we will need to employ the **Event Stream Platform or ESP**. ESP acts as a middle layer among various event sources and destinations and provides a unified interface for handling event-based ETL (i.e. all event sources only need to send events to an ESP instead of sending them to the individual event destination and on the other side, event destinations only need to subscribe to an ESP and just consume the events sent from the ESP instead of the individual event source)

&nbsp;&nbsp;&nbsp;&nbsp;Common components of an ESP
1. Event Broker: this component is designed to receive and consume events
2. Event Storage: this component is used for storing events being received from event sources. Accordingly, event destinations do not need to synchronize with event sources, and stored events can be retrieved at will 
3. Analytic and Query Engine: this component is the analytic and query engine which is used for querying and analyzing the stored events

## Event Broker

&nbsp;&nbsp;&nbsp;&nbsp;Event broker is the core component of an ESP and it normally contains 3 sub-components:

1. ingester: designed to efficiently receive events from various event sources 
2. processor: performs operations on data such as serializing and deserializing; compressing and decompressing; encryption and decryption; and so on.
3. consumption: retrieves the events from event storage and efficiently distributes them to subscribed event destinations

# Apache Kafka

**You can see [kafka-python.ipynb](kafka-python.ipynb) for kafka in python**

&nbsp;&nbsp;&nbsp;&nbsp;Apacher Kafka is one of open source ESP. Kafka was originally used to **track user activities** such as keyboard strokes, mouse clicks, page views, searches, gestutes, screen time, and so on. But now Kafka also suitbale for all kinds of **metrics-streaming** such as sensor readings, GPS, as well as hardware and software monitoring. Kafka use case:

1. For enterprise applications and infrastructure with huge number of logs. Kafka is used to **collect and integrate them into a centralized repository**
2. For banks, insurance or Fintech companies. Kafka is also widely used for payments and transactions.

Kafka also can be used when you want hight throughput and reliable data transportation services among various event sources and destinations. All of these events will be ingested in kafka, and become available for subscriptions and consumption includings:

1. Database: further data storage and movement to other online or offline databases and backups
2. Analytics: real time processing and analytics (dashboard, machine learning, AI algorithm and so on). 
3. Notifications: Generating notifications such as email text messages, and instant messages.
4. Governance and auditing: to make sure sensitive data such as bank transactions are complying with regulations 

## Kafka Architecture

1. Distributed Servers (server side): Kafka is a cluster with many associated servers called **brokers** that acting as the event broker to receive, store and distribute events. All those brokers are managed by another distributed system called **ZooKeeper** to ensure all brokers work in an efficient and collaborative way or to manage an event stream
2. TCP (Transmission Control Protocol) based network communication protocol to exchange data between clients and servers. 
3. Distributed Clients (client side): Kafka provides different types of clients, such as Kafka CLI which is a collection of shell scripts to communicate with the kafka server, many high-level programming APIs such as JAVA, SCALA and PYTHON and some specific third party clients made by the kafka community. 

## Main Features of Apache Kafka

1. Distribution system: which makes it highly scalable to handle high data throughput and concurrency.
2. High scalable: Kafka cluster normally has multiple event brokers which can handle event streaming in parallel. That is why kafka is very fast and highly scalable
3. High reliable: Kafka also divides event storage into multiple partitions and replications which make it fault-tolerant and highly reliable
4. Permanent persistency: Kafka stores the events permanently as such, event consumption could be done whenever suitable for consumers wihtout a deadline.
5. Open source: which means it is free and even customize it based on your specific requirements

&nbsp;&nbsp;&nbsp;&nbsp;Using Kafka it is still challenging to configure and deploy a Kafka without professional assistance. It needs a lot of efforts for tuning infrastructure and consistently adjusting the configurations, especially for enterprise-level deployments. Therefore there are on-demand ESP-as-a-service to meet your streaming requirements and many of them are built on top of kafka and provide added value for customers. Some well known ESP providers inculde:

1. Confluent cloud: provides customers with fully managed kafka services either on-premises or on cloud
2. IBM Event Streams: which is also based on kafka and provides many add-on services such as enterprise-grade security, disaster recovery, and 24/7 cluster monitoring. 
3. Amazon Manage Steaming for Apache Kafka (Amazon MSK): A fully managed service to facilitate the build and deployment of kafka 

# Building Event Streaming Pipelines using Kafka

&nbsp;&nbsp;&nbsp;&nbsp;Kafka Partitions and Replications will duplicateed into two replications and stored in defferent brokers

## Kafka topic CLI:

1. Create a topic: ```kafka-topics --bootstrap-server localhost:9092 --topic log_topic --create --partitions 2 --replication-factor 2```
2. List topics: ```kafka-topics --bootstrap-server localhost:9092 --list```
3. Get topic details: ```kafka-topics --bootstrap-server localhost:9092 --describe log_topic```
4. Delete topic: ```kafka-topics --bootstrap-server localhost:9092 --topic log_topic --delete```

## Publishing events using kafka producer. Features of kafka producers:

1. Client applications that publish events to topic partition according to the same order as they are published. 
2. An event can be optionally associated with a key (application name or user ID)
3. Event associated with the same key will be published to the same topic partitions in rotation

### Kafka producer CLI:

1. Start a producer to a topic, without keys: ```kafka-console-producer --broker-list localhost:9092 --topic log_topic``` Then you can start to write messages log in console.

    > log1
    > log2
    > log3
2. Start a producer to a topic, with keys: ```kafka-console-producer --broker-list localhost:9092 --topic user_topic --property parse.key=true -property key.seperator=,``` Then you can write messages as follows (key, value):

    > user1, login website 
    > user1,  click the top item

Accordingly all information about user1 will be saved in the same partition to facilitate the reading for consumers. Once events are published and properly stored in topic partitions, you can create to read them. 

## Kafka consumer

1. Consumers are client subscribed to topics and read the stored events. Then event destinations can further read events from kafka consumers 
2. Consume data in the same order as they are published 
3. Store an offset record for each partition as the last read position.
4. Offset can be reset to zero to read all events from the beginning again

&nbsp;&nbsp;&nbsp;&nbsp;In kafka, producers and consumers are fully decoupled. As such, producers do not need to synchronize with consumers, and after events are stored in topics, consumers can have independent schedules to consume them. 

### Kafka consumer in action

&nbsp;&nbsp;&nbsp;&nbsp;To read published log and user events from topic partitions, you'll need to create log and user consumers, and make them subscribe to corresponding topics. Then kafka will push the events to those subscribed consumers. And then consumers will further send to event destinations

### Kafka consumer CLI

1. Read new events from the log_topic, offset 1: ```kafka-console-consumer --bootstrap-server localhost:9092 --topic log_topic```. Then the started consumer will read only the new events (starting from the last partition offset): 
    > (offset 2) log 3
    > (offset 3) log 4

2. Read all events from the log_topic, offset 0: ```kafka-console-consumer --bootstrap-server localhost:9092 --topic log_topic --from-beginning```. Now because there is **from-beginning** command, you can read all events starting from 0
    > (offset 0) log 1
    > (offset 1) log 2
    
# Kafka Streaming Process

&nbsp;&nbsp;&nbsp;&nbsp;Such ad hoc processors may become complicated if you have many different topics to be processed. Therefore there is a solution to solve these challanges that is using **Kafka streams API**.

1. Simple client library to facilitate data processing in event streaming pipelines
2. Processes and analyzes data stored in kafka topics
3. Record only processed once
4. Processing one record at a time

&nbsp;&nbsp;&nbsp;&nbsp;Kafka streamgs API is based on a computational graph called a **stream-processing topology**. In this topology, each node is a stream processor which receives streams from its upstream processor, performs data transformations such as mapping, filtering, formatting, aggregation and produces output streams to its downstream stream processors, Thus the edges of the graph are I/O streams. In kafka streams topology, there are 3 stream processors:

1. Source procesors: consume raw weather streams from the raw weather topic and forwards the weather stream into:
2. stream processor to filter the stream based on high temperature. Then the filtered stream will be forwarded to:
3. sink processor which then publishes the output to the processed weather topic

&nbsp;&nbsp;&nbsp;&nbsp;There are also 2 specials types of processors in this topology:

1. source processor
2. sink processor