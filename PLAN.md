# Plan: BigQuery + Hacker News (Learn SQL + Python)

Goal: practice raw SQL and basic Python data analysis by finding recurring pain points on Hacker News.

## Status
- Current step: Step 1 (Explore the dataset)
- Next action: Identify tables and key fields

## Scope (keep it small)
- Dataset: `bigquery-public-data.hacker_news` (posts + comments)
- Time window: last 6–12 months
- Output: 2–3 pain themes with evidence (counts, example titles/comments)

## Questions to Answer
- What “problem” or “struggle” topics appear most often in HN posts/comments?
- Which topics have the highest engagement (comments, points)?
- Are any topics trending up over time?

## Step 1: Explore the dataset (SQL only)
- [ ] Identify tables and key fields: `id`, `title`, `text`, `by`, `time`, `type`, `score`, `parent`
- [ ] Confirm how to filter to “Ask HN” or “Show HN” (likely via `title`)
- [ ] Count posts per month to confirm data volume

## Step 2: Extract candidate pain posts (SQL only)
- [ ] Filter to titles/text containing phrases like “struggling”, “problem”, “pain”, “help”, “how do you”
- [ ] Focus on `type = "story"` for posts; optionally add comment sampling later
- [ ] Aggregate by month and keyword to see frequency

## Step 3: Sample for manual labeling (Python)
- [ ] Pull 50–100 candidate rows into Python
- [ ] Manually label 5–10 themes (small list)
- [ ] Track: post id, title, keyword matched, label

## Step 4: Re-run SQL with labels (SQL + Python)
- [ ] Use your labels to group posts by theme
- [ ] Summarize counts + engagement (avg comments/score per theme)

## Step 5: Interpret results (write-up)
- [ ] Pick 2–3 themes with strongest evidence
- [ ] For each theme: example post, frequency, engagement signal

## Minimal Deliverables
- [ ] 1 SQL file or notebook with 3–5 queries
- [ ] 1 Python script/notebook that:
  - Loads query results
  - Applies labels
  - Produces a small summary table
- [ ] Short write-up in `PLAN.md` or a new `NOTES.md`

## Guardrails (to keep learning focused)
- [ ] No full automation or heavy NLP
- [ ] Manual labeling is ok and encouraged
- [ ] Keep each step small; iterate only after you can explain each query
