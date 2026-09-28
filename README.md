# ankita1017.github.io

Personal site for Ankita Mathur. Static HTML and CSS, no build step, no JS.

## Files

```
index.html                  Home: hero, experience, education, recent work, selected writing (two groups), data art
img/ankita.jpg              Profile photo, 480px square from headshot.jpeg (shown in a circle)
img/                        Writing thumbnails (740x460), data-art pieces (740x555), the 2025 portrait
img/tools/                  Connector logos shown on the Customer data connectors tile
img/hotspots/               One 360x240 photo per portrait hotspot, named by hotspot id
img/logos/                  24px company marks for the experience/education rows
writing/index.html          Blog and essay links
404.html                    GitHub Pages serves this for unknown paths
css/site.css                All styles; tokens at the top
AnkitaMathur_Resume.pdf     The one primary action on the site
.nojekyll                   Tells Pages to serve files as-is
```

`/explainers/` is a separate repository (`ankita1017/explainers`) that Pages
mounts under this site. Nothing here touches it; the nav just links to it.

## Run locally

```
python3 -m http.server 8000
```

Open http://localhost:8000/. Links to `/explainers/` will 404 locally because
that content lives in the other repo.

## Deploy

The repository currently builds a Hugo site into a `gh-pages` branch. This
replaces that with plain files served from `main`.

1. In a clone of `ankita1017/ankita1017.github.io`, on `main`, delete the Hugo
   files: `.github/`, `.gitmodules`, `.hugo_build.lock`, `_config.yml`,
   `archetypes/`, `config.toml`, `resources/`, `themes/`.
2. Copy everything in this folder into the clone (including the dot-files
   `.nojekyll`; do not copy `AnkitaMathur_Resume_June2026.docx.pdf`,
   `linkedIn.pdf` or the `Screenshot *.png` reference files).
3. Commit and push to `main`.
4. On GitHub: Settings > Pages > Build and deployment > Source: "Deploy from a
   branch", Branch: `main`, folder `/ (root)`. Save.
5. Wait about a minute, then `curl -s https://ankita1017.github.io/ | grep -c
   "Selected outcomes"` should print `1`. The Pages build API reports the
   previous build as done, so poll the live HTML, not the API.
6. Optionally delete the now-unused `gh-pages` branch.

## Typeface

Helvetica Neue for everything (system font on macOS/iOS; Helvetica, then Arial
on other systems). The site downloads no font files.
Sizes: heading and byline 22px/30px, body text 15px/22px in #4A4948; column 64rem (960px).

## Review loop

`python3 tools/build-preview.py` bundles the home page into one self-contained
HTML file (CSS, fonts and images inlined; site links pointed at the live site).
Claude publishes it as a private artifact at
https://claude.ai/code/artifact/a7655ca5-85e0-44cd-9a0d-5110219cca43 after each
round. Open it, select anything, leave a comment and choose "Send to Claude";
Claude reads the comments, edits the source here, and republishes to the same
URL. `preview.html` is git-ignored; it is a build product.

## Editing

- Colors, weights and the type scale are CSS custom properties at the top of
  `css/site.css`. The site is white-only; there is no dark theme.
- Logos: each company's own favicon/app icon, saved as 128px PNG (Houseware's
  came from the Wayback Machine since houseware.io is gone; KCL's is a square
  cut from their SVG wordmark). Add a new row with
  `<img class="logo" src="img/logos/x.png" width="24" height="24" alt="">`.
- Thumbnails: the Medium one is the post's featured image (Medium's RSS feed at
  medium.com/feed/@anki-mat lists every post's images; the site itself blocks
  scripted fetches). The explainer one is the tile from /explainers/ captured
  at a 600px viewport. Keep new ones 740x460 JPEG.
- Layout follows the reference screenshots: one left-aligned column, monospace
  uppercase section labels, three-column rows with hairline dividers. The fold
  at 1280x800 should always hold the name, positioning line, intro, contact
  links and the resume button. After editing copy, check it:
  `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  --headless=new --window-size=1280,800 --screenshot=home.png http://localhost:8000/`
- Section order: Experience, Education, Recent work, Data and product, Musings,
  Data art. Section headings are the mono labels only; no intro sentences.
- The Ask Clari tile's chat is a CSS animation with made-up copy ("Acme deal"),
  not a product screenshot; edit the text in the `.chat` block. It loops every
  9 s and stops under `prefers-reduced-motion`.
- Hover layer (all CSS, no JS): experience rows reveal a `.more` line and their
  logo goes from grey to colour; writing thumbnails zoom 2%; work tiles gain a
  hairline; the nine `.dot`s on the data portrait show a tooltip. Rows and dots
  have `tabindex="0"`, so keyboard and tap work too. Dot positions are the
  percentages from the dear-data-2025 page's `hotspotData` (+5, +4 for centre).
  Hotspot photos: drop a 3:2 JPEG at `img/hotspots/<id>.jpg` where id is one of
  day-job, puzzles, exercise, reading, writing, loved-ones, vacation, walks,
  out-of-comfort; the tooltip picks it up (loved-ones has none yet).
- Recent-work tile copy is drafted in a Claude Doc ("Recent Work Tiles"); edit
  there and ask Claude to pull it in, or edit the two `.card` blocks directly.
- Update the date in the footer of each page when content changes.
