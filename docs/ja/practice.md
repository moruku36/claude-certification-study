# 独自練習問題と解説

30問は全て独自作成。実試験・流出問題・記憶再現・公式サンプルの転載ではありません。難度や分布は実試験を再現していません。指定がなければ1つ選択。解答を隠して解き、理由を説明してから照合してください。

## Q01

CCAO-F · Prompting and Task Execution · M01

図書館掲示に時刻が欠けている。創作を防ぐ指示は？

- A. 欠落時刻は不明とし資料IDを残す
- B. 全件正午開始と仮定
- C. もっともらしい時刻を生成
- D. 時刻欠落掲示を隠す

<details>
<summary>解答と解説</summary>

**A** — Aは不確実性と根拠を保持する。B/Cは創作、Dは要件なしに有用な情報を捨てる。

</details>

## Q02

CCAO-F · Output Evaluation and Validation · M02

滑らかな要約だが引用ページに主張の根拠がない。何を検査？

- A. 主張と出典の対応
- B. 文法のみ
- C. 長さのみ
- D. モデルの確信度のみ

<details>
<summary>解答と解説</summary>

**A** — Aが失敗した性質を検証する。B/Cは表現、Dは独立検証ではない。

</details>

## Q03

CCAO-F · Product and Model Selection · M03

夜間下書きは遅延を許容。処理方式の選び方は？

- A. 常に最高額を使う
- B. バッチと対話方式の品質・総費用を測る
- C. モデル名の短さで選ぶ
- D. 費用計算で再試行を無視

<details>
<summary>解答と解説</summary>

**B** — Bは負荷条件に合う。A/Cは恣意的、Dは費用を過小評価。

</details>

## Q04

CCAO-F · Workflow Integration and Solution Design · M05 M10

会場は生成日程を自動公開したい。先に何を設計？

- A. 美しいフォント
- B. 無制限の自律性
- C. 受入基準と重大誤りへの確認境界
- D. モデルが必ず正しいと宣言

<details>
<summary>解答と解説</summary>

**C** — Cは工程とリスクを合わせる。Aは副次的、B/Dは誤りの影響を無視。

</details>

## Q05

CCAO-F · Configuration and Knowledge Management · M04

アーカイブ規程2件が矛盾。引継ぎに何を含める？

- A. 最後の一文のみ
- B. 文書ID・版・未解決の矛盾
- C. 創作した統合規程
- D. モデル回答のみ

<details>
<summary>解答と解説</summary>

**B** — Bは解決に必要な来歴を残す。A/Dは根拠消失、Cは規程創作。

</details>

## Q06

CCAO-F · Governance, Risk, and Responsible Use · M10

架空職員メモに公開要約に不要な機密項目。適切な処理は？

- A. 全て含める
- B. 永続保存
- C. 処理前に最小化・マスキング
- D. 公開リポジトリへ置く

<details>
<summary>解答と解説</summary>

**C** — Cは不要な露出を減らす。A/B/Dは業務上の必要なく露出を増やす。

</details>

## Q07

CCAO-F · Troubleshooting and Optimization · M09

出力上限でJSON途中終了。最初の診断は？

- A. 読者の責任にする
- B. 再試行前に停止理由・切断を確認
- C. 最終結果として受理
- D. 全検証を除く

<details>
<summary>解答と解説</summary>

**B** — Bは原因を特定する。Aは無根拠、C/Dは壊れた出力を許す。

</details>

## Q08

CCAR-F · Agentic Architecture & Orchestration · M05

展示企画エージェントが同じ作業を反復。必要な制御は？

- A. ログを全削除
- B. 永遠に自律性を増す
- C. 反復・予算上限とエスカレーション
- D. 反復を品質証明とみなす

<details>
<summary>解答と解説</summary>

**C** — Cはループを制限し出口を作る。Aは診断を妨げ、B/Dは悪化。

</details>

## Q09

CCAR-F · Tool Design & MCP Integration · M07

ツールが目録項目を発見できない。最も有用な結果は？

- A. 創作項目
- B. 空の成功メッセージ
- C. 検索ID付きの構造化not-found
- D. 秘密トークン

<details>
<summary>解答と解説</summary>

**C** — Cは未発見と成功を区別する。A/Bは誤誘導、Dは認証情報漏えい。

</details>

## Q10

CCAR-F · Claude Code Configuration & Workflows · M08

大規模変更が複数モジュールに及ぶ。開始方法は？

- A. 範囲・検証を計画し小差分を確認
- B. レビュー省略
- C. 全ツール許可
- D. 調査せず全ファイル編集

