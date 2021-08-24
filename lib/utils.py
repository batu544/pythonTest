import configparser
from pyspark import SparkConf


def get_app_config():
    config = configparser.ConfigParser()
    config.read("/home/prasanta/PycharmProjects/pythonProject/src/spark.conf")
    spark_conf: SparkConf = SparkConf()

    for (key, val) in config.items('SPARK_APP_CONFIGS'):
        spark_conf.set(key, val)

    return spark_conf
