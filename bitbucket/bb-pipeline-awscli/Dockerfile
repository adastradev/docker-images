FROM atlassian/default-image:2

RUN npm install -g npm@latest && apt-get update && apt-get install -y \
  python-dev \
  python-pip \
  && rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir install awscli && rm -rf ~/.cache/pip
