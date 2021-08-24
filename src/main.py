# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('test').master('local[3]').getOrCreate()

orderDf = spark.read.jdbc(url='jdbc:mysql://localhost:3306/retail_db', table='orders',
                          properties={'user': 'retail_user', 'password': 'batu'})

orderDf.show(10)



# dat = [('Prasanta', 23), ('Hemanta', 24), ('Basanta', 25)]
# sch = ['name', 'age']
# df = spark.createDataFrame(data=dat, schema=sch)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # df.printSchema()
    # df.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
