# Xusheng Zhu Academic Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a production-ready English academic website for Dr. Xusheng Zhu on GitHub Pages using Jekyll, with eight primary pages, CV-derived content, a supplied portrait, downloadable CV, news posts, responsive styling, and deployment documentation.

**Architecture:** The site is a static Jekyll project. Structured CV data lives in `_data/*.yml`, reusable page chrome lives in `_layouts` and `_includes`, long-form page copy lives in Markdown, and news items live in `_posts`. Core content requires no JavaScript; the site is rendered at build time and deployed directly through GitHub Pages.

**Tech Stack:** Jekyll 4.x, Ruby/Bundler, Liquid templates, YAML data files, Markdown, semantic HTML5, CSS3, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-09-18-academic-homepage-design.md`

## Global Constraints

- Use GitHub Pages with Jekyll; no server-side backend.
- Provide primary navigation for Home, Research, Publications, Grants, Service, News, CV, and Contact.
- Use a clean UCL/IEEE-inspired visual direction: white background, dark navy/blue accents, restrained secondary accent, no decorative animation.
- Maintain content primarily through Markdown/YAML rather than repeated hard-coded HTML.
- Use the supplied portrait at `assets/img/profile.jpg` and the latest English academic CV at `assets/cv/Xusheng_Zhu_CV.pdf`.
- Do not invent publication metrics, roles, dates, affiliations, awards, or grants.
- Publish no personal phone number.
- Core content must not depend on JavaScript.
- Navigation must be keyboard accessible and responsive.
- No `TBD`, `TODO`, lorem ipsum, or other visible placeholder content may ship.
- All eight pages must build successfully with Jekyll; internal links and CV download must resolve.

---

## File Structure

The implementation will create the following focused units:

```text
.
├── _config.yml                         # Site metadata, GitHub Pages settings, SEO defaults
├── Gemfile                             # Jekyll and GitHub Pages-compatible dependencies
├── _data/
│   ├── navigation.yml                  # Primary nav labels/URLs
│   ├── publications.yml                # Selected, first/corresponding, other journal, conference records
│   ├── grants.yml                      # MSCA, NSFC, SJTU fellowship/scholarship data
│   └── service.yml                     # Editorial, guest-editing, conference, TPC, reviewer records
├── _includes/
│   ├── head.html                       # Metadata, Open Graph, stylesheet
│   ├── header.html                     # Site masthead and navigation
│   ├── footer.html                     # Copyright/affiliation footer
│   ├── publication-list.html           # Reusable publication renderer
│   └── service-list.html               # Reusable service renderer
├── _layouts/
│   ├── default.html                    # Shared page shell
│   ├── home.html                       # Home-specific hero and section layout
│   └── post.html                       # News post layout
├── _posts/                             # Initial dated news entries
├── assets/
│   ├── css/main.css                    # Entire visual system and responsive behavior
│   ├── img/profile.jpg                 # Supplied portrait
│   └── cv/Xusheng_Zhu_CV.pdf           # Latest English academic CV
├── index.md                            # Home page data/copy
├── research.md                         # Four research themes and secondary topics
├── publications.md                     # Publication page structure
├── grants.md                           # Grants/fellowships page
├── service.md                          # Editorial and conference service page
├── news.md                             # News index
├── cv.md                               # CV page/download CTA
├── contact.md                          # UCL/contact links
├── 404.html                            # Branded not-found page
├── README.md                           # Local build + GitHub Pages deployment guide
└── tests/
    └── verify_site.sh                  # Deterministic static verification after Jekyll build
```

---

### Task 1: Create the Jekyll skeleton and build verification

**Files:**
- Create: `_config.yml`
- Create: `Gemfile`
- Create: `_data/navigation.yml`
- Create: `_layouts/default.html`
- Create: `_includes/head.html`
- Create: `_includes/header.html`
- Create: `_includes/footer.html`
- Create: `tests/verify_site.sh`

**Interfaces:**
- Consumes: nothing.
- Produces: a buildable Jekyll shell; `site.data.navigation`; the shared `default` layout; executable `tests/verify_site.sh` used by all later tasks.

- [ ] **Step 1: Write the failing verification script**

Create `tests/verify_site.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

