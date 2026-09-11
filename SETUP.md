# Setup Guide — Terminal Dashboard Profile

## File Structure

```
<USERNAME>/
├── README.md
├── assets/
│   ├── liquid-morph-wordmark.svg   # Self-hosted morphing identity
│   └── terminal-card.svg           # Terminal intro card
└── .github/
    └── workflows/
        ├── metrics.yml             # lowlighter/metrics — stats, languages, activity
        └── pacman.yml              # Pac-Man contribution graph
```

Generated files (committed automatically by Actions):
- `metrics.stats.svg`       — GitHub Stats Dashboard
- `metrics.languages.svg`   — Top Languages
- `metrics.activity.svg`    — Activity Pulse
- `metrics.recent.svg`      — Recent Activity
- `output/pacman-contribution-graph.svg` — Pac-Man graph (on `output` branch)

---

## Step 1 — Replace Placeholders

### README.md
Search and replace every occurrence of:

| Placeholder | Replace With | Example |
|-------------|--------------|---------|
| `<USERNAME>` | Your GitHub username | `zaki` |
| `<NAME>` | Your display name | `Zaki` |
| `<TAGLINE>` | One-line descriptor | `Full-Stack Engineer` |
| `<LOCATION>` | Your location | `Berlin, DE` |
| `<EDUCATION>` | Your education | `B.S. Computer Science` |
| `<FOCUS>` | Current focus area | `React & Distributed Systems` |
| `<PORTFOLIO_URL>` | Your portfolio URL | `https://zaki.dev` |
| `<EMAIL>` | Your email | `hello@zaki.dev` |
| `<CURRENT_ROLE>` | Your role / stage | `Senior Eng @ Acme` |
| `<CURRENT_PROJECT>` | What you are building | `Real-time analytics platform` |
| `<CURRENT_LEARNING>` | What you are learning | `Rust, WebAssembly` |
| `<CURRENT_EXPERIMENT>` | What you are experimenting with | `Local LLM inference` |
| `<CURRENT_SHIPPING>` | What you are shipping | `v2.0 API rewrite` |
| `<LINKEDIN_HANDLE>` | LinkedIn username | `zaki` |
| `<TWITTER_HANDLE>` | Twitter/X username | `zaki` |

### assets/liquid-morph-wordmark.svg
Open the SVG and replace:
- `NAME` (the 4-letter wordmark text) with your name or initials.
- Adjust `font-size` if your name is not 4 characters.
- Replace `<USERNAME>` in the bottom-right detail text.

### assets/terminal-card.svg
Open the SVG and replace all `<PLACEHOLDER>` values with your actual info.
Also update the skill pills to match your actual technology stack.

---

## Step 2 — Configure GitHub Secrets

Go to **Settings → Secrets and variables → Actions → New repository secret**.

### `METRICS_TOKEN` (Required for lowlighter/metrics)

1. Go to GitHub **Settings → Developer settings → Personal access tokens → Tokens (classic)**.
2. Click **Generate new token (classic)**.
3. **Token name:** `METRICS_TOKEN`
4. **Expiration:** Choose an expiration (e.g., 90 days) and set a calendar reminder.
5. **Scopes:** Select the **minimum** required for your data:

| Scope | Needed For | Recommendation |
|-------|-----------|----------------|
| *(no scopes)* | Public profile, public repos, public activity | **Start here** |
| `public_repo` | Public repository traffic, detailed lines | Add if basic stats fail |
| `repo` | Private repository contributions, traffic, lines | Only if you want private data included |
| `read:user` | User metadata, private profile fields | Add if user-level plugins fail |
| `read:org` | Organization membership metrics | Only if you belong to orgs you want tracked |

> **Security:** Use the least scopes possible. A scopeless token can still display private contributions if you enable *"Include private contributions on my profile"* in your GitHub profile settings.

6. Copy the token and paste it into the `METRICS_TOKEN` repository secret.

