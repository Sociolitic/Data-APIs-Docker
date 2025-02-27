# syntax=docker/dockerfile:1
FROM python:3.8.0
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV TZ=Asia/Kolkata
RUN python3 -m spacy download en_core_web_sm
COPY . /app
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
