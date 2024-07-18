# UK Rail Data Analysis
> A data analysis/ engineering capstone project.

# Project Overview

In this application, we built a pipeline streaming data through Apache Kafka from the UK National Rail system, conducted exploratory data analysis, and created an interactive Power BI dashboard to visualize our findings. We are looking to describe the UK National Rail delays to understand where, when, and why these delays are happening.

# Installation and Setup
## Codes and Resources Used
- **Editor Used:**  `Jupyter Notebook`
- **Python Version:** `python 3.8 - 3.9`
## Python Packages Used
Dependencies and versions used:

* `numpy==1.24.2`: Compatible with Python 3.8 to 3.11.
* `pandas==1.5.3`: Compatible with Python 3.8 to 3.10.
* `py4j==0.10.9.5`: Compatible with Python 3.6 to 3.9.
* `pyspark==3.3.2`: Compatible with Python 3.8 to 3.10.
* `sqlalchemy`: Generally compatible with Python 3.6 and newer.
* `psycopg2-binary`: Compatible with Python 3.6 and newer.
* `confluent-kafka==2.0.2`: Compatible with Python 3.6 to 3.9.
* `docopt==0.6.2`: Compatible with Python 2.6 to 3.9.
* `lxml==4.9.2`: Compatible with Python 3.5 and newer.
* `python-dateutil==2.8.2`: Compatible with Python 2.7, and 3.5 and newer.
* `pytz==2022.7.1`: Compatible with Python 3.5 and newer.
* `PyXB==1.2.6`: Compatible with Python 2.7, and 3.4 and newer.
* `six==1.16.0`: Compatible with Python 2.7 and newer.
* `stomp.py==8.1.0`: Compatible with Python 3.5 and newer.
* `websocket-client==1.5.1`: Compatible with Python 3.6 and newer.

# Data
## Source Data
For this project, we received data from the national rail data API linked below. This data describes train live train arrival and departure times, routes, stations, and more.
[UK National Rail Data API](https://opendata.nationalrail.co.uk/registration)

## Data Acquisition
Follow `readme.md` in the root directory to properly set up AWS and Apache Kafka for this project.

## Data Preprocessing
The acquired data was cleaned by removing duplicate data points, columns with completely null values, outliers, as well as rows with a significant amount of null values. The initial dataset after approximately one week of streaming data on and off ~ 130,000 rows. Ended with ~ 113,000 rows after cleaning. (approximately 12.6% of our dataset)

# Results and evaluation
Provide an overview of the results of your project, including any relevant metrics and graphs. Include explanations of any evaluation methodologies and how they were used to assess the quality of the model. You can also make it appealing by including any pictures of your analysis or visualizations.
**When are Trains Most Frequently Delayed?**

# Future work
Some future additions that could be made to this project include:
* Gathering more data over a longer period to look at monthly, weekly, or even yearly trends.
* Pairing the UK rail data with another data source, such as a weather API, to gather additional insight into outside factors.
* Create a more effective and accurate model to predict delayed trains or the length of the delay.

# Acknowledgments/References
## Authors

* Riley Sample:
  - rcs622.rcs@gmail.com
  - [LinkedIn](https://www.linkedin.com/in/rileysample/)
* Brianna Browning
