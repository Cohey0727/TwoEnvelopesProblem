# Two Envelopes Problem (2つの封筒問題)

数学の有名なパラドックス「2つの封筒問題」を、Manimを使ったアニメーション動画で解説するプロジェクトです。

## 概要

2つの封筒問題は、一見すると交換が常に有利に見えてしまう興味深い確率論のパラドックスです。このプロジェクトでは、以下の内容を視覚的に解説します：

- **問題の設定**: 2つの封筒があり、一方の封筒には他方の2倍の金額が入っている
- **パラドックスの提示**: なぜ常に交換した方が得に見えるのか
- **数学的分析**: 期待値計算の矛盾点の解明

## プロジェクト構造

```
TwoEnvelopesProblem/
├── main.py                    # メインエントリポイント
├── src/                       # Manimアニメーションソースコード
│   ├── 01_introduction/       # 導入部のアニメーション
│   │   └── introduction.py    # 問題設定の説明
│   ├── 02_paradox_explanation/ # パラドックス説明部（準備中）
│   ├── 03_paradox_analysis/   # パラドックス分析部（準備中）
│   └── title.py               # タイトル画面
├── media/                     # 生成される動画・画像ファイル
├── SENARIO.md                 # シナリオ詳細説明
├── Makefile                   # ビルドコマンド集
├── pyproject.toml             # Python依存関係設定
└── package.json               # Node.js依存関係設定
```

## 必要環境

### Python環境

- Python >= 3.13
- Manim >= 0.19.0
- matplotlib >= 3.10.5
- numpy >= 2.3.2

### Node.js環境（開発用）

- pnpm@10.15.0
- prettier@3.6.2

## セットアップ

1. Python依存関係のインストール:

```bash
uv sync
```

3. Node.js依存関係のインストール（開発用）:

```bash
pnpm install
```

## 使用方法

### アニメーション動画の生成

導入部のアニメーションをレンダリング:

```bash
make render-intro
```

全体のアニメーションをレンダリング:

```bash
make render
```

生成されたファイルのクリーンアップ:

```bash
make clean
```

利用可能なコマンド一覧:

```bash
make help
```

### 動画ファイルの確認

生成された動画ファイルは `media/videos/` 配下に保存されます。

- `media/videos/introduction/480p15/TwoEnvelopesIntro.mp4` - 導入部アニメーション

## 技術的詳細

### フォント設定

日本語テキストの表示には「Hiragino Sans」フォントを使用しています（macOS環境）。
他のOS環境では適切な日本語フォントに変更してください。

### アニメーション設定

- 解像度: 480p
- フレームレート: 15fps
- 低品質モード（`-ql`）でプレビュー生成

## ファイル説明

### `SENARIO.md`

動画で説明する内容の詳細なシナリオが記載されています。パラドックスの説明から分析まで、段階的な構成が含まれています。

### `src/01_introduction/introduction.py`

問題設定を説明する導入部のアニメーション。以下の要素を含みます：

- タイトル表示
- 2つの封筒の視覚化
- 基本ルールの説明
- 不確実性の表現

## 開発状況

- ✅ 導入部（01_introduction）- 完成
- 🔄 パラドックス説明部（02_paradox_explanation）- 開発中
- 🔄 パラドックス分析部（03_paradox_analysis）- 開発中

## ライセンス

ISC License

## 貢献

プロジェクトへの貢献を歓迎します。プルリクエストやイシューの報告をお待ちしております。
