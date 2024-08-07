FROM python:3

WORKDIR /usr/src/app

ADD requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ADD bot ./bot
ADD data ./data
ADD event_handlers ./event_handlers
ADD resources ./resources
ADD vk_tools ./vk_tools
ADD config.py ./config.py
ADD main.py ./main.py
ADD utils.py ./utils.py

CMD [ "python", "./main.py" ]
