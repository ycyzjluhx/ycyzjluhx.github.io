# Xusheng Zhu Academic Homepage — Design Specification

## Goal
Create a professional, English-language academic website for Dr. Xusheng Zhu that presents his research identity, publications, grants, editorial service, conference leadership, awards, and contact information in a form suitable for academic peers, funding panels, collaborators, and recruiters.

## Platform
- GitHub Pages
- Jekyll static site generator
- No server-side backend
- Responsive on desktop, tablet, and mobile
- Content maintained primarily through Markdown/YAML rather than editing HTML directly

## Visual Direction
A clean UCL/IEEE-inspired academic style:
- white background
- dark navy/blue typography and accents
- restrained use of a secondary accent color
- no decorative animations
- strong hierarchy and generous whitespace
- professional portrait on the home page

## Site Structure
Primary navigation:
1. Home
2. Research
3. Publications
4. Grants
5. Service
6. News
7. CV
8. Contact

## Home Page
The first screen will contain:
- professional portrait
- `Xusheng Zhu, Ph.D.`
- `Marie Skłodowska-Curie Actions Postdoctoral Fellow`
- Department of Electronic & Electrical Engineering, University College London
- concise research statement
- quick links: Google Scholar, ORCID, Email, CV

Below the hero section:
- About / short biography
- Research highlights
- Selected publications
- Recent news
- Academic service highlights
- selected grants/fellowships

Recommended research statement:
> I develop reconfigurable wireless technologies for 6G, with a focus on fluid and movable antennas, intelligent surfaces, spatial/index modulation, and AI-assisted wireless systems.

## Research Page
Four main research themes:
1. Fluid and Movable Antenna Systems
2. Reconfigurable Intelligent / Fluid Surfaces
3. Spatial and Index Modulation
4. AI-Assisted Reconfigurable Wireless Systems

Secondary topics may include mmWave MIMO, finite-blocklength/URLLC, UAV and low-altitude communications, ISAC, channel measurement, and performance analysis.

## Publications Page
Sections:
- Selected Publications
- First/Corresponding-Author Journal Articles
- Other Journal Articles
- Conference Papers

Each item can include year, title, venue, authors, DOI/link where available.
Google Scholar is linked prominently; the site will not attempt live citation synchronization in v1.

## Grants Page
Feature:
- Horizon Europe MSCA Postdoctoral Fellowship — SM-FAS
- NSFC doctoral project
- SJTU Outstanding Ph.D. Graduate Development Scholarship

Use original award currencies where possible.

## Service Page
### Editorial Service
- Editor, IEEE Transactions on Communications
- Associate Editor, IEEE Wireless Communications Letters
- Associate Editor, IEEE Communications Letters
- Associate Editor, IEEE Open Journal of the Communications Society
- Guest Editor, IEEE Transactions on Aerospace and Electronic Systems Special Section on Next-Generation Reconfigurable Antenna Systems for Aerospace Communications and Sensing

### Conference Leadership
- AIPIP 2026 Symposium Co-Chair
- IEEE GLOBECOM 2026 Workshop General Co-Chair
- IEEE/CIC ICCC 2026 Workshop General Co-Chair & Track Chair
- IEEE VTC 2026-Spring Workshop General Co-Chair
- IEEE/CIC ICCC 2026 FAS Workshop Session Chair
- IEEE ICC 2026 Workshop Session Chair
- IEEE/CIC ICCC 2026 Tutorial Presenter

### Additional Service
- Technical Program Committee service
- journal reviewing service

## News Page
Chronological entries managed as Jekyll posts. Initial items will include:
- MSCA fellowship at UCL
- IEEE TCOM editorship
- IEEE WCL/CL/OJ-COMS editorial appointments
- IEEE TAES Guest Editorship
- AIPIP 2026 Symposium Co-Chair appointment
- recent TWC/TCOM/FAS publications
- GLOBECOM/ICCC/VTC workshop leadership

## CV Page
- short overview
- button to download the latest English academic CV PDF
- optional link to full publication list

## Contact Page
- UCL affiliation
- UCL email
- Google Scholar
- ORCID
- optional LinkedIn/ResearchGate later

No personal phone number will be published in v1.

## Content Source
Primary source: the user's current English academic/editorial CV and the details confirmed in the conversation.
The site will not invent metrics, titles, affiliations, dates, or roles not supported by those materials.

## Files / Architecture
Proposed project structure:

```
.
├── _config.yml
├── _data/
│   ├── navigation.yml
│   ├── publications.yml
│   ├── grants.yml
│   └── service.yml
├── _includes/
├── _layouts/
├── _posts/
├── assets/
│   ├── css/main.css
│   ├── img/profile.jpg
│   └── cv/Xusheng_Zhu_CV.pdf
├── index.md
├── research.md
├── publications.md
├── grants.md
├── service.md
├── news.md
├── cv.md
├── contact.md
├── 404.html
├── Gemfile
└── README.md
```

## Maintenance Model
- Add a news item by creating one Markdown file in `_posts/`
- Add/update publications in `_data/publications.yml`
- Replace CV by overwriting `assets/cv/Xusheng_Zhu_CV.pdf`
- Replace profile photo by overwriting `assets/img/profile.jpg`

## SEO / Discoverability
- descriptive page titles and metadata
- Open Graph metadata
- canonical site title: `Xusheng Zhu | 6G Wireless Communications`
- keywords centered on UCL, MSCA, fluid antenna systems, reconfigurable intelligent surfaces, spatial modulation, and 6G
- sitemap and robots-compatible GitHub Pages output

## Accessibility and Quality
- semantic HTML
- alt text for profile image
- keyboard-accessible navigation
- readable contrast
- responsive layout
- no dependency on JavaScript for core content

## Deployment
Initial deployment target:
`https://<github-username>.github.io/`

Recommended later upgrade:
- purchase a personal domain such as `xushengzhu.com` or `xushengzhu.org`
- point the domain to GitHub Pages

## Acceptance Criteria
The project is complete when:
1. all eight pages build successfully with Jekyll;
2. the home page renders the supplied portrait cleanly;
3. all CV-derived roles and research information are represented accurately;
4. the site is responsive and readable on mobile;
5. internal links work;
6. CV download works;
7. README contains step-by-step GitHub Pages deployment instructions;
8. no placeholder/TBD content is visible on the live site.
