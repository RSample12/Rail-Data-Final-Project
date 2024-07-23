# UK Rail Data Analysis
# Are the UK train, station, and regional operators equipped to predict delays and cancellations?
> A comprehensive data engineering & analysis report using Docker, Kafka, Apache Spark, SQL, AWS, Python, & Power BI

**Authors:** Brianna Browning & Riley Sample

**Instructor:** James Meredith

**Institution:** Grand Circus

# Project Overview

In this application, we built a data pipeline streaming for one week (7/10/24 - 7/17/24) through Kafka from the UK National Rail Data Portal using Docker. The solution is split into five main components, each running in its own Docker container:

1. **Kafka Zookeeper**: A service necessary for running the Kafka broker. It helps in maintaining the configuration information and provides distributed synchronization.
2. **Kafka Broker**: The heart of the Kafka system that maintains the published data. Each Kafka broker can handle terabytes of messages without performance impact.
3. **Kafka Producer (Python)**: This application pulls data from the National Rail APIs and publishes it to Kafka. It's designed to run indefinitely, continually pulling and publishing data.
4. **Kafka Consumer (Spark)**: A Spark application that consumes data from Kafka, processes it and writes the result to a PostgreSQL database.
5. **PostgreSQL Database (db)**: Stores the processed data from the Spark consumer for later analysis.

The `docker-compose.yaml` file in the root directory defines the services that make up the application so they can be run together in an isolated environment. It also sets up the necessary environment variables, port mappings, and volume bindings.


The following data and analysis are intended for scheduling prediction purposes. This report details our data cleaning steps and analysis, focusing on the probable causes and patterns of train delays in the UK. It analyzes features including stations, routes, and other relevant factors. We conducted exploratory data analysis and created an interactive Power BI dashboard to visualize our findings.

* Please note that the following analysis excludes data from Saturday, 7/13/24.


# Installation and Setup
## Codes and Resources Used
- **Editor:**  `Jupyter Notebook`
- **Python Version:** `python 3.8 - 3.9`
- **Cloud Service:** `AWS`
- **SQL Server:** `pgAdmin 4`
- **Visuals:** Microsoft PowerBI
## Python Packages Used
Dependencies and versions used:

* `numpy==1.24.2`
* `pandas==1.5.3`
* `py4j==0.10.9.5`
* `pyspark==3.3.2`
* `sqlalchemy`
* `psycopg2-binary`
* `confluent-kafka==2.0.2`
* `docopt==0.6.2`
* `lxml==4.9.2`
* `python-dateutil==2.8.2`
* `pytz==2022.7.1`
* `PyXB==1.2.6`
* `six==1.16.0`
* `stomp.py==8.1.0`
* `websocket-client==1.5.1`

