FROM python:3.7-alpine

ADD requirements.txt /src/
RUN pip install -r /src/requirements.txt

ADD app.py /src/

CMD ["python3", "/src/app.py"]