### `GITHUB_TOKEN` (Auto-provided, no setup needed)
The Pac-Man workflow uses `secrets.GITHUB_TOKEN` which GitHub injects automatically. No manual configuration required.

---

## Step 3 — Trigger Workflows Manually

### Metrics Workflow
1. Go to the **Actions** tab in your profile repo.
2. Click **Metrics** in the left sidebar.
3. Click **Run workflow** → **Run workflow**.
4. Wait ~2–3 minutes. The workflow will commit 4 SVG files to the `main` branch.

### Pac-Man Workflow
1. Go to the **Actions** tab.
2. Click **Generate Pac-Man** in the left sidebar.
3. Click **Run workflow** → **Run workflow**.
4. Wait ~1–2 minutes. The workflow will create an `output` branch and push the SVG there.

> **First run note:** The Pac-Man workflow creates the `output` branch automatically on its first run. If the README shows a broken image before this, that is expected.

---

## Step 4 — Verify Generated SVGs

After running both workflows:

1. **Metrics SVGs:** Check the root of your repo for:
   - `metrics.stats.svg`
   - `metrics.languages.svg`
   - `metrics.activity.svg`
   - `metrics.recent.svg`

   Open each file in GitHub's file viewer to confirm it renders as an SVG.

2. **Pac-Man SVG:** Check the `output` branch for:
   - `pacman-contribution-graph.svg`
   - `pacman-contribution-graph-dark.svg`

   Verify by visiting:
   ```
   https://raw.githubusercontent.com/<USERNAME>/<USERNAME>/output/pacman-contribution-graph.svg
   ```

3. **README preview:** Edit `README.md` and use the **Preview** tab to check layout.

---

## Troubleshooting

### Metrics workflow fails with "API rate limit"
- lowlighter/metrics makes many GitHub API calls.
- If you have many repos, the scopeless token rate limit (60/hr) may be exceeded.
- **Fix:** Use a token with `public_repo` scope (5,000 requests/hour).

### Metrics workflow fails with "Insufficient token scopes"
- Some plugins (traffic, lines) need repository access.
- **Fix:** Add `repo` or `public_repo` scope to `METRICS_TOKEN`.

### Pac-Man workflow fails with "Resource not accessible"
- The workflow needs `contents: write` permission.
- **Fix:** Ensure the workflow YAML has `permissions: contents: write` under the `generate` job.

### Pac-Man SVG not showing in README
- The `output` branch may not exist yet.
- **Fix:** Run the Pac-Man workflow manually once. It will create the branch.
- Also verify the raw URL in the README matches your exact username.

### SVGs look too wide on mobile
- GitHub scales wide SVGs down on narrow screens.
- **Fix:** This is expected behavior. The `width="100%"` attribute ensures they fill the container. Avoid making SVGs wider than ~800px if readability is a concern.

### Liquid morph wordmark text overflows
- The wordmark is designed for ~4 characters.
- **Fix:** Adjust `font-size` in `assets/liquid-morph-wordmark.svg` to fit your name.

### Terminal card info is outdated
- The terminal card is a static SVG.
- **Fix:** Edit `assets/terminal-card.svg` directly when your info changes.

---

## Daily Automation

Both workflows are scheduled to run daily:
- **Metrics:** Every day at 04:00 UTC (`0 4 * * *`)
- **Pac-Man:** Every day at 07:47 UTC (`47 7 * * *`)

You can change these cron expressions in the workflow files. Use [crontab.guru](https://crontab.guru/) to validate your cron.

---

## Token Permissions Summary

| Workflow | Secret | Minimum Scopes | Why |
|----------|--------|----------------|-----|
| `metrics.yml` | `METRICS_TOKEN` | *(none)* | Public GitHub data |
| `metrics.yml` | `METRICS_TOKEN` | `public_repo` | Traffic + lines plugins |
| `metrics.yml` | `METRICS_TOKEN` | `repo` | Private repo data |
| `pacman.yml` | `GITHUB_TOKEN` | *(auto)* | Pushes to `output` branch |
