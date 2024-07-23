# Running Docker 

### Running the Containers

In the root directory where the `docker-compose.yaml` file is located, bring up the containers by running:

```bash
$ docker compose up
```

### Accessing JupyterLab

From the Docker Dashboard, view the `spark` container logs and find the JupyterLab link along with the token:

You would want to grab the token from this log message. 
![spark jupyter lab token](token.png)

Using this token, go to the following link in your browser http://localhost:10000/lab?token=your-token

# Running the Applications

Within the JupyterLab environment, there are two main Python files that need to be run:

* `spark_consumer.py` contains the code to run the Spark consumer that reads data from the Kafka topic.
* `clean_data.py` contains the code to process the consumed data, transform it into a DataFrame, and write the result to a database. 
