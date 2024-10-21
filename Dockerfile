FROM python:3.9
RUN pip3 install flask flask_autoindex
WORKDIR /app
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
