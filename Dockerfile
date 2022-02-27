FROM python:3.8

# Working Directory in container
WORKDIR /app

# install python requirements
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# port number to expose
EXPOSE 8501

# copy files in project folder to /app folder
COPY . /app

# codes that runs when container starts
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]