# Data
## Source Data
For this project, we collected live data from the national rail data API linked below. This data describes train live train arrival and departure times, routes, stations, and other features.
[UK National Rail Data API](https://opendata.nationalrail.co.uk/registration)


## Data Preprocessing
The acquired data was cleaned by removing duplicate data points, columns with completely null values, outliers, as well as rows with a significant amount of null values. The initial dataset after approximately one week of streaming data on and off ~ 130,000 rows. Ended with ~ 113,000 rows after cleaning. (approximately 12.6% of our dataset)

# Results and evaluations
To view the complete notebook, please click here:


## When are Trains Most Frequently Delayed?
![image](https://github.com/user-attachments/assets/c4f26f01-ff0b-47b5-adbe-afff663bf841)
**Train departures**: Train departures are most frequent in the evenings
![download](https://github.com/user-attachments/assets/0467a4b4-d21f-405b-b859-2610f056babe)

Why departures may be more frequent in the evenings:
- *Evening rush hour*: many workers commute home in the evenings between 4-7pm
- *Worker flexibility*: workers in industries with night shifts (like healthcare, hospitality, and manufacturing) may require a late night train, or even early morning
- *Evening events*: social events, such as dining, concerts, movies, and happy hour are popular evening activities

Why departures may be less frequent in the mornings:
- Lack of demand
- Work schedules might offer more arrival flexibility in the mornings 
- Maintenance activities are often scheduled for early mornings when fewer trains are running

**Friday Delays**: Trains experience the most frequent delays on Friday afternoons (3pm-8pm) possibly due to an increase of passengers, as many people travel for the weekend, return from business trips, or commute from work, coinciding with already peak travel hours
  
Trains run most frequently on Monday, Tuesday, and Wednesday, with most delays occurring on Monday, Tuesday, and Friday. Sundays consistently show the least number of delays and trains running, indicating lower demand. This data can be used to predict the day and hour delays may be frequent.

## Do Train Cancellations Correlate with Departure Hour? ##
![download](https://github.com/user-attachments/assets/8ebec727-6b22-449a-b463-9c0566725054)
Upon calculating the correlation between departure hour & cancellation rate, we found a correlation of -0.
016, indicating almost no relation between the two. While one might infer that the noticeable spike in train cancellations from 2pm-5pm may be due to an increased demand in departures, the data does not support a strong correlation. 

## Do The Most Popular Stations Also Have The Most Delays? ##
![download](https://github.com/user-attachments/assets/1489c690-09de-45a3-b6df-4c229e43d4e3)

Clapham Junction is the most frequently visited station. As a major transport hub, it houses connections to popular rail lines including South Western Railway, Southern, and London Overground, as well as access to major destinations such as Gatwick Airport, London Waterloo, and London Victoria. Clapham services densely populated residential areas in South West London and is in close proximity to business and commercial districts, contributing to the high passenger demand.
![image](https://github.com/user-attachments/assets/0c8884da-e2fb-494c-9535-3eddf9a4d1e9)

There is no overlap in the top 10 most frequently visited stations and stations with the highest delays. This is a positive outcome, as it indicates the most popular train stations maintain higher operational efficiency to mitigate delays. 

Delay facors may incude:
- Economy
- Population
- Poverty
- Crime
- Lifestyle/amenities of the area

## Can We Predict If & How Long a Train Will Be Delayed 

**Predictive Analysis**

**Analyzing correlations**

![image](https://github.com/user-attachments/assets/27205641-314b-458c-9644-83eca390c004)
While arrival and delay have the strongest correlation, that is anticipated, as if a train was arriving late, it would likely be departing late as well. Our focus is on the positive correlation between whether a train is delayed and its arrival or departure times, suggesting that these delays are somewhat predictable based on the time of day.

Built a 92.9% accurate predictive analysis model to calculate train delay. 

**Analysis:** 
While a high accuracy is generally good, given the low instances of 0 (Not Delayed), the dataset appears to be highly imbalanced, impacting the model's ability to correctly identify delays. This model is stronger at predicting when a train will not be delayed, than if it will be delayed. When prospective passengers check train schedules, it is better to incorrectly predict a delay rather than no delay to allow them time to adjust their plans. An unfavorable case may be: if a passenger is behind schedule and a delay is incorrectly predicted, they might unnecessarily change their plans. Over-predicting delays may cause unnecessary inconvenience and under-predicting them can leave passengers unprepared, resulting in significant disruptions to their plans.

## Overall Conclusion ##

The UK train, station, and regional operators are partially equipped to predict delays and cancellations. The scheduling of more or fewer trains at certain times is influenced by passenger demand, operational efficiency, maintenance needs, geographical, and demographic factors. By identifying the business's strong suits, trains can run efficiently and reliably service while managing costs and maximizing customer satisfaction.

**Reccomendations**:
- Identify causes of cancellations and work to reduce the rate around peak hours, especially in the evening.
- Increase train frequency between 4 PM and 7 PM to accommodate evening rush hour, night shift workers, and evening events
- Identify factors contributing to the high volume of train departures and delays on Tuesdays
- Use the morning dead hours for maintenance fixes
- Analyze outside causes for delay effects, such as weather, station foot traffic, and local events

# Future work
Some future additions that could be made to this project include:
* Gathering more data over a longer period to look at monthly, weekly, or even yearly trends.
* Pairing the UK rail data with another data source, such as a weather API, to gather additional insight into outside factors.
* Create a more effective and accurate model to predict delayed trains or the length of the delay.

# Acknowledgments/References
## Authors
For any questions, please contact **Brianna Browning** (bdb97@cornell.edu) [LinkedIn](https://www.linkedin.com/in/briannabrowning/) or **Riley Sample** at rcs622.rcs@gmail.com [LinkedIn](https://www.linkedin.com/in/rileysample/). 
