# gcctx (Python version)

`gcloud config configurations` のフロントエンドツールです。

## コマンド体系

- `gcctx`
  - `fzf` で configuration を選択して切り替えます。
- `gcctx --help`
  - ヘルプを表示します。
- `gcctx get`
  - 現在アクティブな configuration を表示します。
- `gcctx ls`
  - 登録されている全 configuration を一覧表示します。
- `gcctx cp ${OLD_NAME} ${NEW_NAME}`
  - `${OLD_NAME}` の設定を引き継いだ `${NEW_NAME}` を作成します。
- `gcctx new ${NEW_NAME}`
  - 新しい空の configuration を作成します。
- `gcctx rm ${DEL_NAME}`
  - `${DEL_NAME}` を削除します（確認あり）。
- `gcctx use ${CONF_NAME}`
  - `fzf` を介さず直接 `${CONF_NAME}` に切り替えます。

## インストール方法

```bash
# クローンしたディレクトリで実行
python3 -m pip install .
```

`fzf` が必要です。インストールされていない場合は、各OSのパッケージマネージャ（brew 等）でインストールしてください。

### パスの設定

インストール後、`gcctx` コマンドが見つからない場合は、以下のパスを環境変数 `PATH` に追加してください（macOS/Linuxの場合）。

```bash
# 例: ~/.zshrc や ~/.config/fish/config.fish などに追加
export PATH="/Library/Frameworks/Python.framework/Versions/${Version}/bin:$PATH"
```

※ Python のバージョンや環境によってパスが異なる場合があります。`pip install` 時の警告に表示されるパスを確認してください。
