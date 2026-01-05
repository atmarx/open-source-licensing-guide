# Convert Images to WebP

Converts PNG images from `assets/images/` to optimized WebP format in `docs/assets/images/`.

## Usage

Run this skill when you have new PNG images in the root `assets/images/` folder that need to be converted for web use.

## Workflow

1. Check for PNG files in `assets/images/` that don't have corresponding WebP files in `docs/assets/images/`
2. Convert each PNG to WebP using `cwebp` with quality 85
3. Report file size savings

## Commands

Convert all new PNGs:
```bash
for png in assets/images/*.png; do
  filename=$(basename "$png" .png)
  webp="docs/assets/images/${filename}.webp"
  if [ ! -f "$webp" ]; then
    cwebp -q 85 "$png" -o "$webp"
    echo "Converted: $filename.png -> $filename.webp"
  fi
done
```

Convert a specific file:
```bash
cwebp -q 85 assets/images/FILENAME.png -o docs/assets/images/FILENAME.webp
```

## Quality Settings

- **85**: Good balance of quality and file size (default)
- **90**: Higher quality, larger files (use for hero images if needed)
- **75**: Smaller files, slight quality loss (use for thumbnails)

## Notes

- WebP typically achieves 70-90% size reduction vs PNG
- Original PNGs are preserved in `assets/images/` for archival
- Only WebP files in `docs/assets/images/` should be referenced in the site
