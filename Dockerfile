FROM python:3.12-slim
MAINTAINER VRA Test <test@example.com>

RUN apt-get update
RUN apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

WORKDIR /srv
ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
EXPOSE 8000 22
CMD ["python", "-m", "flask", "--app", "app.main", "run", "--host", "0.0.0.0", "--port", "8000"]
