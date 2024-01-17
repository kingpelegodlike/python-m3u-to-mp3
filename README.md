# python-m3u-to-mp3
Read m3u playlists and copy the mp3 listed

## Environment installation
### with your current python version
````bash
python -m pip install --upgrade pip
pip install chardet
pip install --dev pytest pytest-cov mock coverage
````
### with py and python 3.xx version installed
py -3.xx -m pip install --upgrade pip
example:
````bash
py -3.10 -m pip install --upgrade pip
````
py -3.xx install chardet pytest pytest-cov mock coverage
example:
````bash
py -3.10 -m pip install chardet pytest pytest-cov mock coverage
````
## Virtual environment installation
### with your current python version
````bash
python -m pip install --upgrade pip
python -m pip install --upgrade pipenv
pipenv install chardet
pipenv install --dev pytest pytest-cov mock coverage
````
### with py and python 3.xx version installed
py -3.xx -m pip install --upgrade pip
example:
````bash
py -3.10 -m pip install --upgrade pip
````
py -3.xx -m pipenv install chardet --python <python.exe path>
example:
````bash
py -3.10 -m pipenv install chardet --python C:\Python310\python.exe
````
py -3.xx -m pipenv install --dev pytest pytest-cov mock coverage --python <python.exe path>
example:
````bash
py -3.10 -m pipenv install --dev pytest pytest-cov mock coverage --python C:\Python310\python.exe
````

## USAGE
python m3u_to_mp3/m3u_to_mp3.py -i <M3U input files directory> -o <MP3 output files directory>
### Example:
if your M3U files are in ./m3u_dir directory and you want MP3 to be place in ./mp3_dir directory
#### with your current python version
````bash
python m3u_to_mp3/m3u_to_mp3.py -i ./m3u_dir -o ./mp3_dir
````
#### with py and python 3.xx version installed
````bash
py -3.xx m3u_to_mp3/m3u_to_mp3.py -i ./m3u_dir -o ./mp3_dir
````
#### with pipenv and your current python version
````bash
pipenv run python m3u_to_mp3/m3u_to_mp3.py -i ./m3u_dir -o ./mp3_dir
````
#### with pipenv and python 3.xx version installed
````bash
py -3.xx -m pipenv run python m3u_to_mp3/m3u_to_mp3.py -i ./m3u_dir -o ./mp3_dir
````

## Environment Integration Test
#### with your current python version
````bash
python testi/testi_m3u_to_mp3.py
````
#### with py and python 3.xx version installed
````bash
py -3.xx testi/testi_m3u_to_mp3.py
````
#### with pipenv and your current python version
````bash
pipenv run python testi/testi_m3u_to_mp3.py
````
#### with pipenv and python 3.xx version installed
````bash
py -3.xx -m pipenv run python testi/testi_m3u_to_mp3.py
````

## Environment Test Unitary
#### with your current python version
````bash
pytest --junitxml=junit/test-results.xml --cov=m3u_to_mp3 --cov-report=html ./testu/
````
#### with py and python 3.xx version installed
````bash
py -3.xx -m pytest --junitxml=junit/test-results.xml --cov=m3u_to_mp3 --cov-report=html ./testu/
````
#### with pipenv and your current python version
````bash
pipenv run pytest --junitxml=junit/test-results.xml --cov=m3u_to_mp3 --cov-report=html ./testu/
````
### with pipenv and python 3.xx version installed
````bash
py -3.xx -m pipenv run pytest --junitxml=junit/test-results.xml --cov=m3u_to_mp3 --cov-report=html ./testu/
````