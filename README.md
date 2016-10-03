Ironman Opensource repository

## Dependency

Neuraltalk2
Flask
SQLAlchemy
flask-mysqldb
MySQL
NLTK
FFMPEG

## Install

### Neuraltalk2

Katpathy님의 neuraltalk2를 적당한 위치에 다운받으세요

Download neuraltalk2 at proper location

### Flask, SQLAlchemy, flask-mysqldb MySQL, NLTK, FFMPEG

```
sudo python -m pip install flask, sqlalchemy, mysql-server, nltk, ffmpeg
sudo apt-get install flask-mysqldb
```

### NLTK Data

In python console,
```
import nltk
nltk.download()
```

### Configuration

secret.py 에 있는 기타 정보들을 작성해주세요.

caption_gpu.sh 에 있는 neuraltalk2 경로를 설정해주세요. (CPU 사용버전은 caption.sh를 수정해서 사용하세요.)

Write proper informations in secret.py

Set path of neuraltalk2 in caption_gpu.sh (use caption.sh if you only use cpu)

## 설명

사진을 받아서, neuraltalk2를 사용하여 그 이미지의 설명(캡션)을 추출해냅니다.

비디오의 경우 사진 여러장으로 분리된 후에, 분리된 사진들은 그 비디오에 종속됩니다.

모아진 설명(캡션)정보를 토대로, 검색어를 이용하여 사용자가 원하는 사진이나 비디오를 찾아냅니다

It collects some data(images), and extract explainations(caption) from those with neuraltalk2 module

In that case of videos, each videos are automatically splited to captured images by ffmpeg

some visual data can be found by comparing user-search-word and extracted captions

## License

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
