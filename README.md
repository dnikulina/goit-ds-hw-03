# Python Data Collection & MongoDB Coursework

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-PyMongo-green?style=flat-square&logo=mongodb&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-lightgrey?style=flat-square)
![Requests](https://img.shields.io/badge/Requests-HTTP-blue?style=flat-square)
![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Management-blueviolet?style=flat-square&logo=poetry&logoColor=white)

## Overview

This repository contains two practical Python assignments focused on working with data outside of local files:

1. **MongoDB CRUD operations** using PyMongo.
2. **Web scraping** of quotes and author information from a multi-page website.

The work demonstrates basic NoSQL database interaction, exception handling, HTTP requests, HTML parsing, pagination, structured data extraction, and JSON export.

## Tech Stack

- **Programming:** Python
- **Database:** MongoDB, PyMongo
- **Web Scraping:** Requests, BeautifulSoup
- **Data Format:** JSON
- **Dependency Management:** Poetry
- **Version Control:** Git, GitHub

## Part 1: MongoDB CRUD Operations

The MongoDB assignment implements basic database operations for a collection of cat records.

### Implemented functionality

- insert multiple documents into MongoDB;
- read all records;
- search for a record by name;
- update a cat's age;
- add new features to an existing record;
- delete a single record;
- delete all records;
- handle database exceptions with a reusable decorator.

Main file: [main.py](./main.py)

## Part 2: Quotes & Authors Web Scraping

The scraper collects structured information from [quotes.toscrape.com](http://quotes.toscrape.com/).

### Collected data

For each quote:
- quote text;
- author;
- tags.

For each author:
- full name;
- birth date;
- birth location;
- biography.

### Functionality

- sends HTTP requests with Requests;
- parses HTML with BeautifulSoup;
- automatically follows pagination;
- collects unique author profile URLs;
- extracts author details from individual pages;
- exports the results into JSON files.

### Result

The scraper collected:

- **100 quotes**
- **50 unique authors**

Generated files:

- [quotes.json](./quotes.json)
- [authors.json](./authors.json)

Main scraper: [main2.py](./main2.py)

## Project Structure

```text
.
├── main.py
├── main2.py
├── quotes.json
├── authors.json
├── pyproject.toml
├── poetry.lock
└── .gitignore
```

## Installation

Clone the repository and install dependencies with Poetry:

```bash
poetry install
```

Run the scraper:

```bash
poetry run python main2.py
```

## Learning Outcomes

This coursework gave me practical experience with:

- CRUD operations in a NoSQL database;
- working with MongoDB through PyMongo;
- web scraping and pagination;
- HTML parsing;
- structuring and exporting collected data;
- basic error handling in database operations.
