# シンプルチャットボットUI

Next.jsベースのシンプルなチャットボットUIで、Dify APIと連携してAI機能を提供します。

## 特徴

- **レスポンシブデザイン**: すべてのデバイスで最適に表示
- **リアルタイム対話**: AIとの自然な対話体験
- **Dify API連携**: 高度なAI機能の活用
- **簡単カスタマイズ**: 用途に応じてカスタマイズ可能
- **TypeScript対応**: 型安全な開発

## 技術スタック

- **フレームワーク**: Next.js 15
- **言語**: TypeScript
- **スタイリング**: Tailwind CSS
- **AI API**: Dify
- **開発ツール**: ESLint

## セットアップ

### 1. 依存関係のインストール

```bash
npm install
```

### 2. 環境変数の設定

`.env.local.example`を`.env.local`にコピーして、Dify APIの設定を行います：

```bash
cp .env.local.example .env.local
```

`.env.local`ファイルを編集：

```env
# Dify API設定
NEXT_PUBLIC_DIFY_API_URL=https://api.dify.ai/v1
NEXT_PUBLIC_DIFY_API_KEY=your-dify-api-key-here
```

### 3. 開発サーバーの起動

```bash
npm run dev
```

ブラウザで [http://localhost:3000](http://localhost:3000) を開いてアプリケーションを確認できます。

## Dify APIの設定方法

1. [Dify](https://dify.ai/)にアカウント登録またはログイン
2. 新しいアプリを作成または既存のアプリを選択
3. アプリの設定画面からAPIキーを取得
4. `.env.local`ファイルに以下を設定：
   - `NEXT_PUBLIC_DIFY_API_URL`: DifyのAPIエンドポイント
   - `NEXT_PUBLIC_DIFY_API_KEY`: 取得したAPIキー

## 使用方法

1. アプリケーションを起動
2. 右下のチャットボタンをクリック
3. チャットウィンドウが開いたら質問を入力
4. Enterキーまたは送信ボタンでメッセージを送信

## カスタマイズ

### チャットボットのスタイル変更

`src/components/Chatbot.tsx`ファイルでUIのカスタマイズが可能です：

- カラーテーマの変更
- レイアウトの調整
- アニメーション効果の追加

### API連携のカスタマイズ

`src/services/difyService.ts`ファイルでAPI連携の詳細設定が可能です：

- リクエスト形式の変更
- レスポンス処理のカスタマイズ
- エラーハンドリングの改善

## プロジェクト構造

```
src/
├── app/
│   ├── globals.css          # グローバルスタイル
│   ├── layout.tsx           # レイアウトコンポーネント
│   └── page.tsx            # メインページ
├── components/
│   └── Chatbot.tsx         # チャットボットコンポーネント
└── services/
    └── difyService.ts      # Dify API連携サービス
```

## 本番環境デプロイ

### Vercelでのデプロイ

1. [Vercel](https://vercel.com)にアカウント作成
2. プロジェクトをインポート
3. 環境変数を設定
4. デプロイ実行

## トラブルシューティング

### よくある問題

1. **チャットボットが応答しない**
   - `.env.local`ファイルの設定を確認
   - DifyのAPIキーが正しいか確認
   - ネットワーク接続を確認

2. **開発サーバーが起動しない**
   - Node.jsのバージョンを確認（Node.js 18以上推奨）
   - `npm install`を再実行
   - ポート3000が使用されていないか確認

3. **スタイルが正しく表示されない**
   - ブラウザのキャッシュをクリア
   - Tailwind CSSの設定を確認

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
# simple-chatbot-ui
