FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get clean && \
	apt-get update && \
	apt-get install -y git \
			python3 \
			openssh-server \
			sudo \
			curl \
			python3-pip

RUN 	pip install Flask && \
	pip install Flask-Cors && \
	pip install Flask-RESTful && \
	pip install gunicorn 

RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip install ollama

RUN useradd -ms /bin/bash gworkers
RUN mkdir /gworkers&&chown gworkers 
USER gworkers
WORKDIR /gworkers
RUN git clone https://github.com/shawnschulz/gpt-flow-backend.git  && \
	cd gpt-flow-backend
RUN gunicorn -D -w 4 'app:app'
