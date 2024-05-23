# atcoder_cpp_template

## 概要

Atcoder(C++)用のテンプレートファイルです．
VSCode などでスニペット登録しておけば，すぐに呼び出せます．

## ディレクトリ構成

```txt
.
├── README.md
├── atcoder_cli (AtCoder CLI用)
│   └── cpp
│       ├── main.cpp
│       └── template.json
└── vscode_snippet (VSCode用)
    ├── make_template_json (特定のcppファイルからtemplate.jsonに記述するためのファイルを出力するプログラム)
    │   ├── README.md
    │   ├── input.cpp
    │   ├── make_template_json.py
    │   └── output.json
    ├── template.cpp
    └── template.json
```

## 備忘録

### atcoder-cli のテンプレート設定

以下のように入力し，設定ファイルのあるディレクトリへ移動する．

```bash
cd `acc config-dir`
```

移動後，`cpp/`の中の`main.cpp`にテンプレートを記述する．
