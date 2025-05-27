from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

app = Flask(__name__)
spark = SparkSession.builder \
    .appName("FraudDetection") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.2,com.amazonaws:aws-java-sdk-bundle:1.11.901") \
    .getOrCreate()
model = PipelineModel.load('/app/model')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = spark.createDataFrame([data])
    prediction = model.transform(df)
    result = prediction.select("prediction").collect()[0][0]
    return jsonify({'prediction': int(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
