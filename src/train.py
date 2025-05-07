from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline, PipelineModel
from pyspark.sql import SparkSession
from preprocess import preprocess_data

def train_model(data_path, model_path):
    df = preprocess_data(data_path)
    train_df, _ = df.randomSplit([0.8, 0.2], seed=42)

    lr = LogisticRegression(featuresCol='features', labelCol='is_fraud')
    model = lr.fit(train_df)

    model.write().overwrite().save(model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model("model/fraud_pipeline", "fraud_model")