bundle exec jekyll build --trace

test -f _site/index.html
for page in research publications grants service news cv contact; do
  test -f "_site/${page}/index.html"
done

grep -q 'Xusheng Zhu' _site/index.html
grep -q 'Home' _site/index.html
grep -q 'Research' _site/index.html
grep -q 'Publications' _site/index.html
```

Run:

```bash
chmod +x tests/verify_site.sh
./tests/verify_site.sh
```

Expected: FAIL because `Gemfile`, `_config.yml`, layouts, and pages do not yet exist.

- [ ] **Step 2: Create the Jekyll dependency/configuration files**

Create `Gemfile`:

```ruby
source "https://rubygems.org"

gem "jekyll", "~> 4.3"
gem "jekyll-seo-tag", "~> 2.8"
gem "jekyll-sitemap", "~> 1.4"
gem "webrick", "~> 1.8"
```

Create `_config.yml`:

```yaml
title: "Xusheng Zhu | 6G Wireless Communications"
name: "Xusheng Zhu"
description: "Academic website of Xusheng Zhu, MSCA Postdoctoral Fellow at University College London, working on 6G wireless communications, fluid antennas, intelligent surfaces, spatial modulation, and AI-assisted wireless systems."
url: ""
baseurl: ""
lang: "en-GB"
timezone: "Europe/London"
email: "xusheng.zhu@ucl.ac.uk"
author:
  name: "Xusheng Zhu"
  email: "xusheng.zhu@ucl.ac.uk"
  affiliation: "University College London"
plugins:
  - jekyll-seo-tag
  - jekyll-sitemap
exclude:
  - Gemfile
  - Gemfile.lock
  - README.md
  - tests
  - docs
markdown: kramdown
permalink: pretty
```

- [ ] **Step 3: Create navigation data**

Create `_data/navigation.yml`:

```yaml
- title: Home
  url: /
- title: Research
  url: /research/
- title: Publications
  url: /publications/
- title: Grants
  url: /grants/
- title: Service
  url: /service/
- title: News
  url: /news/
- title: CV
  url: /cv/
- title: Contact
  url: /contact/
```

- [ ] **Step 4: Create the shared document shell**

Create `_includes/head.html` with charset, viewport, title, stylesheet, Open Graph defaults, canonical URL, and `{% seo %}`. Create `_includes/header.html` to iterate over `site.data.navigation` and mark the current URL with `aria-current="page"`. Create `_includes/footer.html` with `© {{ site.time | date: '%Y' }} Xusheng Zhu · University College London`.

Create `_layouts/default.html`:

```html
<!doctype html>
<html lang="{{ site.lang | default: 'en' }}">
  <head>{% include head.html %}</head>
  <body>
    <a class="skip-link" href="#main-content">Skip to content</a>
    {% include header.html %}
    <main id="main-content" class="site-main">
      {{ content }}
    </main>
    {% include footer.html %}
  </body>
</html>
```

- [ ] **Step 5: Add temporary-but-final-content page stubs required by the build test**

Create `index.md`, `research.md`, `publications.md`, `grants.md`, `service.md`, `news.md`, `cv.md`, and `contact.md`, each with the `default` layout, a permanent permalink, an accurate page title, and one sentence of real content derived from the approved spec. Example for `research.md`:

```markdown
---
layout: default
title: Research
permalink: /research/
---

# Research

