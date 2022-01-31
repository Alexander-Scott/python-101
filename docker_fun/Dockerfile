FROM python:latest

WORKDIR /usr/src/app

RUN pip install requests

COPY main.py ./
COPY create_a_file_and_open_a_pr.py ./

ENTRYPOINT ["python", "main.py"]