import re, base64, os

BASE = r"C:\Users\ray\Downloads\Transportes Mallorca-20260831T124637Z-1-001\website"
OUT = r"C:\Users\ray\AppData\Local\Temp\claude\c--Users-ray-Downloads-Transportes-Mallorca-20260831T124637Z-1-001\f8c530cc-4f90-4d13-b2f8-24a91c5256aa\scratchpad\mallorca-transportes-preview.html"

os.makedirs(os.path.dirname(OUT), exist_ok=True)

with open(os.path.join(BASE, "index.html"), encoding="utf-8") as f:
    html = f.read()
with open(os.path.join(BASE, "css", "styles.css"), encoding="utf-8") as f:
    css = f.read()
with open(os.path.join(BASE, "js", "main.js"), encoding="utf-8") as f:
    js = f.read()

MIME = {".svg": "image/svg+xml", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}

def to_data_uri(path):
    ext = os.path.splitext(path)[1].lower()
    mime = MIME[ext]
    with open(path, "rb") as f:
        b = f.read()
    return f"data:{mime};base64," + base64.b64encode(b).decode("ascii")

def replace_img(match):
    src = match.group(1)
    if not src.startswith("img/"):
        return match.group(0)
    path = os.path.join(BASE, src)
    uri = to_data_uri(path)
    return match.group(0).replace(src, uri)

html = re.sub(r'src="(img/[^"]+)"', replace_img, html)

# Strip <!doctype>, <html>, <head>...</head> open tag, </html>
html = re.sub(r'<!doctype html>\s*<html[^>]*>\s*', '', html, flags=re.I)
html = re.sub(r'</html>\s*$', '', html, flags=re.I)

head_match = re.search(r'<head>(.*?)</head>', html, flags=re.S)
head_content = head_match.group(1)
html = html[:head_match.start()] + html[head_match.end():]

title_match = re.search(r'<title>.*?</title>', head_content, flags=re.S)
title_tag = title_match.group(0)

font_links = re.findall(r'<link rel="preconnect".*?>|<link href="https://fonts\.googleapis\.com.*?>', head_content)

body_match = re.search(r'<body>(.*)</body>', html, flags=re.S)
body_content = body_match.group(1)

# Inline the CSS and JS files (linked versions won't exist in the artifact)
body_content = body_content.replace('<link rel="stylesheet" href="css/styles.css">', '')
body_content = re.sub(r'\s*<script src="js/main\.js"></script>\s*', f'\n<script>\n{js}\n</script>\n', body_content)

out = title_tag + "\n" + "\n".join(font_links) + f"\n<style>\n{css}\n</style>\n" + body_content

with open(OUT, "w", encoding="utf-8") as f:
    f.write(out)

print("Written:", OUT)
print("Size KB:", os.path.getsize(OUT) // 1024)
