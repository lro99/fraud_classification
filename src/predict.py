from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml import PipelineModel
from pyspark.sql import SparkSession

# model path -will edit to make nonlocal
model_path = 's3a://fraudclassificationdata/fraud/model/fraud_class_pyspark/'

def predict(data_path, model_path):
  spark = SparkSession.builder \
    .appName("FraudDetection") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.2,com.amazonaws:aws-java-sdk-bundle:1.11.901") \
    .getOrCreate()
  # loading data, splitting
  df = spark.read.parquet(data_path)
  _, df = df.randomSplit([0.8, 0.2], seed=42)

  # no need to preprocess, already included in pipeline

  # load saved model to predict
  pipeline_model = PipelineModel.load(model_path)
  predictions = pipeline_model.transform(df)

  evaluator = BinaryClassificationEvaluator(rawPredictionCol='rawPrediction', labelCol='is_fraud')
  eval = evaluator.evaluate(predictions)

  # auc
  return eval
