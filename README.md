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