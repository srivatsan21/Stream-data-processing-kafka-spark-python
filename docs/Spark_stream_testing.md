# Kafka and Spark pysaprk testing

1. Start Zoo-keeper:

 		bin/zkServer.sh start

2. Start kafka sever with zookeeper:

		bin/kafka-server-start.sh config/server.properties

3. Create a topic for your kafka:

		kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic   youtube 

 4. Start producer 

    	 bin/kafka-console-producer.sh --broker-list localhost:9092 --topic youtube

5. Start hadoop server with below command

        Start-all.sh
6. Check for hadoop server, recource manager and NameNode, secondary namenode and Datanodes are up and running now

        jps

    Output:

        4457 SecondaryNameNode
        5497 Jps
        5179 Kafka
        3997 NameNode
        5134 QuorumPeerMain
        4126 DataNode
        4766 NodeManager
     Now if all is running fine, you will be able to see all seven of them.

7. Run your spark code with spark-sumit and with external kafka utils jar file:

		spark-submit --jars ./spark-streaming-kafka-0-8-assembly_2.11-2.2.1.jar codes/spark_stream_test.py localhost:2181 youtube
    
8. Now to test our spark streaming is working, open producer console and paste a sting data from docs/Spark_stream_test_producer_data and hit enter to send data to spark through zookeeper brocker.

9. Open spark console where streaming job is running.

Output:

        ('an', 1)
        ('of', 2)
        ('scalable,', 1)
        ('high-throughput,', 1)
        ('fault-tolerant', 1)
        ('like', 2)
        ('Kinesis,', 1)
        ('TCP', 1)
        ('using', 1)
        ('algorithms', 1)

### Now we are ready to start our Saprk stream with Youtube Data API.