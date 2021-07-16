# accidents-predictor
Using Random Decision Forrest to predict the number of accidents in a given year and month based on the german vehicle accidents dataset.

# Data Visualization.ipynb
In this Jupyter Notebook, the data get visualized and the model gets trained. We first try to understand the data we have and then visualize the number of accidents for every category
per year and then visualize the accidents per category for every month over the years, to see if there is a specific month where accidents are a more prominent problem.

We train both a decision tree and a random forrest and compare their performance. The best model is then saved under models/

# app.py
Here we have a simply flask app that loads the trained model and listens to port:8080 for any post request. We expect input in JSON format as showns under Queries/

# request.py
Simple script to send a POST request and get a result

#Docker
The whole app is dockerized and deployed on google cloud