My research focuses on reconfigurable wireless technologies for 6G.
```

Do not use placeholders; later tasks replace these sentences with complete content.

- [ ] **Step 6: Install dependencies and run the verification**

Run:

```bash
bundle install
./tests/verify_site.sh
```

Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add _config.yml Gemfile _data/navigation.yml _layouts/default.html _includes tests index.md research.md publications.md grants.md service.md news.md cv.md contact.md
git commit -m "feat: scaffold Jekyll academic site"
```

---

### Task 2: Implement the visual system, portrait, and responsive navigation

**Files:**
- Create: `assets/css/main.css`
- Create: `_layouts/home.html`
- Copy: `/mnt/data/zxs.jpg` → `assets/img/profile.jpg`
- Modify: `_includes/head.html`
- Modify: `_includes/header.html`
- Modify: `index.md`
- Modify: `tests/verify_site.sh`

**Interfaces:**
- Consumes: navigation data and `default` layout from Task 1.
- Produces: reusable CSS classes, responsive header, home layout, portrait asset, and hero quick links.

- [ ] **Step 1: Extend the verification script with visual/asset assertions**

Append:

```bash
test -f _site/assets/css/main.css
test -f _site/assets/img/profile.jpg
grep -q 'Marie Skłodowska-Curie Actions Postdoctoral Fellow' _site/index.html
grep -q 'profile.jpg' _site/index.html
grep -q 'Google Scholar' _site/index.html
grep -q 'ORCID' _site/index.html
grep -q 'Download CV' _site/index.html
```

Run `./tests/verify_site.sh` and expect FAIL because those assets/content do not yet exist.

- [ ] **Step 2: Copy the portrait and wire the stylesheet**

Run:

```bash
mkdir -p assets/img assets/css
cp /mnt/data/zxs.jpg assets/img/profile.jpg
```

Update `_includes/head.html` to include:

```html
<link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">
```

- [ ] **Step 3: Create the complete visual system**

Implement `assets/css/main.css` with:

- CSS custom properties: `--navy: #17365d`, `--blue: #005a9c`, `--accent: #8f1537`, `--text: #20252b`, `--muted: #5f6873`, `--line: #dbe3ea`, `--surface: #f6f9fc`, `--white: #ffffff`.
- 1120px max-width `.container`.
- accessible `.skip-link`.
- sticky but unobtrusive `.site-header`.
- flex/wrap navigation that collapses naturally without JavaScript.
- responsive two-column `.hero` that becomes single-column under 760px.
- circular/soft-square portrait treatment without modifying the source image.
- button/link styles for Scholar, ORCID, email, CV.
- card grid, section headings, publication lists, timeline/news list, footer, and focus-visible states.
- print rules that hide navigation and preserve readable text.

- [ ] **Step 4: Create the home layout**

Create `_layouts/home.html` extending the same shell as `default`, with a hero section that reads front matter keys `role`, `affiliation`, `research_statement`, and `profile_image`, followed by `{{ content }}`.

The hero must render:

```text
Xusheng Zhu, Ph.D.
Marie Skłodowska-Curie Actions Postdoctoral Fellow
Department of Electronic & Electrical Engineering, University College London
I develop reconfigurable wireless technologies for 6G, with a focus on fluid and movable antennas, intelligent surfaces, spatial/index modulation, and AI-assisted wireless systems.
```

- [ ] **Step 5: Replace `index.md` with the approved home front matter and quick links**

Use:

```yaml
---
layout: home
title: Home
permalink: /
role: "Marie Skłodowska-Curie Actions Postdoctoral Fellow"
affiliation: "Department of Electronic & Electrical Engineering, University College London"
research_statement: "I develop reconfigurable wireless technologies for 6G, with a focus on fluid and movable antennas, intelligent surfaces, spatial/index modulation, and AI-assisted wireless systems."
profile_image: "/assets/img/profile.jpg"
---
```

Include links to:

- `https://scholar.google.com/citations?user=zwnN_NsAAAAJ&hl=en&oi=ao`
- `https://orcid.org/0000-0001-8463-0373`
- `mailto:xusheng.zhu@ucl.ac.uk`
- `/assets/cv/Xusheng_Zhu_CV.pdf`

