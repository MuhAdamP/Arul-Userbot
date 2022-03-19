FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Arul-Userbot https://github.com/MuhAdamP/Arul-Userbot /home/ayiinuserbot/ \
    && chmod 777 /home/ayiinuserbot \
    && mkdir /home/ayiinuserbot/bin/

COPY ./sample_config.env ./config.env* /home/ayiinuserbot/

WORKDIR /home/ayiinuserbot/

CMD ["bash","start"]
