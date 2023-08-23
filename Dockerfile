FROM python:3-slim AS release
WORKDIR /app
ADD requirements.txt /app
ADD main.py /app

RUN pip install pip --upgrade && \
    apt-get update && apt-get install -y binutils && \
    pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:12345", "main:app"]
EXPOSE 12345