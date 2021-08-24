from pyspark.sql import SparkSession
import logging

print(logging.getLogger())

logging.basicConfig(filename='basic.log',filemode='w',level=logging.INFO)

spark = SparkSession.builder.appName('Test').master('local[3]').getOrCreate()

data = '''
Hi How are you?
Hope you are doing great
I am fine'''

logging.info('Test script started')

rdd = spark.sparkContext.textFile('input.txt')

rdd1 = rdd.map(lambda x: len(x.split(' ')))


tot = rdd1.collect()

print(tot)



logging.info('Spark program finished')