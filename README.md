# j-2-a

## Local development

If dependencies are not already present:

```powershell
python -m pip install --target .deps -r requirements.txt
```

Run the app:

```powershell
python wsgi.py
```

Open `http://127.0.0.1:3000/`.

## Project structure

- `pages/index.html`: the single page template, including the site script.
- `pages/site.css`: the site stylesheet.
- `assets/`: only the images currently used by the site.
- `.github/workflows/pages.yml`: GitHub Pages deployment workflow.

## GitHub Pages

Push to `main` and GitHub Actions will publish the static site to GitHub Pages.
The workflow stages `pages/index.html` as the published `index.html`, keeps `pages/site.css`, and copies `assets/` into the Pages artifact.
