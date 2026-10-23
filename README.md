# evenso-site

The evenso.me website (GitHub Pages, branch `main`, root). Plain HTML and CSS, no build tools needed to serve it.

- `index.html` – home page. `style.css` – shared styles (follows the visitor's light/dark setting).
- `help/`, `privacy/`, `terms/` – made from `src/*.md` with `python3 src/build.py` (needs `pip install markdown`). Edit the `.md`, run the script, commit both.
- `img/` – app screenshots (from the app repo's `SiteShotsTest`), dark and light.
