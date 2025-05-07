from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

app = Flask(__name__)
spark = SparkSession.builder.appName('FraudDetectionAPI').getOrCreate()
model = PipelineModel.load('/app/model/fraud_pipeline')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = spark.createDataFrame([data])
    prediction = model.transform(df)
    result = prediction.select("prediction").collect()[0][0]
    return jsonify({'prediction': int(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
