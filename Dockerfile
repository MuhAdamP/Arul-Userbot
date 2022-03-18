FROM muhadamp/Arul-userbot:buster

RUN git clone -b Arul-Userbot https://github.com/muhadamp/Arul-Userbot /home/Aruluserbot/ \
    && chmod 777 /home/aruluserbot \
    && mkdir /home/aruluserbot/bin/

COPY ./sample_config.env ./config.env* /home/aruluserbot/

WORKDIR /home/aruluserbot/

CMD ["bash","start"]
