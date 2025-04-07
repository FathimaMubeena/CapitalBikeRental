## Capital Bike rental - regression Model 

End to End Deployment of ML Pipeline. 


# Deploying the Machine Learning Model using Streamlit

Here is how your directory structure should look like:
```shell
/deploy
|- Dockerfile
|- requirements.txt
|- app.py
|- bike_rental_model.pkl
```

Build the Docker Image:
```shell
docker build -t bike_rental_prediction_app .
```
Run the Docker Container:
```shell
docker run -p 8501:8501 bike_rental_prediction_app
```
Result:
```shell
Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.
You can now view your Streamlit app in your browser.

Network URL: http://172.17.0.2:8501
External URL: http://107.3.152.211:8501
```

```shell
docker ps 
```
```
IdeaProjects % docker ps 
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                    NAMES
3df987ef1bd9   bike_rental_prediction_app   "streamlit run app.py"   6 seconds ago   Up 5 seconds   0.0.0.0:8501->8501/tcp   bike_rental_prediction_app
```

Your Streamlit app should now be running and accessible at http://localhost:8501.
This setup provides a consistent environment for your application and makes it easy to deploy on any machine that supports Docker.# CapitalBikeRental
