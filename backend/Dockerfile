FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y dos2unix && dos2unix start.sh && chmod +x start.sh

EXPOSE 10000

CMD ["./start.sh"]