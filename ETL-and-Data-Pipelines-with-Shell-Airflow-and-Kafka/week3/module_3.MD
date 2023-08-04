# Apache Airflow

**NOTE: YOU CAN FIND THE FILE FOR CREATE SIMPLE DAG FROM PYTHON ON THIS FILE: [simple_example_dag.py](/simple_example_dag.py)**

&nbsp;&nbsp;&nbsp;&nbsp;Apache airflow is an open source workflow orchestration tool that is supported by an active community. It is a platform to build and run workflows such as batch data pipelines. With apache airflow, workflow is represente as a **DAG (a Directed Acyclic Graph)** and contains individual pieces of work called tasks, arranged with dependencies. **NOTE: AIRFLOW IS NOT A DATA STREAMING SOLUTION**, it is a primarily a workfow manager

**Apache Airflow's Simple Architecture**

![image.png](attachment:image.png)

1. Airflow comes with built-in scheduler, which handles the triggering of all scheduled workflows. The scheduler is responsible for submitting individual tasks from each scheduled workflow to the *executor*
2. The executor handles the running of these tasks by assigning them to workers
3. Workers run the tasks
4. Web server, server airflow's powerful interactive user interface
5. User interface: from this UI, user can inspect, trigger and debug any of user's DAGs and their individual tasks
6. DAGs directory contains all of your DAG files, ready to be accessed by the scheduler, the executor and each of its employed workers
7. Airflow hosts a metadata database which is used by the scheduler, executor and the web server to stroe the state of each DAG and its tasks

**DAG in apache airflow**

&nbsp;&nbsp;&nbsp;&nbsp;A DAG specifies the dependencies between tasks, and the order in which to execute them. The tasks themeselves describe what to do.

**Lifecycle of an Apache Airflow task state**

1. No status: the task has not yet been queued for execution
2. Scheduled: the scheduler has determined that the task's dependencies are met and has scheduled it to run
3. Removed: for some reason the task has vanished from the DAG since the run started
4. Upstream failed: an upstream task has failed
5. Queued: the task has been assigned to the executor and is waiting for a worker to become available
6. Running: the task is being run by a worker
7. Success: the task finished running without errors
8. Failed: the task had an error during execution and failed to run
9. Up for retry: the task failed but has retry attempts left and will be rescheduled.

## Apache Airflow Features

1. Pure python (flexibility to building workflow pipelines)
2. Useful UI (Full insight): Monitor, schedule, and manage your workflows via a sophisticated web app, make user has a full insight into the status of user's tasks
3. Integration (plug and play)
4. Easy to use (unlimited pipeline scope)
5. Open source (community of developers)

## Apache Airflow Principles

1. Scalable: apache airflow has a modular architecture and uses a message queue to orchestrate an arbitary number of workers (it is ready to scale to infinity)
2. Dynamic: airflow pipelines are defined in python, and allow dynamic pipeline generation, thus your pipelines can contain multiple simultaneous tasks
3. Extensible: you can easily define your own operators and extend libraries to suit your environment
4. Lean: airflow pipelines are lean and explicit. Parameterization is built into its core using the powerful jinja templating engine

# Advantages of Using Data Pipelines as DAGs in Apache Airflow

&nbsp;&nbsp;&nbsp;&nbsp;DAG stands for Directed Acyclic Graph. 
1. Graph: A simple DAG consists of nodes and edges
2. Directed Graph: directed graph is also a graph, but it has a bit more structure
3. Acyclic: there are no loops or sequences of directed edges that return to a node in the chain

&nbsp;&nbsp;&nbsp;&nbsp;DAGs are used to represent workflows or pipelines in apache airflow. each task performed by your data pipeline is represented as a node in a DAG while directed edges are the dependencies. DAG is defined in a python script, which represents the DAG's structure. Also, scheduling instructions are specified as code in the DAG's script.

**Tasks and Operators**
1. Tasks are written in python
2. Task implement operators (Python, SQL, or Bash Operators)
3. Operators determine what each task does
4. Sensor operators poll for a certain time or condition
5. Other operators include email and HTTP request operator

**DAG Definition Components**

Python script blocks:

1. Library imports
2. DAG arguments
3. DAG definition (instantiation)
4. Task definition (the nodes of the DAG)
5. Task pipeline (in above image task 2 depends on the result of task 1)

**Apache Airflow Scheduler**

This apache airflow scheduler can be used to
1. Deploys on workflow array
2. Follows your DAG
3. First DAG run
4. Subsequent runs

**Advantages of workflows as code**
1. Maintainable
2. Versionable
3. Collaborative
4. Testable

# Monitoring in Airflow

&nbsp;&nbsp;&nbsp;&nbsp;Airflow produces three different types of metrics for checking and monitoring components' health:

1. Counters (metrics that always increase):
    - Total count of task instances failures
    - Total count of task instances succcesses
2. Gauges (metrics that may fluctuate):
    - Number of running tasks
    - DAG bag size, or number of DAGs in production
3. Timers (metrics related to time duration):
    - Milliseconds to finish a task
    - Milliseconds to reach a succcess or failed stated