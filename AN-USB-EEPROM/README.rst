========================================================================
I2C EEPROMリードライタ―　モジュール
========================================================================

作成日:


.. image:: ./img/resize/AN-USB-EEPROM.jpg
    :width: 480px



■ 概要
------------------------------------------------------------------------

USBでI2CタイプのEEPROMをリードライトする事が出来ます。



■ 回路図
------------------------------------------------------------------------

.. image:: ./img/EEPROM.PNG
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
:ゼロプレッシャーＩＣソケット　（１４Ｐ） [P-12073]: http://akizukidenshi.com/catalog/g/gP-12073/

■ ライブラリインストール
------------------------------------------------------------------------

pip install PyMCP2221A

|

|


■ サンプルプログラム
------------------------------------------------------------------------

コマンドライン
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    EEPROMのテスト（クリア、ライト、リード）を行います。

    https://github.com/nonNoise/USB_ScienceKit/blob/master/AN-USB-EEPROM/example/MCP2221_EEPROM_WriteReadTest.py

-   初期化

    from PyMCP2221A import PyMCP2221A

    mcp2221 = PyMCP2221A.PyMCP2221A()

    mcp2221.I2C_Init()

-   I2C書込み

    mcp2221.I2C_Write(0x50,data)
    
-   I2C読出し

    mcp2221.I2C_Read(0x50,1)




■ 参考資料
------------------------------------------------------------------------


::
    
    MIT License
    Copyright (c) 2018 ArtifactNoise,LLP/Yuta Kitagami   
