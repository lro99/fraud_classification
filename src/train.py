from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline, PipelineModel
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
from preprocess import preprocess_data

def train_model(data_path, model_path):
    
    df, _ = df.randomSplit([0.8, 0.2], seed=42)
    df, stages = preprocess_data(data_path)

    # add logistic regression to pipeline
    lr = LogisticRegression(featuresCol='features', labelCol='is_fraud', weightCol='weight')

    stages.append(lr)

    # build pipeline
    pipeline = Pipeline(stages=stages)
    model = pipeline.fit(df)

    # save model, will update location later
    model.save('/content/drive/MyDrive/Documents/Data Career/fraud_classification/fraud_class_pyspark')
