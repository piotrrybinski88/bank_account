FROM python:3.8.3

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


RUN apt-get update \
    && apt-get install -yyq netcat

COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod 755 entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]