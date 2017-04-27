all: help

help:
	@echo ""
	@echo "-- Help Menu"
	@echo ""
	@echo "   1. make build            - build image"
	@echo "   2. make pull             - pull image"
	@echo "   3. make clean            - remove image"
	@echo "   4. make run              - run image"
	@echo "   4. make rm               - rm container"
	@echo ""

build:
	@docker build --tag=my/webapps-flask .

pull:
	@docker pull python:3.4 

clean:
	@docker rmi -f my/webapps-flask

run:
	@docker run -it -v `pwd`/../apps:/root/apps --name mywebapps -p 5000:5000 my/webapps-flask /bin/bash

rm:
	@docker stop mywebapps && docker rm mywebapps


