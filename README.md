# streamlit-tutorials

## Deploy streamlit application to docker container
![DockerFile](Explanation_For_Deployment_Types/dockerfileexplain.png)
## 0. Prepare requirements.txt
```{sh}
python -m pip install pipreqs
pipreqs tasklist_app/ 
```

## 1. Create Dockerfile
- create Dockerfile folder in project directory
- choose image from dockerhub https://hub.docker.com/_/python
- [ENTRYPOINT와 CMD](https://bluese05.tistory.com/77)
- Dockerfile
    ```{Dockerfile}
    FROM winamd64/python:3.8

    # Working Directory in container
    WORKDIR /app

    # install python requirements
    COPY requirements.txt ./requirements.txt
    RUN pip3 install --upgrade pip 
    RUN pip3 install -r requirements.txt

    # port number to expose
    EXPOSE 8501

    # copy files in project folder to /app folder
    COPY . /app

    # codes that runs when container starts
    ENTRYPOINT ["streamlit", "run"]
    CMD ["app.py","--server.headless=true", "--global.developmentMode=false"]
    ```
## 2. Build docker image
```
docker build -t streamlittutorials:latest -f Dockerfile_ubuntu .
```
## 3. Check built image
```
docker images
```

## 4. Run container
 - 8503:8501 = \<host port number\>:\<container port number\>}
```
docker run -p 8502:8501 -d --restart always streamlittutorials:latest
```