- [ ] **Step 6: Run build verification**

Run `./tests/verify_site.sh`.
Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add assets _layouts/home.html _includes index.md tests/verify_site.sh
git commit -m "feat: add responsive academic homepage design"
```

---

### Task 3: Add structured research, grants, and service content

**Files:**
- Create: `_data/grants.yml`
- Create: `_data/service.yml`
- Create: `_includes/service-list.html`
- Modify: `research.md`
- Modify: `grants.md`
- Modify: `service.md`
- Modify: `index.md`
- Modify: `tests/verify_site.sh`

**Interfaces:**
- Consumes: page layouts and CSS from Tasks 1–2.
- Produces: structured grant/service records and the complete Research, Grants, and Service pages.

- [ ] **Step 1: Add failing content checks**

Append to `tests/verify_site.sh`:

```bash
grep -q 'Fluid and Movable Antenna Systems' _site/research/index.html
grep -q 'Reconfigurable Intelligent / Fluid Surfaces' _site/research/index.html
grep -q 'AI-Assisted Reconfigurable Wireless Systems' _site/research/index.html
grep -q 'Spatial Multiplexing Fluid Antenna Systems' _site/grants/index.html
grep -q 'IEEE Transactions on Communications' _site/service/index.html
grep -q 'IEEE Transactions on Aerospace and Electronic Systems' _site/service/index.html
grep -q 'AIPIP 2026' _site/service/index.html
grep -q 'Tutorial Presenter' _site/service/index.html
```

Run `./tests/verify_site.sh`; expected FAIL.

- [ ] **Step 2: Create `_data/grants.yml` with the three approved records**

Use exact records:

```yaml
- title: "Spatial Multiplexing Fluid Antenna Systems (SM-FAS)"
  scheme: "Horizon Europe Marie Skłodowska-Curie Actions Postdoctoral Fellowship"
  role: "Principal Investigator"
  period: "Apr. 2026 – Mar. 2028"
  amount: "EUR 276,000"
  project_id: "101269517"
- title: "Key Technologies of Second-Order Spatial Modulation Based on Multi-Antenna and Reconfigurable Intelligent Surfaces"
  scheme: "National Natural Science Foundation of China doctoral student basic research project"
  role: "Principal Investigator"
  period: "Jan. 2025 – Dec. 2026"
  amount: "CNY 300,000"
  project_id: "624B2094"
- title: "Outstanding Ph.D. Graduate Development Scholarship"
  scheme: "Shanghai Jiao Tong University"
  role: "Awardee / Principal Investigator"
  period: "Jun. 2025 – May 2026"
  amount: "CNY 300,000"
