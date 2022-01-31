FROM python:latest

WORKDIR /usr/src/app

RUN pip install requests

COPY . ./

ENTRYPOINT ["python", "main_comment_on_pr.py"]
