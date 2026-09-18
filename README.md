# Xusheng Zhu Academic Homepage

English academic website for **Xusheng Zhu, Ph.D.**, Marie Skłodowska-Curie Actions Postdoctoral Fellow at University College London.

The site is built with Jekyll and designed for GitHub Pages. Content is maintained primarily through Markdown and YAML.

## Site structure

- **Home** — academic profile, research highlights, selected publications, news, service, grants
- **Research** — four core research themes
- **Publications** — selected and full publication records
- **Grants** — fellowships, grants, and selected honors
- **Service** — editorial, guest-editor, conference, tutorial, TPC, and review service
- **News** — dated academic updates
- **CV** — downloadable academic CV
- **Contact** — UCL affiliation, email, Google Scholar, ORCID

## Prerequisites for local development

Install:

- Ruby 3.1 or later
- Bundler
- Git

Check installation:

```bash
ruby --version
bundle --version
git --version
```

## Local setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/<github-username>/<github-username>.github.io.git
cd <github-username>.github.io
bundle install
```

Start the site locally:

```bash
bundle exec jekyll serve
```

Open:

```text
http://127.0.0.1:4000/
```

Run verification:

```bash
./tests/verify_site.sh
```

When Jekyll is installed, the verification script builds the site and checks the generated output. In an offline environment without Jekyll dependencies, it performs deterministic source/data checks instead.

## Deploy with GitHub Pages

The repository includes `.github/workflows/pages.yml`, which builds Jekyll 4.x and deploys the generated site with GitHub Actions.

1. Create a GitHub repository named exactly:

   ```text
   <github-username>.github.io
   ```

2. Push this project to the repository's `main` branch.

3. On GitHub, open **Settings → Pages**.

4. Under **Build and deployment → Source**, choose **GitHub Actions**.

5. Push a commit, or open **Actions → Deploy Jekyll site to GitHub Pages → Run workflow**.

6. After the workflow completes, open:

   ```text
   https://<github-username>.github.io/
   ```

7. Update `_config.yml` once the final username is known:

   ```yaml
   url: "https://<github-username>.github.io"
   baseurl: ""
   ```

8. Verify Home, Research, Publications, News, and the CV download on the live site.

## Routine maintenance

### Add a news item

Create a Markdown file under `_posts/` using the pattern:

```text
YYYY-MM-DD-short-title.md
```

Example front matter:

```yaml
---
layout: post
title: "A concise update title"
date: 2026-09-18 09:00:00 +0100
---
```

### Update publications

Edit:

```text
_data/publications.yml
```

The publication page and selected-publications section on Home are generated from this file.

### Update grants or service

Edit:

```text
_data/grants.yml
_data/service.yml
```

### Replace the CV

Overwrite:

```text
assets/cv/Xusheng_Zhu_CV.pdf
```

Keep the same filename so all links continue to work.

### Replace the portrait

Overwrite:

```text
assets/img/profile.jpg
```

The page uses CSS cropping; no manual photo editing is required.

## Optional personal domain

Later, a domain such as `xushengzhu.com` or `xushengzhu.org` can be attached.

1. Purchase the domain.
2. In **GitHub → Settings → Pages**, enter the custom domain.
3. Configure DNS according to GitHub Pages instructions.
4. Change `_config.yml`:

   ```yaml
   url: "https://xushengzhu.com"
   baseurl: ""
   ```

5. Enable **Enforce HTTPS** after DNS has propagated.

## Content model

The site intentionally avoids live citation widgets and JavaScript dependencies for core content. This keeps the site fast, accessible, durable, and easy to maintain.