```

- [ ] **Step 3: Create `_data/service.yml`**

Add sections for `editorial`, `guest_editor`, `conference_leadership`, `tutorials`, `tpc`, and `reviewing`. Include these exact high-level roles:

- Editor, IEEE Transactions on Communications, Communication Theory & Systems II, 2026–present.
- Associate Editor, IEEE Wireless Communications Letters, 2026–present.
- Associate Editor, IEEE Communications Letters, Wireless Communications, 2026–present.
- Associate Editor, IEEE Open Journal of the Communications Society, Wireless Communications, 2026–present.
- Guest Editor, IEEE Transactions on Aerospace and Electronic Systems Special Section, “Next-Generation Reconfigurable Antenna Systems for Aerospace Communications and Sensing,” 2026–2027.
- Symposium Co-Chair, AIPIP 2026, “Intelligent Antennas, Reconfigurable Electromagnetic Technologies, and High-Frequency Links,” Hangzhou, China.
- Workshops General Co-Chair, IEEE GLOBECOM 2026, Macau, China.
- Workshops General Co-Chair & Track Chair, IEEE/CIC ICCC 2026, Wuhan, China.
- Workshops General Co-Chair, IEEE VTC 2026-Spring, Nice, France.
- Session Chair, IEEE/CIC ICCC 2026 FAS Workshop, Wuhan, China.
- Session Chair, IEEE ICC 2026 Workshops, WS-09: Fluid Antenna Systems for 6G, Glasgow, UK.
- Tutorial Presenter, IEEE/CIC ICCC 2026, Wuhan, China.

For TPC/reviewing, summarize rather than duplicate every line of the CV.

- [ ] **Step 4: Implement the reusable service renderer**

Create `_includes/service-list.html` accepting an `items` array and rendering an accessible `<ul class="service-list">` with bold role, organization, optional area/topic, location, and period.

- [ ] **Step 5: Replace `research.md` with four substantive themes**

Use four H2 sections:

1. Fluid and Movable Antenna Systems — spatial reconfiguration, port selection, fundamental performance limits, FAS-enabled UAV/URLLC, and prototype-aware research.
2. Reconfigurable Intelligent / Fluid Surfaces — reflective/transmissive RIS, FRIS, secure transmission, beam/pattern co-design, and programmable propagation.
3. Spatial and Index Modulation — space shift keying, spatial modulation, spatial scattering modulation, detectors, error analysis, and mmWave sparse channels.
4. AI-Assisted Reconfigurable Wireless Systems — learning-based port/surface control, model-driven learning, GNN/RL opportunities, and autonomous reconfiguration.

Add a final “Related topics” paragraph covering mmWave MIMO, finite-blocklength/URLLC, UAV and low-altitude communications, ISAC, channel measurement, and performance analysis.

- [ ] **Step 6: Implement `grants.md` and `service.md` from YAML**

`grants.md` iterates over `site.data.grants` and renders title, scheme, period, role, amount, and project ID.

`service.md` uses `_includes/service-list.html` for editorial and conference sections, and clearly separates Guest Editorship, Conference Leadership, Tutorial & Speaking, TPC Service, and Journal Reviewing.

- [ ] **Step 7: Add compact research and service highlights to `index.md`**

Add four research cards and a service highlight list containing “Editor, IEEE Transactions on Communications,” “Guest Editor, IEEE TAES Special Section,” and “Symposium Co-Chair, AIPIP 2026.”

- [ ] **Step 8: Run verification and commit**

Run `./tests/verify_site.sh`; expected PASS.

```bash
git add _data _includes/service-list.html research.md grants.md service.md index.md tests/verify_site.sh
git commit -m "feat: add research grants and academic service"
```

---

### Task 4: Add the publication database and publications page

**Files:**
- Create: `_data/publications.yml`
- Create: `_includes/publication-list.html`
- Modify: `publications.md`
- Modify: `index.md`
- Modify: `tests/verify_site.sh`

**Interfaces:**
- Consumes: the existing CSS/list patterns.
- Produces: structured publication data used by the Publications page and selected-publications section on Home.

- [ ] **Step 1: Add failing publication checks**

Append:

```bash
grep -q 'Fluid antenna systems: A geometric approach to error probability and fundamental limits' _site/publications/index.html
grep -q 'Transmissive RIS transmitter enabled spatial modulation for MIMO systems' _site/publications/index.html
grep -q 'On the performance of RIS-aided spatial modulation for downlink transmission' _site/publications/index.html
grep -q 'Selected Publications' _site/index.html
```

Run verification; expected FAIL.

- [ ] **Step 2: Create `_data/publications.yml` from the current CV**

Use YAML top-level keys:

```yaml
selected: []
first_corresponding_journals: []
other_journals: []
conference_papers: []
```

Each item must contain:

```yaml
- year: 2026
  authors: "X. Zhu, K.-K. Wong, H. Xu, H. Xiao, H. Hong, H. Shin, and Y. Zhang"
  title: "Fluid antenna systems: A geometric approach to error probability and fundamental limits"
  venue: "IEEE Transactions on Wireless Communications"
  details: "vol. 25, pp. 17195–17209, May 2026"
  selected: true
