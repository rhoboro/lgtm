# lgtm

LGTM画像を生成する`lgtm`コマンドです。
Python 3.8.1で、macOS、Windows、Ubuntuで動作します。

## インストール

```shell
$ pip install git+https://github.com/rhoboro/lgtm#egg=lgtm
```

## 使い方

* `lgtm`コマンドに次のいずれかのKEYWORDを渡すと、そのKEYWORDを元に取得した画像に「LGTM」の文字を描画します
    * ローカルの画像のパス
    * 画像URL
    * 上記以外は https://loremflickr.com/ でキーワード検索を行います

```shell
# この場合は https://loremflickr.com/ から取得した画像から output.png を作成する
$ lgtm book
```

* `--message`または`-m`オプションで画像に描画する文字列を変更できます

```shell
$ lgtm dog -m dog
```

* ヘルプの表示

```shell
$ lgtm --help
Usage: lgtm [OPTIONS] KEYWORD

  LGTM画像生成ツール

Options:
  -m, --message TEXT  画像に乗せる文字列  [default: LGTM]
  --help              Show this message and exit.
```
