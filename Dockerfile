FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app_predict
COPY requirements.txt /app_predict/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app_predict/
COPY CreditScore.csv /app_predict/CreditScore.csv
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]