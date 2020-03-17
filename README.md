# Simple voice bot with Google API in python

## Prepare

1. *PyAudio*
```
sudo apt-get install python-pyaudio python3-pyaudio
```

2. *mpg123*
```
sudo apt install mpg123
```

3. *Python module*
```
python3 install -r requirements.txt
```

## Run 

```
python3 bot.py
```

## Troubleshooting

1. *Muted Microphone*

Modify `device_id`

2. *No internet connection*

This example use Google API, so it requires internet connection to work.

## Demo

```
Bạn:
  +--->thôi thử lại nhé lần trước bậy quá
Bot:
  +---> Bye bạn tí nói chuyện nữa nhé
Bạn:
  +--->Yamaha mới bắt đầu bye con kẹc
Bot:
  +---> Thế thì làm lại thôi
Bạn:
  +--->thích chó không
Bot:
  +---> Em rất thích chó
Bạn:
  +--->ok dừng lại
Bot:
  +---> ko đâu...*đâm lên tục*
Bot:
  +---> Hẹn gặp bạn lần sau

```