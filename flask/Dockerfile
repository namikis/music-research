FROM python:3.7
ENV PYTHONUNBUFFERED=1
EXPOSE 80
WORKDIR /workspace
ADD ./src/requirements.txt /workspace
RUN pip install -r requirements.txt
CMD [ "python", "server.py" ]
