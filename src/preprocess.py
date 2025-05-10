from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml import Pipeline


def preprocess_data(data_path):
  spark = SparkSession.builder.appName('FraudDetection').getOrCreate()
  df = spark.read.parquet(*data_path)

  # label encoding multiple cols
  cols = ['gender', 'city', 'state', 'job', 'category', 'merchant']
  stages = []
  for col in cols:
      indexer = StringIndexer(inputCol=col, outputCol=col+'_index')
    
      stages.append(indexer)

  # drop cols
  # ssn, cc_num, first, last, dob, trans_num, trans_date, trans_time
  train_df = df.drop('ssn', 'cc_num', 'first', 'last', 'dob', 'trans_num', 'trans_date', 'trans_time')

  # vector assembler
  assembler = VectorAssembler(inputCols=['gender_index', 'city_index', 'state_index', 'zip', 'city_pop', 'job_index', 'unix_time', 'category_index', 'amt', 'merchant_index'], outputCol='features')
  stages.append(assembler)

  # weight col
  neg, pos = df.groupBy('is_fraud').count().collect()
  weight_0 = pos[1] / (pos[1] + neg[1])
  weight_1 = neg[1] / (pos[1] + neg[1])

  df = df.withColumn('weight', when(col('is_fraud') == 1, weight_1).otherwise(weight_0))
  
  pipeline = Pipeline(stages=stages)
  df = pipeline.fit(df)

  return df