```

Populate the complete publication list represented in the current English CV, preserving author order, title, venue, year, volume/pages/DOI where supplied. Mark a concise set of representative works as `selected`, including at minimum:

- 2026 TWC: “Fluid antenna systems: A geometric approach to error probability and fundamental limits.”
- 2026 TWC: “Fluid antenna system-enabled UAV communications in the finite blocklength regime.”
- 2026 WCL: “Fluid reconfigurable intelligent surface enabling secure wireless communications.”
- 2025 TCOM: “Spatial scattering shift keying for mmWave MIMO systems.”
- 2025 JSAC: “Transmissive RIS transmitter enabled spatial modulation for MIMO systems.”
- 2024 TWC: “On the performance of RIS-aided spatial modulation for downlink transmission.”
- 2024 TWC: “Performance analysis of RIS-aided double spatial scattering modulation for mmWave MIMO systems.”

- [ ] **Step 3: Create `_includes/publication-list.html`**

Render an ordered list with year, authors, quoted title, italic venue, and details. Bold `X. Zhu` using Liquid replacement only if safe; otherwise store author markup explicitly in YAML and render with `markdownify`. Do not introduce external citation-JavaScript dependencies.

- [ ] **Step 4: Implement `publications.md`**

Create sections:

- Selected Publications
- First/Corresponding-Author Journal Articles
- Other Journal Articles
- Conference Papers

Add prominent Google Scholar link at the top.

- [ ] **Step 5: Add selected publications to Home**

Render only the selected subset, limited to 6–7 records, with a “View all publications” link.

- [ ] **Step 6: Verify and commit**

Run `./tests/verify_site.sh`; expected PASS.

```bash
git add _data/publications.yml _includes/publication-list.html publications.md index.md tests/verify_site.sh
git commit -m "feat: add structured publication record"
```

---

### Task 5: Add news posts and the News page

**Files:**
- Create: `_layouts/post.html`
- Create: `_posts/2026-04-01-msca-fellowship.md`
- Create: `_posts/2026-07-01-ieee-editorial-appointments.md`
- Create: `_posts/2026-08-01-taes-guest-editor.md`
- Create: `_posts/2026-09-01-aipip-symposium-co-chair.md`
- Create: `_posts/2026-05-01-fas-twc-publications.md`
- Create: `_posts/2026-06-01-2026-workshop-leadership.md`
- Modify: `news.md`
- Modify: `index.md`
- Modify: `tests/verify_site.sh`

**Interfaces:**
- Consumes: Jekyll post collection and shared layouts.
- Produces: chronological news index and home-page recent updates.

- [ ] **Step 1: Add failing news assertions**

Append:

```bash
grep -q 'Recent News' _site/index.html
grep -q 'MSCA' _site/news/index.html
grep -q 'AIPIP 2026' _site/news/index.html
```

Run verification; expected FAIL.

- [ ] **Step 2: Create the post layout**

`_layouts/post.html` must show title, formatted date, content, and a “Back to News” link while inheriting the same site header/footer.

- [ ] **Step 3: Add six factual initial news posts**

Each post uses front matter `layout: post`, `title`, and `date`. Keep posts concise (roughly 60–120 words) and factual. Initial subjects:

1. MSCA Postdoctoral Fellowship at UCL.
2. IEEE TCOM/WCL/CL/OJ-COMS editorial appointments.
3. IEEE TAES Special Section Guest Editorship.
4. AIPIP 2026 Symposium Co-Chair appointment.
5. 2026 TWC/FAS publications.
6. 2026 GLOBECOM/ICCC/VTC/ICC workshop leadership.

- [ ] **Step 4: Implement `news.md`**

Iterate over `site.posts`, newest first, and display date, linked title, and excerpt.

- [ ] **Step 5: Add the latest four posts to Home**

Use Liquid `limit: 4` and a “More news” link.

- [ ] **Step 6: Verify and commit**

Run `./tests/verify_site.sh`; expected PASS.

```bash
git add _layouts/post.html _posts news.md index.md tests/verify_site.sh
git commit -m "feat: add academic news and recent updates"
```

---

### Task 6: Add CV download, About/Contact details, and 404 page

**Files:**
- Copy: `/mnt/data/Xusheng_Zhu_Academic_Editorial_CV_Updated.pdf` → `assets/cv/Xusheng_Zhu_CV.pdf`
- Modify: `cv.md`
- Modify: `contact.md`
- Modify: `index.md`
- Create: `404.html`
- Modify: `tests/verify_site.sh`

**Interfaces:**
- Consumes: existing site styles and source CV asset.
- Produces: working CV download, complete contact page, and branded 404 handling.

- [ ] **Step 1: Add failing CV/contact assertions**

Append:

```bash
test -f _site/assets/cv/Xusheng_Zhu_CV.pdf
grep -q 'Department of Electronic & Electrical Engineering' _site/contact/index.html
grep -q 'xusheng.zhu@ucl.ac.uk' _site/contact/index.html
grep -q 'Google Scholar' _site/contact/index.html
grep -q 'ORCID' _site/contact/index.html
test -f _site/404.html
```

Run verification; expected FAIL.

- [ ] **Step 2: Copy the CV asset**

Run:

```bash
mkdir -p assets/cv
cp /mnt/data/Xusheng_Zhu_Academic_Editorial_CV_Updated.pdf assets/cv/Xusheng_Zhu_CV.pdf
```

- [ ] **Step 3: Complete `cv.md`**

Include a short statement that the downloadable academic CV contains appointments, grants, editorial service, conference leadership, awards, publication record, patents, standardization, and white papers. Add a prominent link to `/assets/cv/Xusheng_Zhu_CV.pdf`.

- [ ] **Step 4: Complete `contact.md`**

Publish only:

- Xusheng Zhu, Ph.D.
- Marie Skłodowska-Curie Actions Postdoctoral Fellow
- Department of Electronic & Electrical Engineering, University College London
- London, United Kingdom
- `xusheng.zhu@ucl.ac.uk`
- Google Scholar URL from Task 2
- ORCID `0000-0001-8463-0373`

Do not publish phone numbers.

- [ ] **Step 5: Add the concise About section to Home**

Write a short biography derived from the CV: 2025 Ph.D. in Information and Communication Engineering from Shanghai Jiao Tong University; current MSCA Fellow at UCL; research emphasis on 6G reconfigurable wireless systems; editorial and conference service highlighted without listing every role.

- [ ] **Step 6: Create `404.html`**

Use `layout: default`, `permalink: /404.html`, heading “Page not found,” a concise message, and a link back to Home.

- [ ] **Step 7: Verify and commit**

Run `./tests/verify_site.sh`; expected PASS.

```bash
git add assets/cv cv.md contact.md index.md 404.html tests/verify_site.sh
git commit -m "feat: add CV contact and not-found pages"
```

---

### Task 7: Finish SEO, accessibility, README deployment instructions, and final quality checks

**Files:**
- Modify: `_includes/head.html`
- Modify: `_config.yml`
- Modify: `README.md`
- Modify: `assets/css/main.css`
- Modify: `tests/verify_site.sh`

**Interfaces:**
- Consumes: the complete website from Tasks 1–6.
- Produces: production-ready metadata, accessibility polish, deployment documentation, and a final deterministic verification gate.

- [ ] **Step 1: Add final verification checks**

Append:

```bash
# No visible placeholders in source content.
if grep -RniE 'TBD|TODO|lorem ipsum' \
  --exclude-dir=.git --exclude-dir=_site --exclude='*.md' docs _data _includes _layouts *.md 2>/dev/null; then
  echo "Placeholder content found" >&2
  exit 1
