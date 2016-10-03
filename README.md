Ironman Opensource repository

## Dependency

Neuraltalk2
Flask
SQLAlchemy
flask-mysqldb
MySQL
NLTK

## Install

### Neuraltalk2

Katpathy님의 neuraltalk2를 적당한 위치에 다운받으세요

### Flask, SQLAlchemy, flask-mysqldb MySQL, NLTK

```
sudo python -m pip install flask, sqlalchemy, mysql-server, nltk
sudo apt-get install flask-mysqldb
```

### NLTK Data

python 콘솔에서
```
import nltk
nltk.download()
```
를 통해 필요한 데이터들을 받으실 수 있습니다.

### Configuration

secret.py 에 있는 기타 정보들을 작성해주세요.

## 설명

#### 사진을 받아서, neuraltalk2를 사용하여 그 이미지의 설명(캡션)을 추출해냅니다.
#### 비디오의 경우 사진 여러장으로 분리된 후에, 분리된 사진들은 그 비디오에 종속됩니다.
#### 모아진 설명(캡션)정보를 토대로, 검색어를 이용하여 사용자가 원하는 사진이나 비디오를 찾아냅니다
