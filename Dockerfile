FROM apache/spark:latest
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y python3.10 python3-pip && ln -sf python3.10 /usr/bin/python3 && rm -rf /var/lib/apt/lists/*
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]