fi

# Every primary page links the stylesheet and has a viewport meta tag.
for file in _site/index.html _site/research/index.html _site/publications/index.html _site/grants/index.html _site/service/index.html _site/news/index.html _site/cv/index.html _site/contact/index.html; do
  grep -q 'assets/css/main.css' "$file"
  grep -q 'name="viewport"' "$file"
done

# Sitemap generated.
test -f _site/sitemap.xml
```

- [ ] **Step 2: Finalize SEO and Open Graph metadata**

In `_includes/head.html`, ensure:

- `<meta name="viewport" content="width=device-width, initial-scale=1">`
- descriptive title using page title + site title.
- meta description from `page.description | default: site.description`.
- canonical URL.
- Open Graph title/description/type.
- Open Graph image pointing to `/assets/img/profile.jpg` for default social preview.
- `{% seo %}` and sitemap plugin remain enabled.

- [ ] **Step 3: Final accessibility polish**

In CSS/templates ensure:

- visible keyboard focus using `:focus-visible`.
- minimum 44px target height for primary nav/actions on touch layouts.
- portrait has descriptive alt text `Portrait of Xusheng Zhu`.
- heading hierarchy contains one H1 per page.
- external text links remain understandable without icons.
- colour contrast is readable on white and surface backgrounds.

- [ ] **Step 4: Write `README.md` with exact local and GitHub Pages steps**

README sections:

1. Prerequisites: Ruby, Bundler, Git.
2. Local setup:

```bash
bundle install
bundle exec jekyll serve
```

3. Open `http://127.0.0.1:4000/`.
4. Run verification:

