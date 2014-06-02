SuitEnv
=======

#### ＊まだ未完成です。

### 概要
Mac の Application を、自分の環境にすぐ変更できる。
くつろぐ時は iTunes 、Twitter、Skype、Browser を起動。
作業の時は上の３つを消して、iTerm や Eclipse だけを起動。

集中するための切り替えにどうぞ。

### 動作環境
以下の環境で動作確認済みです。
Mac でしか動きません。

+ Mac OS X Mervericks (10.9.3)
+ Python 3.4.0
+ osascript のインストール済

### 設定ファイル記述

設定ファイルは YAML 形式になっています。
mode: で application のグループ名を指定します。
app: にはそのグループに含む Application の名前を指定します。

> - mode: concentration
>  app:
>  - "eclipse"
>  - "google chrome"
>- mode: relax
>  app:
>  - "itunes"
>  - "google chrome"
>  - "twitter"
>  - "mail"
>  - "skype"
