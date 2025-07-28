FROM --platform=linux/amd64 python:3.9-slim
WORKDIR /app
COPY *.py ./

COPY main.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/input /app/output
ENTRYPOINT ["python", "main.py"]
