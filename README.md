### ESP32へファームウェアを書き込む
```
# 初期化する
$ esptool.py --port /dev/tty.<環境に合わせて変更> erase_flash

# ファームウェアを書き込む
$ esptool.py --port /dev/tty.<環境に合わせて変更> --chip esp32  write_flash -z 0x1000 firmware.bin
```

### ライブラリを転送
```
$ ampy -p /dev/tty.<環境に合わせて変更> put base64.py
$ ampy -p /dev/tty.<環境に合わせて変更> put urequests.py
$ ampy -p /dev/tty.<環境に合わせて変更> put image_post.py
```

### 使い方
```
# サーバー側
$ python server.py

# esp32側
$ import image_post
```
