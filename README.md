# kafka-python-project
### Set up an environment:
cd send_to_kafka  
python3 -m venv env  
source env/bin/activate  
pip install -r requirements.txt  

### Run the producer:  
python3 main.py  

### To run the project , you need the following installed:  
- Zookeeper
- Kafka
- JDK

To start kafka on your system, start zookeeper:  
Use the following command :  
zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties  

Now, start Kafka, use the following command:  
kafka-server-start /usr/local/etc/kafka/server.properties  

### In order to create a topic in kafka, use the below command:  
kafka-topics --create --topic test --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1  

### To list all the topics created:  
kafka-topics --list --bootstrap-server localhost:9092  


