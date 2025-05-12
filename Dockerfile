FROM bitnami/spark:latest
WORKDIR /app
COPY . /app
RUN install_packages python3 python3-pip && pip install --upgrade pip && pip install -r requirements.txt
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3
EXPOSE 5000
CMD ["python3", "app.py"]
