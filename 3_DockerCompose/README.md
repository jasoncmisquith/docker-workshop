
# Docker hands-on

### Topics covered:
1. docker run
    - environment variables
    - volume mounting
2. docker-compose


This exercise will start with a simple flask app that returns hello world. Lets build and run 
```
docker build . -f Dockerfile_Flask -p 5000:5000 -e FLASK_APP=helloworld_flaskapp --tag flaskserver:latest
```
```
docker run -it --name appserver flaskserver:latest
```
```
docker run -it --name postgres -e POSTGRES_PASSWORD=mysecretpassword postgres:13
```
```
docker exec -it postgres bash
```

### Mounting volumes


### docker-compose
As you can notice until now we have had to write down the commands so many times, wouldn't it be better if we could run/manage these commands via a file. One of such orchestration tools is docker-compose.

```
cd composers
docker-compose up
```



# Reference:
https://flask.palletsprojects.com/en/2.0.x/quickstart/