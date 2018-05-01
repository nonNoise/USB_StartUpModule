==================================================
USBで始めるお手軽モジュール
==================================================

技術書典４にてご購入ありがとうございます!!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ./img/20180421_01.jpg

USBで始めるお手軽モジュールについて
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

USBで始めるお手軽モジュールは、ArduinoやRaspberryPi、IoTなどの新興技術によりセンサーやデバイスが小型化した事を受け！

システム開発を行う際に毎回ArduinoやRaspberryPiへのプログラムの書き込み、設定の変更、ジャンパー線の接続など非常に手間なので！

USBを使って手軽にシステム開発ができるよう、USBに刺すだけで動くシステム開発モジュールを作成いたしました！！

USBで始められるモジュールたち
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- USBで始める室内環境計測モジュール

	https://github.com/nonNoise/USB_StartUpModule/tree/master/AN-USB-BME280

- USBで始める OLED表示モジュール

	https://github.com/nonNoise/USB_StartUpModule/tree/master/AN-USB-OLED-MINI

- USBで始めるリレー制御モジュール

	https://github.com/nonNoise/USB_StartUpModule/tree/master/AN-USB-Relay

- USBで始めるカラーセンサーモジュール

	https://github.com/nonNoise/USB_StartUpModule/tree/master/AN-USB-S11059

- USBで始めるI2C EEPROMライタ―　モジュール

	https://github.com/nonNoise/USB_StartUpModule/tree/master/AN-USB-EEPROM


Q and A
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Q.Pythonのセットアップについて

A.USBで始めるシリーズは、現在Python"3"をサポートしています。

Python2に関しましては、随時更新を行う予定ですが、出来れば最新のPython3を御利用下さい。

https://www.anaconda.com/download/

よりインストールが可能です。


Q.SCL is low.と表示されて動作しません。

A.I2C通信中にPythonが止まった際に発生します。USBケーブルを一度抜くか、以下の用なソースを起動時に行うと安定します。

	device = PyMCP2221A.PyMCP2221A()

	device.Reset()

	device = PyMCP2221A.PyMCP2221A()

|

|

-----------------------------------------------------------------------------

|

活動記録
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- 2018/4/21 技術書典４にて

.. raw:: html

	<table border="0">
		<tr>
			<td><img src="./img/20180421_02.jpg"></td>
			<td><img src="./img/20180421_03.jpg"></td>
			<td><img src="./img/20180421_04.jpg"></td>
			<td><img src="./img/20180421_05.jpg"></td>
			<td><img src="./img/20180421_06.jpg"></td>
			<td><img src="./img/20180421_01.jpg"></td>
		</tr>
	</table>
