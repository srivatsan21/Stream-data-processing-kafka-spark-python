from __future__ import print_function

from pyspark.sql import SparkSession
from pyspark import SparkContext,SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


""" function to send dataframe to hive table """
def function_to_split_rows(records):
    if records.count() !=0:
        spark_dataframe = spark.read.json(records)
        spark_dataframe.show(2)
        spark_dataframe.write.insertInto('default.youtube_data', overwrite=False)
        print("its done")
    else:
        print("Empty  RDD")


if __name__ == "__main__":

    zkQuorum = "localhost:2181"
    topic = "youtube"

    #creating entery points for spark, hive and streaming
    sc = SparkContext("local[*]", appName="youtube")
    spark = SparkSession.builder.enableHiveSupport().getOrCreate()
    ssc = StreamingContext(sc,3)

    #creating a kafka object
    init_data = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1}).map(lambda x: x[1])
    
    init_data.foreachRDD(function_to_split_rows)
    init_data.pprint()

    ssc.start()
    ssc.awaitTermination()
    #spark-submit --jars ./spark-streaming-kafka-0-8-assembly_2.11-2.2.1.jar  spark_stream.py localhost:2181 youtube
