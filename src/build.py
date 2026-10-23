"""Turns src/*.md into /<page>/index.html. Run: python3 src/build.py"""
import markdown, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
TPL = (root / "src" / "page.html").read_text()
for name, title, desc in [
    ("privacy", "Privacy policy", "How Evenso handles your information: everything stays on your device. No accounts, ads or analytics."),
    ("terms", "Terms of use", "The terms for using the Evenso app."),
    ("help", "Help", "Help with Evenso: backups, widgets, reminders and the daily check-in."),
]:
    md = (root / "src" / f"{name}.md").read_text()
    md = re.sub(r"^# .*\n", "", md, count=1)
    date = ""
    m = re.match(r"\s*Last updated: (.*)\n", md)
    if m:
        date = f'<p class="date">Last updated: {m.group(1)}</p>'
        md = md[m.end():]
    body = markdown.markdown(md, extensions=["md_in_html"])
    body = re.sub(r"evenso\.me/(privacy|terms)", r'<a href="/\1/">evenso.me/\1</a>', body)
    body = re.sub(r"(?<![\w:>/@])hello@evenso\.me(?!</a>)", '<a href="mailto:hello@evenso.me">hello@evenso.me</a>', body)
    html = TPL.replace("{{title}}", title).replace("{{desc}}", desc).replace("{{slug}}", name).replace("{{date}}", date).replace("{{body}}", body)
    out = root / name / "index.html"; out.parent.mkdir(exist_ok=True); out.write_text(html)
    print("wrote", out.relative_to(root))
