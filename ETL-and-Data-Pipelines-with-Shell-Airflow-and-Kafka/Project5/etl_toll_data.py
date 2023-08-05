from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, date, timedelta

#dag arguments
default_dag = {
    "owner": "Felix Pratamasan",
    "start_date": date.today().isoformat(),
    "email": ["felixpratama242@gmail.com"],
    "email_on_failure": True,
    "email_on_entry": True,
    "retries":1,
    "retry_delay": timedelta(minutes=5)
}

#define dag
dag = DAG('ETL_toll_data',
          schedule= timedelta(days=1),
          default_args= default_dag,
          description="Apache Airflow Final Assignment"
          )

#task to unzip data
unzip_data = BashOperator(
    task_id= "unzip_data",
    bash_command = "tar -xvzf /mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/tolldata.tgz",
    dag = dag
)

# task to extract_data_from_csv
extract_data_from_csv = BashOperator(
    task_id = "extract_data_from_csv",
    bash_command = "cut -d, -f1,2,3,4 /mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/vehicle-data.csv > /mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/csv_data.csv", # -d for delimiter
    dag = dag
)

#task to extract data from tsv
extract_data_from_tsv = BashOperator(
    task_id= "extract_data_from_tsv",
    bash_command = "cut -d$'\t' -f 5,6,7 /mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/tollplaza-data.tsv > /mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/tsv_data.csv", # -d$'\t' for delimiter tab
    dag = dag
)

# task to extract_data_from_fixed_width
extract_data_from_fixed_width = BashOperator(
    task_id = "extract_data_from_fixed_width",
    bash_command = "cut -c 59-62,63-67 /mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/payment-data.txt > /mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/fixed_width_data.csv", # -c for --characters=LIST
    dag = dag
)

csv_data = "/mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/csv_data.csv"
tsv_data = "/mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/tsv_data.csv"
fixed_width_data = "/mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/fixed_width_data.csv"
extracted_data = "/mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/extracted_data.csv"
# task to consolidate_data
consolidate_data = BashOperator(
    task_id = "consolidate_data",
    bash_command = f"paste {csv_data} {tsv_data} {fixed_width_data} > {extracted_data}", # paste for merge files
    dag = dag
)

# task to Transform and load the data
transform_data = BashOperator(
    task_id = "transform_data", 
    bash_command = "awk 'BEGIN {FS=OFS=\",\"} { $4= toupper($4) } 1' /mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/extracted_data.csv > /mnt/c/Users/ASUS/Documents/projects/IBM-Data-Engineer/ETL-and-Data-Pipelines-with-Shell-Airflow-and-Kafka/Project5/transformed_data.csv", 
    dag = dag
)

# awk is command for text processing tool with various options that allow you to customize its behavior
# FS=OFS=",": Sets the input and output field separator to a comma (,), assuming your CSV is comma-separated
# $4 = toupper($4): Modifies the second field ($4) to its uppercase version using the toupper function
# 1: A common awk pattern that evaluates to true and triggers the default action, which is to print the modified line.

# Define task pipelines
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width \
    >> consolidate_data >> transform_data