```bash
./tests/verify_site.sh
```

5. GitHub Pages deployment:
   - create repository `<github-username>.github.io`;
   - push the project to the repository's default branch;
   - in GitHub `Settings → Pages`, choose deployment from the default branch/root if required by the account configuration;
   - set `_config.yml` `url` to `https://<github-username>.github.io` once username is known;
   - verify Home, CV download, and navigation after deployment.
6. Maintenance: add `_posts`, edit `_data/publications.yml`, `_data/grants.yml`, `_data/service.yml`, replace CV/photo assets.
7. Optional custom domain later: add domain in GitHub Pages settings, configure DNS, then set `_config.yml` `url` to the custom domain.

- [ ] **Step 5: Run Jekyll build and the full verification script**

Run:

```bash
./tests/verify_site.sh
```

Expected: PASS with no warnings that block the build.

- [ ] **Step 6: Run a local-server smoke test**

Run:

```bash
bundle exec jekyll serve --detach
curl -I http://127.0.0.1:4000/
curl -I http://127.0.0.1:4000/research/
curl -I http://127.0.0.1:4000/assets/cv/Xusheng_Zhu_CV.pdf
pkill -f 'jekyll serve' || true
```

Expected: HTTP 200 for all three URLs.

- [ ] **Step 7: Final repository status and commit**

Run:

```bash
git status --short
```

Confirm only intended files are modified, then:

```bash
git add .
git commit -m "docs: finalize academic site deployment and quality checks"
```

---

## Self-Review Results

- **Spec coverage:** All eight pages, portrait, structured research/publications/grants/service content, news posts, CV download, SEO, responsive design, accessibility, README deployment, and 404 handling are covered by Tasks 1–7.
- **Placeholder scan:** The plan contains no implementation placeholders; the only angle-bracket username token appears exclusively in deployment instructions where the GitHub username is genuinely user-specific and is not shipped as visible site content.
- **Data consistency:** Service roles, UCL affiliation, ORCID, Google Scholar URL, MSCA title/project ID/period, NSFC project ID/period, and the current editorial/conference roles align with the approved design and current CV-derived material.
- **Testing:** Every task adds a failing verification check before implementation and finishes by running the same deterministic site verification script.
