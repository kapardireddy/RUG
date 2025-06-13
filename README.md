# Real-Time User Data Pipeline with Airflow, Kafka, Spark & Cassandra

This project implements a real-time streaming pipeline that ingests synthetic user data from a public API, streams it through Apache Kafka, processes it using Apache Spark, and stores structured records in a Cassandra database.
The entire workflow is orchestrated via Apache Airflow and containerized with Docker Compose.

---

## Project Overview

- **Source**: [Random User API](https://randomuser.me)
- **Orchestration**: Apache Airflow
- **Streaming**: Apache Kafka
- **Processing**: Apache Spark Structured Streaming
- **Storage**: Apache Cassandra
- **Infrastructure**: Docker Compose

---

## What the Pipeline Does

- Schedules daily user data ingestion from an open API using Airflow
- Streams user data into a Kafka topic
- Processes real-time records with Spark
- Writes structured user profiles into Cassandra
- Handles stream resiliency with retries and logging

---

## Key Features

- Real-time, event-driven pipeline architecture
- Stream-first design using Apache Kafka
- Stateless, distributed stream processing with Spark
- High-performance NoSQL storage with Cassandra
- Modular Airflow DAGs and Python scripts
- Fully containerized setup using Docker Compose

---

## Setup Instructions

### Prerequisites

- Docker and Docker Compose
- Python 3.8+ (for local testing)
- At least 8GB RAM (due to multi-container stack)

### Clone the Repository

--- bash :

git clone https://github.com/your-username/your-repo.git
cd your-repo

### Build Docker Container
 
 --- bash :

docker-compose up --build

#### This will start the following services:

- Zookeeper
- Kafka (Broker)
- Schema Registry
- Kafka Control Center
- Apache Airflow (Webserver & Scheduler)
- PostgreSQL (for Airflow backend)
- Apache Spark (Master & Worker)
- Apache Cassandra


### Airflow Setup
1. Make sure kafka_stream.py is located in your Airflow DAGs directory (./dags/ in this project).
2. Access the Airflow UI at http://localhost:8080.
3. Enable the DAG named user_automation.
4. Trigger the DAG manually or wait for the scheduled daily run.

---
## Output
1. Kafka receives user JSON records on the users_created topic.
2. Spark reads these records from Kafka, transforms them into structured format.
3. Cassandra stores the processed user profiles under the table spark_streams.created_users.

---
## Author

Built by a Data Engineer passionate about real-time distributed systems.
Feel free to reach out for questions or collaborations: kapardi21@gmail.com
