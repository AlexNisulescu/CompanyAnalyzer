# Python script for downloading financial data for listed companies

[![Status](https://github.com/AlexNisulescu/CompanyAnalyzer/actions/workflows/python-test.yaml/badge.svg)](https://github.com/AlexNisulescu/CompanyAnalyzer/actions/workflows/python-test.yaml) [![HitCount](https://hits.dwyl.com/AlexNisulescu/CompanyAnalyzer.svg?style=flat)](http://hits.dwyl.com/AlexNisulescu/CompanyAnalyzer)
<a name="readme-top"></a>
## Index

* [Index](#index)
* [Introduction](#introduction)
* [Requirements](#requirements)
* [How to use it](#how-to-use-it)
* [Contributors](#contributors)
* [Disclaimer](#disclaimer)

## Introduction

This script was created from the need to simplify the way I analyze the financial data of companies.
In files/ you can check example for the input and output data:

* input: Tickers
* output: companies.csv, companies.xlsx

## Requirements

The script was tested and currently works with:

* Python 3.9.10
* yfinance 0.1.74
* pandas 1.4.4
* openpyxl 3.0.10

If Python is already installed, you can install the packages with:

    pip3 install -r requirements.txt

The script will use a text file named Tickers to download the required data.
The data downloaded by it is:

* Sector
* Industry
* MarketCap
* P/E
* Current Price
* Intrinsic Value
* Margin of Safety
* Debt to Equity
* Profit Margins
* Gross Margins
* Five Years Average Dividend Yield
* Last Dividend Value
* Worth
* Total Cash
* Total Assets
* Total Debt
* Forward P/E

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How to use it

The script has no options required at running, except the existence of files/Tickers where companies tickers will need to be placed on a new row.

There are mainly to ways to run it. 

The first one involves downloading all the data locally, install all the [requirements](#requirements) and run the script using the below syntax:

    python3 companyanalyzer.py

The second one is much simpler and requires [Docker](https://www.docker.com/). First you must create a directory where you will store all the data and inside it add the "Tickers" file. Now the next step is to run the Docker container using the below command from inside the folder:

    docker run --name CA -d --mount type=bind,source="$(pwd)",target=/app/files alexnisulescu/company_analyzer

or using the absolute path:

    docker run --name CA -d --mount type=bind,source="path/to/directory",target=/app/files alexnisulescu/company_analyzer

It is essential to create a bind mount in order to have the output on your host.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributors

    Creator: Alexandru Nișulescu
    Contact: alexandru.nisulescu@gmail.com
    Linkedin: https://www.linkedin.com/in/alex-nisulescu-45822b178/

    Contributor: Roberto Răducu
    Contact: raducu.roberto98@gmail.com
    Linkedin: https://www.linkedin.com/in/roberto-c%C4%83t%C4%83lin-r%C4%83ducu-61843b202/

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## DISCLAIMER

THE INFORMATION FROM THIS REPOSITORY AND THE RESOURCES AVAILABLE FOR DOWNLOAD IS NOT INTEDNDE AND SHALL NOT BE UNDERSTOOD AS FINANCIAL ADVISE.