"""Scans the images/ folder and rewrites images.js so the gallery shows everything in it.
Run after adding or removing pictures:  python update_gallery.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(HERE, "images")
EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"}

files = sorted(
    f for f in os.listdir(IMG_DIR)
    if os.path.splitext(f)[1].lower() in EXTS
)

with open(os.path.join(HERE, "images.js"), "w", encoding="utf-8") as fh:
    fh.write("window.GALLERY_IMAGES = " + json.dumps(files, indent=2, ensure_ascii=False) + ";\n")

print(f"images.js updated with {len(files)} image(s).")
