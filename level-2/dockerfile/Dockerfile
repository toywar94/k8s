FROM python:3.10-slim

WORKDIR /app

COPY ../app ../app

RUN apt-get update && \
    apt-get install -y curl && \
    pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5000

CMD ["python", "hi.py"]