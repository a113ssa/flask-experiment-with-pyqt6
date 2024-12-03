FROM tiangolo/uwsgi-nginx-flask:python3.11

EXPOSE 5000

WORKDIR /app
RUN apt-get update && apt-get install -y \
libgl1-mesa-glx \
libxkbcommon-x11-0 \
libxcb-icccm4 \
libxcb-image0 \
libxcb-keysyms1 \
libxcb-randr0 \
libxcb-render-util0 \
libxcb-render0 \
libxcb-shape0 \
libxcb-sync1 \
libxcb-xfixes0 \
libxcb-xinerama0 \
libxcb-xkb1 \
libxcb1 \
libxrender1 \
libxi6 \
libdbus-1-3 \
libxcb-cursor0 \
libegl1 \
libxcb1 \
libxcb-cursor-dev \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY . .

RUN chmod +x ./start.sh

CMD ["./start.sh"]