# fatihbozdag.com — project notes

Personal academic website of Fatih Ünal Bozdağ (Dr. Öğr. Üyesi, English Translation and Interpretation, Osmaniye Korkut Ata University). Built with Quarto, hosted on GitHub Pages, custom domain fatihbozdag.com.

## Conventions

- Language of the site: English primary, Turkish page at `tr/index.qmd`. Keep both in sync when biography changes.
- Commit messages: plain, imperative, no co-author or tool attribution lines. Never add `Co-Authored-By`, `Claude-Session` or "Generated with" trailers.
- Do not run `quarto render` output into git: `_site/` and `.quarto/` are ignored; GitHub Actions renders.
- Publications are hand-formatted APA in `publications.qmd` (one `::: {.pub}` block each) **and** mirrored in `pubs/bozdag.bib`. Update both.
- Only upload PDFs the publisher allows (open-access journals, CC-licensed articles). Lingua: only the accepted manuscript is posted (`files/papers/bozdag-mo-2026-lingua-cross-linguistic-influence-aam.pdf`, built 30 Oct 2026 from `ConstructionVerbs/second round/Revised manuscript R2 with figures and copyedits.docx` with R2 colouring removed and the CC BY-NC-ND notice added); never the publisher PDF. Currently excluded on purpose: book chapters from IGI Global, Cambridge Scholars, Harrassowitz, Çizgi, Eğiten, IJOPEC, LIF. Author post-prints may be added later if rights allow.
- PDF file names: `files/papers/<authors>-<year>-<venue>-<short-title>.pdf`.
- Images: `images/`. Profile photo should replace `images/profile.svg` (placeholder) — then change the reference in `index.qmd`.
- Link-preview image `images/og-image.png` (1200×630) is drawn by `scripts/make_og_image.py`; regenerate it when the position or research areas change (fonts: Source Serif 4 and Source Sans 3 variable TTFs from github.com/google/fonts, passed by path, not stored here). `404.qmd` is the custom not-found page; GitHub Pages serves it for any missing address.
- `stats/index.html` is the statistics companion (standalone HTML, copied as a resource, not rendered by Quarto). It was imported on 30 Oct 2026 from the claude.ai artifact https://claude.ai/artifact/XpyrwrmwD2c3rq26Ym9rfB with only the document head adjusted (title and meta moved into <head>, site icon and preview tags added, byline linked to the home page). The site copy is canonical. Its research passages were checked against the paper texts on 30 Oct 2026; re-check any new figure, cite no manuscript under review, and re-check the Language and Cognition figures against the proofs.

## Stack

- Quarto website (`_quarto.yml`), theme `cosmo` + `styles.scss` (Source Sans 3 / Source Serif 4 from Google Fonts). Dark mode: `styles-dark.scss` overrides the colour variables, which `styles.scss` declares as `!default`; keep new colours as variables in both files. Only the `.qmd` pages are rendered (`project.render`).
- Pages: `index.qmd` (About), `publications.qmd`, `tools.qmd`, `teaching.qmd`, `tr/index.qmd`.
- Deployment: `.github/workflows/publish.yml` — on push to `main`: `quarto-dev/quarto-actions/setup` (Quarto 1.7.32) → `quarto render` → `actions/upload-pages-artifact` → `actions/deploy-pages`.
- `CNAME` = `fatihbozdag.com`; `robots.txt` and `files/**`, `pubs/**` are copied as resources.
- Local preview: install Quarto (https://quarto.org/docs/get-started/), then `quarto preview` in this folder.

## Infrastructure state (as of 2026-10-29)

- Domain: fatihbozdag.com, registered 28 Oct 2026 via GoDaddy, 3 years, expires 28 Oct 2029, auto-renew on. Registrar account details are in `CLAUDE.local.md` (not committed). Consider transferring to Cloudflare Registrar after the 60-day lock for cheaper renewals.
- DNS (GoDaddy, ns37/ns38.domaincontrol.com):
  - A @ → 185.199.108.153 / 109.153 / 110.153 / 111.153
  - CNAME www → fatihbozdag.github.io
  - leave NS, SOA, `_dmarc` TXT as they are
- GitHub repo: https://github.com/fatihbozdag/fatihbozdag.github.io (branch `main`). Deleted and recreated on 30 Oct 2026 to purge an early commit that held registrar details; the clean history was pushed to the new repository. Local backups are in `_ARCHIVE/` (git-excluded, never publish).
- GitHub Pages: Source = "GitHub Actions" (switched 29 Oct 2026). Before the switch the Jekyll-rendered README was served instead of the Quarto build. The Quarto build (generator quarto-1.7.32) has been live since 29 Oct.
- HTTPS: Let's Encrypt certificate issued 29 Oct 2026 (valid to 27 Jan 2027, renewed automatically by GitHub). HTTPS is enforced: http:// returns 301 to https://. After the recreation HTTPS was re-enforced on 30 Oct; the setting took effect only after the next deploy (Actions, Run workflow).
- Health check: `curl -I https://fatihbozdag.com/publications.html` returns 200 and `https://www.fatihbozdag.com` returns 301 to the apex (both verified 29 Oct 2026).

## Open to-dos

1. Replace placeholder profile image with a real photo (`images/profile.jpg`, ~400×400, <200 KB).
2. *Language and Cognition* article (DOI 10.1017/langcog.2026.10131) is listed as "in press" since 29 Oct 2026. When it appears online, replace "in press" with 2026, add the volume (18) and e-number in `publications.qmd`, `index.qmd` and `pubs/bozdag.bib`.
3. Add the Lotus Congress 2026 abstract-book details when published.
4. Add the website URL to ORCID, Google Scholar and YÖK Akademik (needs the author's logins). GitHub profile `blog` field set 30 Oct 2026.
5. Optional: author post-prints for book chapters, if each publisher allows (Lingua accepted manuscript posted 30 Oct 2026).
6. Optional: a short "News" or "Talks" list; no blog unless it will be maintained.

## People / identifiers

- ORCID 0000-0002-9959-4704 · Google Scholar user W_xdrwwAAAAJ · GitHub fatihbozdag · e-mail fatihbozdag@osmaniye.edu.tr
- Related repos listed on the Tools page: bitig, linguistic_clusters, metadiscourse_analysis, passive_detection, annotator, Grammar-Research-with-Spacy, lexical_complexity.
- OSF profile https://osf.io/vz746/ (public projects: kq7gv = CLLT 2026 Linguistic Clusters, bg39s = Lingua 2026 CLI, zt9md = Language and Cognition passive verb preferences). A second, empty account (8guxd) exists. Never link `view_only` URLs on the site.
