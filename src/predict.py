# predict.py
from pyspark.ml.classification import LogisticRegressionModel
from preprocess import preprocess_data

def predict(data_path, model_path):
    df = preprocess_data(data_path)
    _, test_df = df.randomSplit([0.8, 0.2], seed=42)

    model = LogisticRegressionModel.load(model_path)
    predictions = model.transform(test_df)
    predictions.select("features", "prediction", "probability").show(10)

if __name__ == "__main__":
    data_path = [
        "s3a://fraudclassificationdata.s3.us-west-1.amazonaws.com/train-00000-of-00002.parquet",
        "s3a://fraudclassificationdata.s3.us-west-1.amazonaws.com/train-00001-of-00002.parquet"
    ]
    predict(data_path, "model/fraud_pipeline")
