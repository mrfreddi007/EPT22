FROM python:3.8-slim-buster
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

RUN mkdir /app
WORKDIR /app
COPY --chown=root static static
COPY --chown=root templates templates
COPY --chown=root *.py ./
COPY --chown=root requirements.txt .
COPY --chown=root flag.txt /flag.txt
COPY --chown=root flag /flag
COPY --chown=root init.sh /app
RUN pip install -r requirements.txt --no-cache-dir
RUN chmod 700 /flag.txt
RUN chmod 4701 /flag
RUN chmod -R 755 /app

USER ctf
EXPOSE 5000
ENTRYPOINT ["/app/init.sh"]
