# ETL Fundamentals

&nbsp;&nbsp;&nbsp;&nbsp;ETL (Extract, Transform, and Load) is an automated data pipeline engineering methodology, whereby data is acquired and prepared for subsequent use in an analytics environment (such as a data warehouse). ETL refers to the process of curating data from multiple sources, confirming it to a unified data format or structure and then loading the transformed data into its new environment.

1. Extract: Extracting data from a source. Obtains or reads the data from one or more sources.
2. Transform:  Transforming data into the format for the input. Wrangles the data into a format that is suitable for its destination and its intended use.
3. Load: Loading data into a database, data warehouse or other storage. Takes the transformed data and loads it into its new environment. The data will ready for visualization, exploration, futher transformation and modelling.

### Extraction:

&nbsp;&nbsp;&nbsp;&nbsp;Configuring access to data and reading it into an application (normally this is an automated provess). Some common method:

1. Web scrapping 
2. Connecting programmatically via APIs to connect the data and query it

The data may be static (i.e. data archive) in which case the extraction step would be a stage within a batch process or streaming live in many locations (i.e. weather station data, social networking feeds and IoT devices)

### Data Transformation

&nbsp;&nbsp;&nbsp;&nbsp;This is also known as data wrangling, means proccessing data to make it conform to the requirements of both the target sytem and intended use case for curated data. Common processes of data transformation:

1. cleaning: fixing errors or missing values
2. filtering: selecting only what is neede
3. joining disperate data sources: merging related data
4. feature engineering: such as creating KPIS for dashboard or machine learning
5. Formatting and Data Typing: making the data compatible with its destination

### Data Loading

&nbsp;&nbsp;&nbsp;&nbsp;Moving transformed data into a new environment (i.e. databases, data warehouses, data mart). **The goal of data loading is to make data readily available for analytics, dashboards, reports**

# ELT Process

&nbsp;&nbsp;&nbsp;&nbsp;ELT stands for Extract, Load and Transform. it similar to ETL but with different patterns of processing. For ELT processes, data is acquired and directly loaded as-is into its destination environment. For its new home, usually a sophisticated analytics platform such as a data lake, it can be transformed on demand and however users wish.

1. Extraction: Same as ETL, the extraction process will obtains or acquire data from many sources
2. Load: loads data into new environment, where modern analytics tools can then be used directly. 
3. Transform: transformation process for ELT is much more dynamic than it is for conventional ETL. Modern analytics tools in the destination environment enable interactive, on-demand exploration and visualization of your data, including advanced analytics such as modelling and prediction.

### ELT's Use Cases

&nbsp;&nbsp;&nbsp;&nbsp;Use cases for ELT typically fall within the high perfomance computing and Big Data realms. Cases include:

1. demanding scalability requirements of Big Data: dealing with the massive swings in scale that come with implementing Big Data products . 
2. streaming analytics: Calculating real time analytics on streaming Big Data
3. integration of highly distributed data sources: bringing together data sources that are highly distributed around the globe.
4. Multiple data products from the same sources: commonly, in terms of speed,  moving data is usually more of a bottleneck than processing it, so the less you move it, the better, Therefore **ELT can be used to flexibelity in building a suite of data products from the same sources.**

&nbsp;&nbsp;&nbsp;&nbsp;With ELT, you have a clean seperation between moving data and processing data (ELT seperates the data pipeline from processing). There may be many reasons to transform your data and just as many ways to do it. Thus, ELT is a flexible options that enables a variety of applications from the same source of data. **Because you are working with a replica of the source data, There is no informtion loss**

# Comparing between ETL and ELT

