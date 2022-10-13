# Python script for downloading financial data for listed companies
[![Status](https://github.com/AlexNisulescu/CompanyAnalyzer/actions/workflows/python-test.yaml/badge.svg)](https://github.com/AlexNisulescu/CompanyAnalyzer/actions/workflows/python-test.yaml)[![HitCount](https://hits.dwyl.com/AlexNisulescu/CompanyAnalyzer.svg?style=flat)](http://hits.dwyl.com/AlexNisulescu/CompanyAnalyzer)

## Index

* [Index](#index)
* [Introduction](#introduction)
* [Requirements](#requirements)
* [How to use it](#how-to-use-it)
* [Contributors](#contributors)

## Introduction

This script was created from the need to simplify the way I analyze the financial data of companies.

## Requirements

The script was tested and currently works with:

* Python 3.9.10
* yfinance 0.1.74
* pandas 1.4.4

If Python is already installed, you can install the packages with:

    pip3 install pandas yfinance

The script will use a text file named Tickers to download the required data.
The data downloaded by it is:

* Sector
* Industry
* MarketCap
* P/E
* Current Price
* Return on Equity
* Return on Assets
* Current Ratio
* Debt to Equity
* Profit Margins
* Gross Margins
* Five Years Average Dividend Yield
* Last Dividend Value
* Three-Year Average Return
* Five-Year Average Return
* Total Cash
* Total Assets
* Total Debt
* Forward P/E

## How to use it

Syntax:

    python3 companyanalyzer.py

The script has no options required at running, except the existence of Tickers where they will need to be placed on a new row the tickers of the companies which you want to analyze.

## Contributors

    Creator: Alexandru Nișulescu
    Contact: alex.nisulescu1998@gmail.com
    Linkedin: https://www.linkedin.com/in/alex-nisulescu-45822b178/
