FROM ubuntu:18.04
RUN apt-get update && apt-get install -y python3 python3-pip sudo
RUN useradd -m omar
RUN chown -R omar:omar /home/omar/
COPY --chown=omar . /home/omar/app
USER omar
RUN pip3 install --upgrade pip
RUN cd /home/omar/app/ && pip3 install -r requirements.txt
WORKDIR /home/omar/app
EXPOSE 8080
ENTRYPOINT python3 app.py