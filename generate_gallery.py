import os

image_folder = "photos"
html_path = "index.html"

# Get list of image files in /photos
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# Build <img> tags
image_tags = ""
for filename in sorted(image_files):  # optional: sort alphabetically
    image_tags += f'    <img src="{image_folder}/{filename}" alt="{filename}">\n'

# Read index.html
with open(html_path, "r", encoding="utf-8") as file:
    html = file.read()

# Replace content inside <div class="gallery">...</div>
start = html.find('<div class="gallery">')
end = html.find('</div>', start)
if start != -1 and end != -1:
    end += len('</div>')
    before = html[:start]
    after = html[end:]
    new_gallery = f'<div class="gallery">\n{image_tags}</div>'
    new_html = before + new_gallery + after

    # Backup
    with open("index_backup.html", "w", encoding="utf-8") as backup:
        backup.write(html)

    # Write updated index.html
    with open(html_path, "w", encoding="utf-8") as output:
        output.write(new_html)

    print("✅ index.html updated with photos from /photos folder.")
else:
    print("❌ Could not find <div class=\"gallery\"> in index.html")
