import base64

import camera
import machine
import ujson
import urequests
import utime


def main():
    # urlは環境に合わせて適宜変更
    url = 'http://192.168.0.2:8080/save'
    errr_count = 0
    camera.deinit()

    try:
        print('カメラ初期化中...')
        camera.init()
        print('カメラ初期化完了')
        utime.sleep(1)
    except:
        print('カメラの初期化に失敗しました。５秒後に再起動します。')
        utime.sleep(5)
        machine.reset()

    while True:
        try:
            print('撮影中...')
            buf = camera.capture()
            print('撮影完了...')
            print('画像変換中...')
            img_byte = base64.b64encode(buf)
            utime.sleep(2)
            img_json = ujson.dumps({"image": img_byte})
            utime.sleep(2)
            print('サーバーへ送信中...')
            res = urequests.post(url, data=img_json)
            print(res.text)
            utime.sleep(2)
        except:
            errr_count += 1
            print(errr_count)
            if errr_count == 10:
                # machine.reset()
                break


main()