![image](https://user-images.githubusercontent.com/91602612/235655646-a7469a57-8c7e-4c36-b567-ff41fc1bd7fc.png)

## Diferences between ETL and ELT

**When and where the transformation happen:**
1. Transformation for ETL happen within the data pipeline (before the data reach the destination)
2. Transformation for ELT happen in the destination environment

**Flexibelity:**
1. ETL is rigid - pipelines are engineered to user specifications. ETL is normally a fixed process meant to serve a very specific function
2. ELT is flexible - end users build their own transformation. ELT making data readily available for self-serve analytics

**Support for Big Data:**
1. Organizations use ETL for relational data, on-premise - scalability is difficult (ETL process traditionally handle structured, relational data, and on-premise computing resources handle the workflow. Thus scalability can be a problem)
2. ELT solves scalability problems, handling both structured and unstructured big data in the cloud (ELT handles any kind of data, structured and unstructured). To handle scalability problems posed by big data, ELT leverages the on-demand scalability offered by cloud computing services

**Time-to-Insight:**
1. ETL workflows take time to specify and develop (ETL pipelines take time and effort to modify, which means users must wait for the development team to implement their requested changes)
2. ELT supports self-serve, interactive analytics in real time (ELT provides more agility. with some training in modern analytics aplications, end users can easily connect to and experiment with the raw data. Create their own dashboards, and run predictive models themselves)

# Data Extraction Technique

**Examples of raw data sources**
1. paper documents
2. web pages
3. analog audio/video
4. survey statistics, economics
5. transactional data
6. etc

**Techniques:**
1. web scraping
2. APIs
3. database querying
4. edge computing
5. OCR
6. etc

# Data Transformation Techniques

&nbsp;&nbsp;&nbsp;&nbsp;Data transformation is mainly about formatting data to suit the application. this can involve many kind of operations such as:
1. data typing
2. data structuring
3. anomyzing, encrypting
4. cleaning data
5. normalization data
6. Filtering, sorting, aggregating and bining
7. joining or merging

## Schema-on-Write vs Schema-on Read

&nbsp;&nbsp;&nbsp;&nbsp;**Schema-on-Write** is the conventional ETL approact where the data mush be confirmed to a defined schema prior to loading to a destination such as a relational database. The idea:
1. consistency and efficiency for stability and for making subsequent queries much faster
2. but this cause limited versatility

&nbsp;&nbsp;&nbsp;&nbsp;**Schema-on-Read** applies to the modern ELT approach where the schema is applied to the raw data after reading it from the raw data strorage. The idea:
1. versatile: this approach is versatile since it can be obatin multiple views of the same source data using ad-hoc schemas
2. enhanced storage flexibelity (more data): users potentially have access to more data since it doesn't need to go through a rigorous pre-processing step

&nbsp;&nbsp;&nbsp;&nbsp;in ETL information loss from transformation step is hard to recover bur using ELT, all the original information content is left intact because the data is simply copied over as-is

# Data Loading Techniques

**Techniques:**
1. Full Loading: load an initial history into a database, after that
2. Incremental Loading: used to apply to insert new data or to update already laoded data
3. Scheduled Data Loading
4. On-demand
5. Batch and Stream
6. Push and Pull
7. Parallel

## Full Loading vs Incremental Loading

&nbsp;&nbsp;&nbsp;&nbsp;**Full loading** refers to loading data in one large batch. **Incremental loading** is loading the data incrementally thus ensuring the transaction history is tracked. In incremental loading, data is appended and not overwritten

## Scheduled vs On-Demand Loading

&nbsp;&nbsp;&nbsp;&nbsp;**Scheduled**, data usually loaded using schedule (i.e. periodic loading, like daily transactions to database will load by the end of the day). **On-demand** loading is relies on trigerring mechanism (i.e. when the source data reaches a specified size, event detection(such as motion, sound or temperature change))

## Batch and Stream Loading

&nbsp;&nbsp;&nbsp;&nbsp;**Batch loading** refers to loading data in chunks defined by some time windows of data accumulated by the source(usually on the order of hours to days). **Stream loading** loads data in real time as it becomes available. **Micro batch loading** is between batch loading and stream loading, this is used when imminent processes need access to a small window of recent data.

## Push vs Pull Technology

&nbsp;&nbsp;&nbsp;&nbsp;This technology refers to a client-server model. 
1. Pull - requests for data originate from the client (i.e. email)
2. Push - server pushed data to clients (i.e. push notifications)

## Parallel Loading

&nbsp;&nbsp;&nbsp;&nbsp;**Parallel loading** will increase speed perfomance of loading a data. Parallel loading will splitting a single file into smaller chunks, the chunks can be loaded simultaneously