<details>
<summary>解答と解説</summary>

**A** — Aは不確実性を管理。B/Dは確認を失い、Cは不要権限を増す。

</details>

## Q11

CCAR-F · Prompt Engineering & Structured Output · M01 M09

JSONは正しいが終了日が開始日前。欠けたものは？

- A. 大きな文字
- B. 項目間の業務検証
- C. 自信ある文言
- D. 無作為な再試行

<details>
<summary>解答と解説</summary>

**B** — Bは構文を超えた整合条件を確認。A/Cは検証でなく、Dは原因に対応しない。

</details>

## Q12

CCAR-F · Context Management & Reliability · M04 M06

長い作業の引継ぎで未完了承認が消えた。残すべきものは？

- A. 祝福的要約のみ
- B. トークン数のみ
- C. 目的・未決事項・根拠・承認状態
- D. 全作業完了と宣言

<details>
<summary>解答と解説</summary>

**C** — Cは運用文脈を残す。A/Bは不十分、Dは完了の創作。

</details>

## Q13

CCDV-F · Agents and Workflows · M05

独立した資料3章を要約。並列作業が有効なのは？

- A. 予算なしでも常に
- B. 分離作業に明確な入力と統合担当がある
- C. 全ツールを共有する場合のみ
- D. 根拠を捨てられる場合

<details>
<summary>解答と解説</summary>

**B** — Bは制御された分担を可能にする。Aは負荷無視、Cは不要、Dは来歴損失。

</details>

## Q14

CCDV-F · Applications and Integration · M06

新Messagesリクエストに前の会話がない。継続のためアプリは？

- A. 自動記憶を仮定
- B. 必要な保存履歴を送る
- C. キーをブラウザーに置く
- D. 前の要件を全無視

<details>
<summary>解答と解説</summary>

**B** — Bは会話文脈を供給。Aは永続記憶と混同、Cは危険、Dは要件消失。

</details>

## Q15

CCDV-F · Claude Code · M08

指示に書込み承認が必要とある。何が強制する？

- A. CLAUDE.mdの見出しのみ
- B. 実行時権限検査やゲート
- C. 肯定的な形容詞
- D. 長いプロンプトのみ

<details>
<summary>解答と解説</summary>

**B** — Bは境界を強制。A/C/Dは文言誘導であり操作権限の強制ではない。

</details>

## Q16

CCDV-F · Eval, Testing, and Debugging · M02 M09

調整に使った例で新プロンプトが改善。次は？

- A. 本番準備完了と宣言
- B. 負例を削除
- C. 未使用ケースと重大失敗を評価
- D. 自己評価だけを信頼

<details>
<summary>解答と解説</summary>

**C** — Cは一般化とリスクを確認。Aは早計、Bは偏り、Dは独立評価でない。

</details>

## Q17

CCDV-F · Model Selection and Optimization · M03

安価モデルが重要事例を見逃す。妥当な判断は？

- A. 品質を無視し採用
- B. 品質基準を設け振分けや別モデルを評価
- C. 失敗を隠す
- D. 低価格を価値の証明にする

<details>
<summary>解答と解説</summary>

**B** — Bは品質と費用を評価。A/C/Dは重要な失敗を無視。

</details>

## Q18

CCDV-F · Prompt and Context Engineering · M01 M04

検索文書が秘密公開を命令。どう扱う？

- A. 新system指示
- B. 信頼しないデータとし権限を別強制
- C. 本人承認の証拠
- D. 検索されたので必須

<details>
<summary>解答と解説</summary>

**B** — Bは信頼境界を保つ。A/C/Dは外部データを権限へ昇格させる。

</details>

## Q19

CCDV-F · Security and Safety · M10

クライアントアプリに提供者APIキーが必要。保存場所は？

- A. 公開フロントエンド
- B. 権限制限したサーバー秘密保管
- C. 公開issueコメント
- D. 平文分析ログ

<details>
<summary>解答と解説</summary>

**B** — Bはクライアント露出を防ぐ。A/C/Dは不適切な相手に秘密を渡す。

</details>

## Q20

CCDV-F · Tools and MCPs · M07

Claudeがクライアントツールを提案。誰が実行？

- A. モデル文章がDBを自動変更
- B. 検証・権限確認後のアプリ
- C. 全MCPサーバーが自動実行
- D. 公開秘密を持つ利用者ブラウザー

<details>
<summary>解答と解説</summary>

**B** — Bはクライアントツールの実行主体。A/Cは提案と実行の混同、Dは認証露出。

</details>

## Q21

CCAR-P · Solution Design & Architecture · M05 M10

