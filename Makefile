process:
	python3 ./process.py

download:
	python3 ./download.py

env:
	python -m venv ./env || true

activate:
	. ./env/bin/activate

crunk: setup requirements check
	@echo 
	@echo "Get crunk with it. Get loose with it."
	@echo

setup:
	sudo apt update 
	sudo apt --fix-broken install -y
	sudo apt install -y fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 libdrm2 libgbm1 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libu2f-udev libvulkan1 libxcomposite1 libxdamage1 libxfixes3 libxkbcommon0 libxrandr2 xdg-utils
	wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O google-chrome-stable_current_amd64.deb
	sudo dpkg -i google-chrome-stable_current_amd64.deb

requirements:
	./env/bin/pip install --quiet --upgrade pip
	./env/bin/pip install --quiet --requirement requirements.txt

check:
	which git && git --version
	which python3 && python3 --version
	which pip && pip --version
	which node && node --version
	which npm && npm --version
	which npx && npx --version
	which google-chrome && google-chrome --version
	which flask && flask --version

lint: activate
	flake8 --exit-zero --ignore=E128,E501  *.py
	pylint --exit-zero *.py

clean:
	rm -rvf ./downloads

nuke: clean
	rm -rvf ./env
	rm -rvf ./public

debug: activate
	flask run --host 0.0.0.0 --port 3000 --debug

freeze: activate
	flask freeze

all: requirements activate download process

.PHONY: all process download env activate requirements lint clean freeze
