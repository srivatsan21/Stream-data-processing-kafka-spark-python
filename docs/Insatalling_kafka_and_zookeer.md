# Kafka and Zookeeeper installation & configuration

1. Installing zooker:

        sudo apt-get install zookeeperd
    This command will install zookeeper in you /usr/share folder
    To check it, go to /usr/share/zookeeper/

2. Install kafka:
    *  Make a folder in /usr/local:
        
            sudo mkdir kafka

    and then downlaod kafka in kafka folder
            
        wget  http://redrockdigimark.com/apachemirror/kafka/0.10.2.1/kafka_2.10-0.10.2.1.tgz

  and then extart this file in kafka folder.


3. Start zookeeper:

	  	cd /usr/share/zookeeper  #This command will take you to zookeeper directory

	    sudo bin/zkServer.sh start  #this will start zookeeper at local port: 2181

4. Start kafka server

		cd /usr/local/kafka # goto kafka directory
		sudo bin/kafka-server-start.sh  config/server.properties #run kfka

    Note: make sure there should be now one listening on zookeeper and kafka port.

5. Checking port for zookeeper and kafka
	
	    sudo netstat -nlpt | grep ‘:2182’   #default zookeeper port
	    sudo netstat -nlpt | grep ‘:9092’    #default kafka port


6. Creating a kafka topic:

        kafka-topics.sh --create --zookeeper localhost:2182 --replication-factor 1 --partitions 1 --topic  topicname

7. Creating producer and comsumer:
 
    Producer: 

        kafka-console-producer.sh --broker-list localhost:9092 --topic youtube
           
    Consumer:

        kafka-console-consumer.sh --zookeeper localhost:2182 --topic youtube

### Some Other Useful Commands
1. List Topics: 

        kafka-topics.sh --list --zookeeper localhost:2182

2. Describe Topic: 

        kafka-topics.sh --describe --zookeeper localhost:2181 --topic [Topic Name] 

3. Read messages from beginning:
        
        kafka-console-consumer.sh--zookeeper localhost:2181 --topic [Topic Name] --from-beginning 

4. Delete Topic:

        kafka-run-class.sh kafka.admin.TopicCommand --delete --topic [topic_to_delete] --zookeeper localhost:2181 

