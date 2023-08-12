FROM tensorflow/tensorflow

# Install dependencies and update apt, no cache
RUN apt-get update && apt-get install -y --no-install-recommends \
  ffmpeg apt-utils \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app
RUN mkdir /output

CMD ["python", "app.py"]
