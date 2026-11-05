# evenso-site

The evenso.me website (GitHub Pages, branch `main`, root). Plain HTML and CSS, no build tools needed to serve it.

**Coming Soon mode (5 Nov 2026):** the live site is only the Coming Soon page, a thank-you page and the legal pages Google Play
needs. No feature descriptions or screenshots until closed testing (12+ testers) is under way. The full site (home page with
features, help, screenshots) is kept, unpublished, on the branch `site-full`.

- `index.html` – Coming Soon: "Your day and your people, in one calm place." plus a tester sign-up. The form posts to
  FormSubmit (formsubmit.co), which emails each sign-up to hello@evenso.me; no backend. The very first submission sends an
  activation email to hello@evenso.me: click its link once, or sign-ups won't be forwarded. After a sign-up the visitor lands
  on `thanks/`.
- `privacy/`, `terms/` – made from `src/*.md` with `python3 src/build.py` (needs `pip install markdown`). Edit the `.md`, run the
  script, commit both. The privacy policy's source of truth is `play/privacy-policy.md` in the app repo; copy it here.
- `style.css` – shared styles (follows the visitor's light/dark setting). `img/` – the icon, the ring mark and the share picture.
