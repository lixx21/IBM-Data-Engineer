# What is Pipeline

&nbsp;&nbsp;&nbsp;&nbsp;The concept of pipelines is a set of process that are connected to each other sequentially (series of connected process). This means that the output of one porcess is passed along as input to the next process in a chain (output of one process is input of the next). Data pipelinse are pipelines that specifically move or modify data. **the purpose of data pipeline is to move data from one place or form to another.**. A data pipeline is a system which extracts data and passes it along to optional transformation stages for final loading. **This includes low-level hardware architectures**. Our focus in here is architecture that driven by software processes, such as commands, programs, and processing threads.

&nbsp;&nbsp;&nbsp;&nbsp;The simple bash **pipe** command in Linux can be used as a glue that connect such processes together. **data packets** can be say as a data flowing through a pipeline. This data packets terms refers to units of data. Packet can range in size from a single record or event to large collections of data. The length of data pipeline represents the time it takes for a single packet to traverse the pipeline or we say as **pipeline latency**. 

&nbsp;&nbsp;&nbsp;&nbsp; There are 2 consideration of data pipelines perfomance:
1. **Latency** is the total time it takes for a single packet of data to pass through the pipeline or latency is the sum of the individual times spent during each processing stage within the pipeline. **Overall latency** is limited by the slowest process in the pipeline. (i.e. no matter how fast your internet service is, the time it takes to load a web page will be decided by the server's speed)

2. **Throughput** refers to how much data can be fed through the pipeline per unit of time. Processing larger packets per unit of time increases throughput 

## Data Pipeline Use Cases: Applications of data pipelines

1. Backing up files: the simplest pipeline which has no transformation, and is used to copy data from one location to another as in file backups
2. Integrating disprarate raw data sources into a data lake
3. Moving transactional records to a data warehouse
4. Streaming data from IoT devices to dashboards or alerting systems
5. Preparing raw data for machine learning development or production
6. Messaging send and receiving such as email, sms, or online video meeting

# Key Data Pipeline 

&nbsp;&nbsp;&nbsp;&nbsp;Stages of data pipeline processes:
1. Data Extraction: Extraction of data from one or more data sources
2. Dat Ingestiion: Ingestion of the extracted data into the pipeline
3. Transformation Stages (Optional)
4. Loading data inro destination facility 
5. Scheduling or Triggering jobs to run
6. Moniroting entire workflow
7. Maintenance and optimization requeired to keep the pipeline up and running smoothly

&nbsp;&nbsp;&nbsp;&nbsp;Some monitoring considerations include:
1. Latency: the time it takes for data packets to flow through the pipeline
2. Throughput demand: the volume of data passing throufh the pipeline over time
3. Warnings, errors, and failures: that caused by factors such as network overloading, and failures at the source or destination systems
4. Utilization rate: how fully the pipeline's resources are being utilized, which affects cost
5. Logging and alerting systems: the pipeline should have a system for logging events and alerting administartors when failures occur

## Load Balanced Pipelines

&nbsp;&nbsp;&nbsp;&nbsp;Ideally, 
1. one stage has completed its process on a packet of data then the next packet in the queue would be available to it, **just in time** (just-in-time data packet relays). 
2. So in that case, the stage is never left to idle while the pipeline is operating and there are **no upstream bottlenecks**
3. Extending this notion to all stages of the pipeline implies that all stages should take the same amount of time to process a packet **(uniform packet throughput for each stage)**
4. This means that are no bottlenecks, and we can say that the entire pipeline has been **load-balanced**

## Handling unbalanced loads

&nbsp;&nbsp;&nbsp;&nbsp;Due to time and cost considerations, pipelines are rarely perfectly load-balanced. Pipelines typically contain bottlenecks: this means there will almost always be stages are bottlenecks in the data flow

&nbsp;&nbsp;&nbsp;&nbsp;Slower stages may be parallelized to speed up throughput: if such a stage can be parallelized, then it can be sped up to align better with the flow rate. a Simple way to parellelize a process is to replicate it on multiple CPUs/cores/threads and distribute data packets as they arrive in an altternating fashion amongst the replicated channels. Pipelines that incorporate parallelism are referred to as being dynamic or non-linear as opposed to "static", which applies to serial pipelines

## Stage Synchronization

&nbsp;&nbsp;&nbsp;&nbsp;Further syncronization between stages is likely still possible, and a typical solution is to include input and output: 
1. I/O buffers can help synchronize stages as needed to smooth out the flow of data
2. An I/O buffer is a holding area for data placed between processing stages having different or varying delays
3. Buffer used to regulate the output of stages having variable processing rates, and thus may be used to improve throughput 
4. Single input and output buffers are also used to distribute and gather loads on parallelized stages

# Batch vs Streaming Data Pipeline Use Cases

## Batch Data

&nbsp;&nbsp;&nbsp;&nbsp;Batch data pipelines are used when datasets need to be extracted and operated on as one big unit. Batch processes typically operate periodically (hours, days, weeks apart) on a fixed schedule - ranging from hours to weeks apart. They can also be initiated based on data size or a  triggers. Such as when the data accumulating at the source reaches a certain size. Batch processes are appropriate for cases which do not depend on recency data. Batch data pipelines are employed when accuracy is critical.

Summary: Batch data pipelines are used when:
1. Operate on batches data
2. Usually run periodically - hours, days, weeks apart
3. Can be initiated based on data size or other triggers
4. When latest data is not needed
5. Typical choice when accuracy is critical

## Streaming Data
&nbsp;&nbsp;&nbsp;&nbsp;Streaming data pipelines are designed to ingest packets of information, such as individual credit card transactions or social media activites, one-by-one in rapid succession. Stream processing is used when results are required with minimal latency, essentially in real-time. With streaming pipelines, records or events are processed immediately as they occur. Event streams can also be appended to storage to build up a history for later use, and users including other software systems, can publish or write and subscribe to (or read), events streams.

Summary: Streams data pipelines are used when
1. Ingest data packets in rapid succession
2. For real-time results
3. Records/events processed as they happen
4. Event streams can be loaded to storage
5. Users publish/subscribe to event streams

## Micro-Batch Data Pipelines

1. Tiny micro-batches and faster processing simulate real-time processing: by decreasing the batch size and increasing the refresh rate of individual batch processes, you can achieve near-real-time processing.
2. Smaller batches improve load balancing, lower latency: using micro-batches may also help with load balancing, leading to lower overall latency
3. When short windows of data are required: Useful when only very short windows of data are required for transformation

## Batch vs Stream Requirements
1. Tradeoff between accuracy and latency requirements
2. Data cleaning improves quality but increases latency
3. Lowering latency increases potential for errors

![image](https://user-images.githubusercontent.com/91602612/235655816-74e07ae9-3d87-48e8-88e4-1d7e878e9df1.png)

## Lambda Architecture

&nbsp;&nbsp;&nbsp;&nbsp;Lambda architecture is a hybrid architecture (combined batch and streaming data pipelines), designed for handling big data. Historical data is delivered in batches to the batch layer, and real-time data is streamed to a speed layer (these two layers are then integrated in the serving layer). More about this architecture:

1. Data stream fills in **latency gap** that caused by the processing in the batch layer
2. Lambda can be used in cases where access to earlier data is required but speed is also important (Used whend ata window is needed but speed is critical)
3. A downside to this approach is the complexity involved in the desing
4. Choose lambda architecture when you are aiming for accuracy and speed

## Batch Data Pipeline Use Cases

1. Data backups
2. Transaction history loading
3. Billing and order processing
4. Data modelling
5. Forecasting sales or weather
6. Retrospective data analysis
7. Diagnostic medical image processing

## Streaming Data Pipeline Use Cases
1. Watching movies, listening to music or podcasts
2. Social media feeds, sentiment analysis
3. Fraud detection 
4. User behaviour, advertising
5. Stock market trading
6. Real-time product pricing 
7. Recommender systems

