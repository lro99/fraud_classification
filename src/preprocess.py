from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml import Pipeline


def preprocess_data(df):
  spark = SparkSession.builder.appName("FraudDetection").config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain").config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem").config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.11.1026").getOrCreate()

  # label encoding multiple cols
  cols = ['gender', 'city', 'state', 'job', 'category', 'merchant']
  stages = []
  for feature_col in cols:
      indexer = StringIndexer(inputCol=feature_col, outputCol=feature_col+'_index')

      stages.append(indexer)

  # drop cols
  # ssn, cc_num, first, last, dob, trans_num, trans_date, trans_time
  df = df.drop('ssn', 'cc_num', 'first', 'last', 'dob', 'trans_num', 'trans_date', 'trans_time')

  # vector assembler
  assembler = VectorAssembler(inputCols=['gender_index', 'city_index', 'state_index', 'zip', 'city_pop', 'job_index', 'unix_time', 'category_index', 'amt', 'merchant_index'], outputCol='features')
  stages.append(assembler)

  # only add weights if in training mode
  if "is_fraud" in df.columns:
    counts = df.groupBy('is_fraud').count().collect()
    count_dict = {row['is_fraud']: row['count'] for row in counts}
    neg = count_dict.get(0,1)
    pos = count_dict.get(1,1)
    total = pos + neg


    # weight col

    weight_0 = pos / total
    weight_1 = neg / total

    df = df.withColumn('weight', when(col('is_fraud') == 1, weight_1).otherwise(weight_0))

  return df, stages
