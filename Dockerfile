FROM tomaszguzialek/flask-api
COPY ./ /app

CMD python ./server.py

