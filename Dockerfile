FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY companyanalyzer.py .

COPY Tickers .

CMD [ "python3", "companyanalyzer.py" ]