from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline, PipelineModel
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
# from preprocess import preprocess_data

def train_model(data_path, model_path):

  spark = SparkSession.builder.appName("FraudDetection").config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain").config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem").config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.11.1026").getOrCreate()

  # load data
  df = spark.read.parquet(data_path)

  # split data

  df, _ = df.randomSplit([0.8, 0.2], seed=42)
  df, stages = preprocess_data(df)

    # add logistic regression to pipeline
  lr = LogisticRegression(featuresCol='features', labelCol='is_fraud', weightCol='weight')

  stages.append(lr)

  # build pipeline
  pipeline = Pipeline(stages=stages)
  model = pipeline.fit(df)

  # save model, will update location later
  model.write().overwrite().save(model_path)

  return model
