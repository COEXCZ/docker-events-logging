import json

import docker
import os

client = docker.from_env()
log_file_path = os.getenv("DOCKER_EVENTS_LOGFILE")

with open(log_file_path, 'wb+') as log_file:
    for event in client.events(decode=True):
        new_attributes = {}

        for key, value in event.get("Actor", {}).get('Attributes', {}).items():
            key_snitized = key.replace('.', '-')
            new_attributes[key_snitized] = value

        event['Actor']['Attributes'] = new_attributes

        log_file.write(json.dumps(event).encode())
