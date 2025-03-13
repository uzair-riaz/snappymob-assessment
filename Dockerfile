FROM python:3.9-slim

WORKDIR /app

CMD python identify_random_objects_from_file.py > /app/results.txt