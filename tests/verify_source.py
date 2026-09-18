#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

required = [
    "_config.yml", "Gemfile", "_data/navigation.yml", "_data/publications.yml",
    "_data/grants.yml", "_data/service.yml", "_includes/head.html",
    "_includes/header.html", "_includes/footer.html", "_includes/publication-list.html",
    "_includes/service-list.html", "_layouts/default.html", "_layouts/home.html",
    "_layouts/post.html", "assets/css/main.css", "assets/img/profile.jpg",
    "assets/cv/Xusheng_Zhu_CV.pdf", "index.md", "research.md", "publications.md",
    "grants.md", "service.md", "news.md", "cv.md", "contact.md", "404.html",
    "README.md", ".github/workflows/pages.yml"
]

errors = []
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")

# YAML must parse.
for rel in ["_config.yml", "_data/navigation.yml", "_data/publications.yml", "_data/grants.yml", "_data/service.yml", ".github/workflows/pages.yml"]:
    try:
        yaml.safe_load((ROOT / rel).read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Invalid YAML {rel}: {exc}")

# Required content checks.
checks = {
    "index.md": ["Xusheng Zhu", "Recent News", "Selected Publications", "IEEE Transactions on Communications"],
    "research.md": ["Fluid and Movable Antenna Systems", "Reconfigurable Intelligent / Fluid Surfaces", "AI-Assisted Reconfigurable Wireless Systems"],
    "grants.md": ["Grants & Fellowships", "Selected Honors"],
    "service.md": ["Journal Editorial Service", "Guest Editorship", "Conference Leadership & Organization", "Tutorials & Speaking"],
    "publications.md": ["Selected Publications", "First/Corresponding-Author Journal Articles", "Conference Papers"],
    "contact.md": ["Department of Electronic & Electrical Engineering", "xusheng.zhu@ucl.ac.uk", "Google Scholar", "ORCID"],
    "cv.md": ["Download Academic CV (PDF)"],
    "_data/service.yml": ["IEEE Transactions on Aerospace and Electronic Systems", "AIPIP 2026", "Tutorial Presenter"],
    "_data/grants.yml": ["Spatial Multiplexing Fluid Antenna Systems (SM-FAS)", "101269517", "624B2094"],
    "_data/publications.yml": ["Fluid antenna systems: A geometric approach to error probability and fundamental limits", "Transmissive RIS transmitter enabled spatial modulation for MIMO systems", "On the performance of RIS-aided spatial modulation for downlink transmission"],
}
for rel, needles in checks.items():
    text = (ROOT / rel).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            errors.append(f"Missing text in {rel}: {needle}")

# Front matter on primary pages and posts.
for rel in ["index.md", "research.md", "publications.md", "grants.md", "service.md", "news.md", "cv.md", "contact.md", "404.html"] + [str(p.relative_to(ROOT)) for p in (ROOT / "_posts").glob("*.md")]:
    text = (ROOT / rel).read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"Missing front matter: {rel}")

# Navigation maps to all eight primary pages.
nav = yaml.safe_load((ROOT / "_data/navigation.yml").read_text(encoding="utf-8"))
expected_nav = {"Home", "Research", "Publications", "Grants", "Service", "News", "CV", "Contact"}
if {item["title"] for item in nav} != expected_nav:
    errors.append("Primary navigation does not match eight approved pages")

# Publication database shape and minimum completeness.
pubs = yaml.safe_load((ROOT / "_data/publications.yml").read_text(encoding="utf-8"))
if len(pubs.get("selected", [])) < 7:
    errors.append("Selected publication list has fewer than 7 records")
if len(pubs.get("first_corresponding_journals", [])) != 19:
    errors.append("First/corresponding journal list does not contain 19 records")
if len(pubs.get("other_journals", [])) != 16:
    errors.append("Other-journal list does not contain 16 records")

# No personal phone number and no visible placeholder content in shipping sources.
shipping = [
    *ROOT.glob("*.md"), *ROOT.glob("*.html"), *ROOT.glob("_data/*.yml"),
    *ROOT.glob("_includes/*.html"), *ROOT.glob("_layouts/*.html"), *ROOT.glob("_posts/*.md")
]
for path in shipping:
    text = path.read_text(encoding="utf-8")
    if re.search(r"\b(?:TBD|TODO|lorem ipsum)\b", text, flags=re.I):
        errors.append(f"Placeholder content found: {path.relative_to(ROOT)}")
    if "18093104505" in text or "+44 7962622256" in text:
        errors.append(f"Personal phone number found: {path.relative_to(ROOT)}")

# Basic Liquid delimiter sanity.
for path in [*ROOT.glob("*.md"), *ROOT.glob("*.html"), *ROOT.glob("_includes/*.html"), *ROOT.glob("_layouts/*.html")]:
    text = path.read_text(encoding="utf-8")
    if text.count("{{") != text.count("}}"):
        errors.append(f"Unbalanced Liquid output delimiters: {path.relative_to(ROOT)}")
    if text.count("{%") != text.count("%}"):
        errors.append(f"Unbalanced Liquid tag delimiters: {path.relative_to(ROOT)}")

# Key assets are nonempty.
for rel in ["assets/img/profile.jpg", "assets/cv/Xusheng_Zhu_CV.pdf", "assets/css/main.css"]:
    if (ROOT / rel).stat().st_size < 1000:
        errors.append(f"Asset unexpectedly small: {rel}")

if errors:
    print("SOURCE VERIFICATION FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("SOURCE VERIFICATION PASSED")
print(f"Primary pages: 8")
print(f"News posts: {len(list((ROOT / '_posts').glob('*.md')))}")
print(f"Journal records: {len(pubs['first_corresponding_journals']) + len(pubs['other_journals'])}")
print(f"Conference records: {len(pubs['conference_papers'])}")
