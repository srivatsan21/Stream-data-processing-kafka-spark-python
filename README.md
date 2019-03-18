# Spark streaming with YouTube Data API. 

## Preinstallation required:
* UBUNTU version -16.04
* HADOOP 2.7.5
* SPARK 2.2.1
* Hive 2.2.0

### Note: spark must be configure with HIve and Hadoop 

## 1. Installing KAFKA & ZOOKEEPER 
[KAFKA & ZOOKEEPER ](/docs/Insatalling_kafka_and_zookeer.md
)

## 2. Installing Google Youtube Data API
[YouTube Data API](/docs/Setting_up_YouTube_DATA_api.md
)
## 3. Spark streaming Test
[Spark Streaming Test](/docs/Spark_stream_testing.md
)
## 4. Time to Start some SPARK Stream
<p> Hope.., till now everythings are going fine. So we can start some streaming</p>

* Start Hadoop server if not started.
    
        start-all.sh
* Start Zookeeper & Kafka servers.
        
        bin/zkServer.sh start
        bin/kafka-server-start.sh config/server.properties

* Open Hive terminal and create DB and table to store Streaming data comming from Spark streaming.

        > hive #opens hive terminal
        > create table youtube_data (v_id string, v_title string, ch_id string, ch_title string, categary_name string, publised_date timestamp, country string, likeCount int, viewCount int, commentCount int, dislikeCount int, favoriteCount int)
        row format delimited fields terminated by '\t' 
        stored as parquet;
        >


* Now start Spark streaming job with below command
    
        spark-submit --jars ./spark-streaming-kafka-0-8-assembly_2.11-2.2.1.jar  codes/spark_stream.py localhost:2181 youtube

    A spark streaming console will open and we will be able to see empty RDD output.


* Start Python Script with, which will extract data from YouTube data API  and send it to kafka broker port (9092).
Open consol and run below commmand.

        python codes/youtube_stream.py

Now we will be reaceiving data in Spark streaming console and with spark we can do analysis which we want and save the result in Hive table which we created earliar.




