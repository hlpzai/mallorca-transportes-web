import os
from PIL import Image, ImageOps

SRC = r"C:\Users\ray\Downloads\Transportes Mallorca-20260831T124637Z-1-001\Transportes Mallorca"
DST = r"C:\Users\ray\Downloads\Transportes Mallorca-20260831T124637Z-1-001\website\img"

os.makedirs(DST, exist_ok=True)

def save_resized(src_rel, dst_name, max_w, quality=78, crop_ratio=None):
    path = os.path.join(SRC, src_rel)
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)
    if im.mode in ("RGBA", "P"):
        bg = Image.new("RGB", im.size, (255, 255, 255))
        im = im.convert("RGBA")
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")

    if crop_ratio:
        w, h = im.size
        target_ratio = crop_ratio
        cur_ratio = w / h
        if cur_ratio > target_ratio:
            new_w = int(h * target_ratio)
            offset = (w - new_w) // 2
            im = im.crop((offset, 0, offset + new_w, h))
        else:
            new_h = int(w / target_ratio)
            offset = (h - new_h) // 2
            im = im.crop((0, offset, w, offset + new_h))

    w, h = im.size
    if w > max_w:
        new_h = int(h * (max_w / w))
        im = im.resize((max_w, new_h), Image.LANCZOS)

    out_path = os.path.join(DST, dst_name)
    im.save(out_path, "JPEG", quality=quality, optimize=True, progressive=True)
    print(dst_name, im.size, os.path.getsize(out_path) // 1024, "KB")


# Hero (wide banner crop)
save_resized("new-home-full-unopened-boxes.jpg",
             "hero-mudanzas-mallorca.jpg", 1920, quality=80, crop_ratio=16/9)

# OG / social share image
save_resized("new-home-full-unopened-boxes.jpg",
             "og-image.jpg", 1200, quality=75, crop_ratio=1200/630)

# Truck photos
save_resized("camion-usado-ocasion-segunda-mano-semi-nuevo-3500-kg-pma-nissan-nt400-cabstar-cerrado-trampilla-puerta-elevadora.jpg",
             "camion-transporte-mallorca.jpg", 1000, quality=80)

# NOTE: da7ed7b0-...jpg is NOT a vehicle photo, it's a generic gray avatar-placeholder
# graphic (two blank profile circles). Kept separately as img/avatar-placeholder.jpg
# for testimonial cards, cropped to a single circle. Do not use it for the fleet section.

save_resized("front-view-delivery-men-job-concept.jpg",
             "equipo-mudanzas-mallorca.jpg", 1200, quality=78, crop_ratio=4/3)

# Gallery (real jobs)
gallery = [
    ("fotos servicios hechos/image00001.jpeg", "trabajo-mudanza-01.jpg"),
    ("fotos servicios hechos/image00005.jpeg", "trabajo-mudanza-02.jpg"),
    ("fotos servicios hechos/image00010.jpeg", "trabajo-mudanza-03.jpg"),
    ("fotos servicios hechos/image00015.jpeg", "trabajo-mudanza-04.jpg"),
    ("fotos servicios hechos/image00020.jpeg", "trabajo-mudanza-05.jpg"),
    ("fotos servicios hechos/image00025.jpeg", "trabajo-mudanza-06.jpg"),
]
for src, dst in gallery:
    save_resized(src, dst, 900, quality=74, crop_ratio=4/3)

# Favicon source (orange island+truck icon, already square-ish transparent PNG)
fav_src = os.path.join(SRC, "icon mudanzas en mallorca.png")
im = Image.open(fav_src).convert("RGBA")
for size, name in [(512, "favicon-512.png"), (192, "favicon-192.png"), (32, "favicon-32.png"), (180, "apple-touch-icon.png")]:
    resized = im.resize((size, size), Image.LANCZOS)
    if name == "apple-touch-icon.png":
        bg = Image.new("RGBA", (size, size), (255, 255, 255, 255))
        bg.paste(resized, (0, 0), resized)
        bg.convert("RGB").save(os.path.join(DST, name), "PNG")
    else:
        resized.save(os.path.join(DST, name), "PNG")
    print(name, "done")

print("DONE")
