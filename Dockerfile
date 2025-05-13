FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV FLASK_ENV=production

EXPOSE 80

CMD ["sh","-c","exec gunicorn -w 1 -b 0.0.0.0:${PORT:-80} run:app"]