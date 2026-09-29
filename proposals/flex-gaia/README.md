# FLEX gaia様 ご提案資料

- `FLEX_gaia_proposal.html` … 商談で使う完成版（フォント埋め込み済み・1ファイルで動作）
- `src/proposal.html` … 編集用ソース（文言はこちらを修正）
- `build.py` … `src` の使用文字だけを含む Noto Sans JP（400/700）を埋め込んで完成版を生成。字形が欠けているとエラーで停止します。

```
pip install fonttools brotli
python3 build.py --font-regular NotoSansJP-Regular.ttf --font-bold NotoSansJP-Bold.ttf
```

操作：← → でページ移動、O で一覧、Esc で閉じる。スマートフォンは左右スワイプでも移動できます。
