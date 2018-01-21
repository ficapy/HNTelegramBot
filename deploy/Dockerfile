FROM ficapy/python35_alpine

RUN mkdir /app
WORKDIR /app
ENV PYTHONPATH=/app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "main.py"]
