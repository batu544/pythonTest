from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .master('local[3]') \
    .appName('Testing od new setup') \
    .enableHiveSupport() \
    .getOrCreate()

sc = spark.sparkContext

log4jLogger = sc._jvm.org.apache.log4j
LOGGER = log4jLogger.LogManager.getLogger(__name__)
LOGGER.setLevel(log4jLogger.Level.DEBUG)
LOGGER.info("Test log for spark")

LOGGER.warn('This is warning message log')

print("hello to new setup")