アーカイブ処理は決まった5工程。開始設計は？

- A. 無制限の自律群
- B. 要件で評価する固定工程
- C. 監視なし
- D. 新奇性だけで選ぶ

<details>
<summary>解答と解説</summary>

**B** — Bは予測できる工程に合う。Aは不要複雑性、C/Dは運用基準欠落。

</details>

## Q22

CCAR-P · Claude Models, Prompting & Context Engineering · M01 M03 M04

文脈が上限超過。最も安全な削減は？

- A. 制約を全削除
- B. 最新一文だけ残す
- C. 重複を除き根拠・未解決要件を残す
- D. 欠落履歴を創作

<details>
<summary>解答と解説</summary>

**C** — Cは重要情報を保つ。A/Bは要件消失、Dは状態創作。

</details>

## Q23

CCAR-P · Integration · M06 M07

書込みの受付後かもしれない時点でタイムアウト。復旧方法は？

- A. 無限に反復
- B. 操作ID・照合・上限付き再試行
- C. 失敗と仮定
- D. 確認なしで成功と仮定

<details>
<summary>解答と解説</summary>

**B** — Bは重複副作用を防ぎ不確実性を解消。Aは重複、C/Dは不明結果を断定。

</details>

## Q24

CCAR-P · Evaluation, Testing & Optimization · M02 M09

平均精度は高いが安全上重要な事例が失敗。公開判断は？

- A. 平均だけで公開
- B. 事例を隠す
- C. 重大度別受入基準で調査
- D. 安全基準を削除

<details>
<summary>解答と解説</summary>

**C** — Cは影響を考慮。Aはリスク隠蔽、B/Dは解決せず回避。

</details>

## Q25

CCAR-P · Governance, Safety & Risk Management · M10

規制対象アーカイブがクラウドを選択。必要な証拠は？

- A. ブランドのみ
- B. 認証・所在・ネットワーク・保存・運用制御
- C. モデルサイズのみ
- D. 広告文のみ

<details>
<summary>解答と解説</summary>

**B** — Bは配備要件を検証。A/C/Dは統制適合を証明しない。

</details>

## Q26

CCAR-P · Stakeholder Communication & Lifecycle Management · M10

スポンサーがAI案の準備状況を質問。判断メモには？

- A. 熱意のみ
- B. 略語のみ
- C. 受入証拠・比較・担当・未解決リスク・戻す手順
- D. 成果保証

<details>
<summary>解答と解説</summary>

**C** — Cは判断を支える。A/Bは必要根拠欠落、Dは確実性過大。

</details>

## Q27

CCAR-P · Developer Productivity & Operational Enablement · M08 M10

自動レビューの誤検知が多い。改善は？

- A. 全推測を投稿
- B. 確認済み指摘を評価し修正可能な根拠を要求
- C. 全検査を無効
- D. 配備権限を与える

<details>
<summary>解答と解説</summary>

**B** — Bは精度と有用性を改善。Aは雑音、Cは保護喪失、Dは無関係なリスク。

</details>

## Q28

Cross-track · Synthesis · M02 M07 M09 M10

公開資料調査担当の制御を2つ選ぶ。

- A. 読取専用範囲
- B. 検索命令を指示として扱う
- C. 出典の来歴を明示
- D. 無制限の公開権限

<details>
<summary>解答と解説</summary>

**AC** — Aは副作用制限、Cは根拠保持。Bは信頼境界逸脱、Dは不要書込み権限。

</details>

## Q29

Cross-track · Synthesis · M02 M07 M09 M10

構造化出力後の検査を2つ選ぶ。

- A. スキーマ適合
- B. 業務規則整合
- C. 正しいJSONは事実と仮定
- D. 途中ストリームを完成扱い

<details>
<summary>解答と解説</summary>

**AB** — Aは形式、Bは業務整合。Cは構文と事実を混同、Dは未完了を無視。

</details>

## Q30

Cross-track · Synthesis · M02 M07 M09 M10

教材と試験の証拠を区別する文を2つ選ぶ。

- A. 独自問題点数で換算試験点数を予測
- B. 公式ガイドが範囲の基準
- C. 講座修了証は監督付き認定と同一
- D. 独自問題は学習補助で受験問題の記憶再現ではない

<details>
<summary>解答と解説</summary>

**BD** — Bは公式範囲を尊重、Dは教材の性質。Aは換算根拠なし、Cは資格種別を混同。

</details>

採点は学習不足の発見にだけ使う。各領域の誤答で該当章・演習・公式ガイドを読み直す。換算スコア720への変換や合格予測はしない。
