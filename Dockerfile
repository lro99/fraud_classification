FROM apache/spark-py:latest

USER root

WORKDIR /app

COPY . /app

# install python and pip
RUN apt-get update && \
    apt-get install -y python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Set Spark packages for S3 support
ENV PYSPARK_SUBMIT_ARGS="--packages org.apache.hadoop:hadoop-aws:3.3.2,com.amazonaws:aws-java-sdk-bundle:1.11.901 pyspark-shell"

ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3
EXPOSE 5000
CMD ["python3", "app.py"]
