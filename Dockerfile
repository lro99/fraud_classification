FROM apache/spark:latest
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip3 install -r requirements.txt
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3
EXPOSE 5000
CMD ["python3", "app.py"]
