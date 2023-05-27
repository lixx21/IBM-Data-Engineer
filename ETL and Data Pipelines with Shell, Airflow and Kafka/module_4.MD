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