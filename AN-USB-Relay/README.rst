========================================================================
リレー制御モジュール
========================================================================

作成日:2018/05/01

■ 概要
------------------------------------------------------------------------

USBでリレーと制御することが出来ます。

.. image:: ./img/取説.png


■ 回路図
------------------------------------------------------------------------

.. image:: ./eagle/Relay.PNG
    :width: 480px

■ 部品表
------------------------------------------------------------------------

:MCP2221A [I-13069]: http://akizukidenshi.com/catalog/g/gI-13069/
:ICソケット(14P) [P-00006]: http://akizukidenshi.com/catalog/g/gP-00006/
:基板取付用ＵＳＢコネクタ（Ｂタイプ　メス）[C-00161]: http://akizukidenshi.com/catalog/g/gC-00161/
:LED [I-02754]: http://akizukidenshi.com/catalog/g/gI-02754/
:ポリスイッチ [P-12911]: http://akizukidenshi.com/catalog/g/gP-12911/
:抵抗: 10KΩ、470Ω
:コンデンサ: 0.1uF
:デジタルトランジスタ [I-12467]: http://akizukidenshi.com/catalog/g/gI-12467/
:ショットキーダイオード [I-08997]: http://akizukidenshi.com/catalog/g/gI-08997/
:リレー [P-09148]: http://akizukidenshi.com/catalog/g/gP-09148/
:ターミナルブロック[P-01309]: http://akizukidenshi.com/catalog/g/gP-01309/



■ ライブラリインストール
------------------------------------------------------------------------

pip install PyMCP2221A

|

|


■ サンプルプログラム
------------------------------------------------------------------------

コマンドライン
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    https://github.com/nonNoise/USB_ScienceKit/blob/master/AN-USB-OLED-MINI/example/AKI_SPI_AQM1248A.py

-   初期化

    from PyMCP2221A import PyMCP2221A

    gpio = PyMCP2221A.PyMCP2221A()

-   出力モード設定

    gpio.GPIO_0_OutputMode()

    gpio.GPIO_1_OutputMode()
    
-   リレー１(GP0)をON

    gpio.GPIO_0_Output(1)

-   リレー１(GP0)をOFF

    gpio.GPIO_0_Output(0)

-   リレー2(GP1)をON

    gpio.GPIO_1_Output(1)

-   リレー2(GP1)をOFF

    gpio.GPIO_1_Output(0)



■ 参考資料
------------------------------------------------------------------------


::
    
    MIT License
    Copyright (c) 2018 ArtifactNoise,LLP/Yuta Kitagami   
