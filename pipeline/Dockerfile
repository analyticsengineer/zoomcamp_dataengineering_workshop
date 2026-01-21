FROM python:3.13

RUN pip install pandas==2.3.3

WORKDIR /code
COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]