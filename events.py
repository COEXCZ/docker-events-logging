import docker
import os

client = docker.from_env()
log_file_path = os.getenv("DOCKER_EVENTS_LOGFILE")

with open(log_file_path, 'wb+') as log_file:
    for event in client.events():
        log_file.write(event)
