# Verification / 検証記録

Checked / 確認日: 2026-10-13 UTC.

- Official evidence: Pearson program and four linked exam pages directly retrieved. English PDF guides v1.0, effective July 2026, read for identity, audience, exam facts, domains, and prerequisites. Four Japanese guides and two policy PDFs retrieved for internal inspection. No official PDF or sample question is redistributed.
- External links: 25/25 source URLs returned HTTP 200 after redirects, with curl exit code 0. Results are in `link-check.json`. HTTP availability does not prove authenticated access, personal eligibility, reservation availability, or permanent correctness.
- Local docs: `python scripts/check_docs.py` checks links, UTF-8 replacement characters, bilingual file/ID presence, all 27 domain weights, curriculum mappings, and 30 bilingual answer keys. No network or dependency install is needed.
- Offline exercise: `python exercises/offline_lab.py` matched 4/4 synthetic fixture expectations; missing and reversed dates were rejected. Mock publication was blocked without approval, and already-recorded operations were reconciled rather than repeated. The injected note remained data. This is a teaching demonstration, not an LLM benchmark or complete security validator.
- Privacy/content: only fictional examples; no candidate profile, payment data, credentials, real-person information, exam dumps, recalled items, or copied official samples. Requested Git author/committer metadata is separate from learning content.
- Git whitespace check: `git diff --cached --check` before commit.
- Internal read-only review found no blocking factual, link, or safety issue. Its recommendation to distinguish protocol stopping (`tool_use` / `end_turn`) from iteration caps was incorporated in both concept guides. Exam scenario-format detail was also added. Review covered bilingual consistency and the saved official evidence.

公式試験の名称・項目数・料金・受験条件・配点を一次資料で確認。25リンクの到達性と教材のローカル参照・日英ID・配点・解答整合を検査。オフライン4例の期待結果が一致し、承認なし公開を模擬制御で拒否。実API・課金・受験申込は実行していません。

Remaining decisions / 残る判断:

1. Confirm the candidate's organization and recognized partner email domain without publishing personal information / 本人のパートナー所属・認識済み企業ドメインを非公開で確認。
2. Select the target exam based on role / 役割に応じて対象試験を選択。
3. Resolve actual exam language at booking: individual pages say English; FAQ says English/Japanese / 英語表記と日英FAQの差異を予約時に確認。
4. Add authorized practical product experience for detailed tasks; this pack provides introductory domain coverage / 詳細タスクには許可済み実機経験を追加。

No registration, payment, paid API execution, or new authentication setup was performed / 受験申込・支払・有料API・新規認証設定なし。
