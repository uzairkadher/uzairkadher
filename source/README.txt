UZAIR KADHER - Black Gold GitHub profile (source)

Upload to your repo (uzairkadher/uzairkadher): README.md + assets/ (preview.html is optional).

Rebuild from source (run inside this folder):
  pip install pillow opencv-python numpy fonttools
  python3 cut.py     # photo.jpg -> ../assets/id.png, ../assets/right_pointing.png (+ id_embed.png, rp_embed.png)
  python3 build.py   # embeds PNGs + fonts -> ../assets/*.svg, ../README.md, ../preview.html

To use your own generated art: replace ../assets/id.png / right_pointing.png, resize copies to
id_embed.png (~740x775) and rp_embed.png (~775x705), then run only build.py.
