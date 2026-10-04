import os
import re
import urllib.parse
import subprocess
from datetime import datetime

SOURCE_DIR = '_posts'
TARGET_DIR = 'src/content/posts'
os.makedirs(TARGET_DIR, exist_ok=True)

# 1. Load Live Sitemap URLs
live_paths = {}
with open('/tmp/live_urls.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for loc in re.findall(r'<loc>https://frhyme\.github\.io(/.*?/)</loc>', text):
    decoded = urllib.parse.unquote(loc).strip('/')
    parts = decoded.split('/')
    # key by last part
    last_part = parts[-1]
    live_paths[last_part] = decoded
    live_paths[last_part.lower()] = decoded

print(f"Loaded {len(live_paths)} slug entries from live sitemap")

date_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2})-(.*)\.md$')
alt_date_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2})_(.*)\.md$')
fm_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n(.*)$', re.DOTALL)
title_pattern = re.compile(r'^title:\s*(.*)$', re.MULTILINE)
date_fm_pattern = re.compile(r'^date:\s*(.*)$', re.MULTILINE)
cat_pattern = re.compile(r'^(?:category|categories):\s*(.*)$', re.MULTILINE)
tags_pattern = re.compile(r'^(?:tag|tags):\s*(.*)$', re.MULTILINE)

def get_git_date(filepath):
    try:
        out = subprocess.check_output(['git', 'log', '-1', '--format=%ad', '--date=short', filepath], text=True).strip()
        if out and re.match(r'^\d{4}-\d{2}-\d{2}$', out):
            return out
    except Exception:
        pass
    mtime = os.path.getmtime(filepath)
    return datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')

total_scanned = 0
migrated = 0
skipped_empty = 0

for root, dirs, files in os.walk(SOURCE_DIR):
    for f in files:
        if not f.endswith('.md'):
            continue
        filepath = os.path.join(root, f)
        total_scanned += 1
        
        if os.path.getsize(filepath) == 0:
            skipped_empty += 1
            continue
            
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read().strip()
            
        if not content:
            skipped_empty += 1
            continue

        m1 = date_pattern.match(f)
        m2 = alt_date_pattern.match(f)
        
        if m1:
            file_date, raw_slug = m1.group(1), m1.group(2)
        elif m2:
            file_date, raw_slug = m2.group(1), m2.group(2)
        else:
            file_date = get_git_date(filepath)
            raw_slug = f[:-3]
            
        clean_s = re.sub(r'[\(\)\[\]\{\}\'\"`,]', '', raw_slug.strip())
        clean_s = re.sub(r'\s+', '-', clean_s)

        # Analyze content frontmatter
        m_fm = fm_pattern.match(content)
        
        title = None
        date_str = file_date
        category = 'others'
        tags = []
        body = content

        if m_fm:
            fm_text, body = m_fm.group(1), m_fm.group(2)
            
            tm = title_pattern.search(fm_text)
            if tm:
                title = tm.group(1).strip(' "\'')
                
            dm = date_fm_pattern.search(fm_text)
            if dm:
                d_val = dm.group(1).strip(' "\'')
                d_match = re.match(r'(\d{4}-\d{2}-\d{2})', d_val)
                if d_match:
                    date_str = d_match.group(1)
                    
            cm = cat_pattern.search(fm_text)
            if cm:
                cat_val = cm.group(1).strip(' []"\'')
                if cat_val and cat_val != 'tags:':
                    parts = re.split(r'[, ]+', cat_val)
                    if parts and parts[0] and parts[0] != 'tags:':
                        category = parts[0].strip()
                        
            tgm = tags_pattern.search(fm_text)
            if tgm:
                t_val = tgm.group(1).strip(' []"\'')
                for t in re.split(r'[, ]+', t_val):
                    t = t.strip()
                    if t and t not in tags:
                        tags.append(t)
        else:
            lines = content.split('\n')
            for line in lines:
                if line.startswith('#'):
                    title = line.lstrip('#').strip()
                    break

        if not title:
            title = raw_slug.replace('_', ' ').replace('-', ' ').title()

        # Determine exact canonical permalink matching live sitemap
        cand1 = re.sub(r'\s+', '-', raw_slug.strip())
        cand2 = re.sub(r'[\(\)\[\]\{\}\'\"`,]', '', raw_slug.strip())
        cand2 = re.sub(r'\s+', '-', cand2)
        cand3 = urllib.parse.quote(cand1)
        cand4 = re.sub(r'[\(\)\[\]\{\}\'\"`,]', '-', raw_slug.strip())
        cand4 = re.sub(r'[-_\s]+', '-', cand4).strip('-')
        cand5 = re.sub(r'[\(\)\[\]\{\}\'\"`,]', '-', raw_slug.strip())
        cand5 = re.sub(r'[-\s]+', '-', cand5).strip('-')

        live_match = (
            live_paths.get(cand1)
            or live_paths.get(cand1.lower())
            or live_paths.get(cand2)
            or live_paths.get(cand2.lower())
            or live_paths.get(cand3)
            or live_paths.get(cand4)
            or live_paths.get(cand4.lower())
            or live_paths.get(cand5)
            or live_paths.get(cand5.lower())
        )
        if live_match:
            permalink = f"/{live_match}/"
        else:
            cat_norm = category.lower().replace(' ', '-')
            permalink = f"/{cat_norm}/{cand2}/"

        # Fix image paths in body so they all start with /
        def fix_img(m):
            alt, src = m.group(1), m.group(2).strip()
            if src.startswith(('http://', 'https://', 'data:')):
                return f"![{alt}]({src})"
            src = re.sub(r'^(?:\.\./)+assets/images/', '/assets/images/', src)
            src = re.sub(r'^assets/images/', '/assets/images/', src)
            if not src.startswith('/'):
                basename = os.path.basename(src)
                if os.path.exists(os.path.join('assets/images/markdown_img', basename)):
                    src = f"/assets/images/markdown_img/{basename}"
                else:
                    src = f"/assets/images/{src}"
            src = src.replace('/assets/images/markdown_imgs/', '/assets/images/markdown_img/')
            return f"![{alt}]({src})"

        body = re.sub(r'\!\[(.*?)\]\((.*?)\)', fix_img, body)

        # Sanitize title to prevent invalid YAML escapes
        title = title.replace('\\', '').replace('"', "'")
        safe_title = title.strip()

        clean_tags = [t.replace('"', '').replace('\\', '') for t in tags[:10]]
        tag_yaml = "[" + ", ".join(f'"{t}"' for t in clean_tags) + "]" if clean_tags else "[]"
        new_fm = f"""---
title: "{safe_title}"
date: {date_str}
category: "{category}"
tags: {tag_yaml}
permalink: "{permalink}"
---
"""
        new_content = new_fm + "\n" + body.lstrip()

        target_filename = f"{date_str}-{clean_s}.md"
        target_path = os.path.join(TARGET_DIR, target_filename)

        counter = 1
        while os.path.exists(target_path):
            target_filename = f"{date_str}-{clean_s}-{counter}.md"
            target_path = os.path.join(TARGET_DIR, target_filename)
            counter += 1

        with open(target_path, 'w', encoding='utf-8') as out_fp:
            out_fp.write(new_content)

        migrated += 1

print(f"Total scanned: {total_scanned}")
print(f"Skipped empty: {skipped_empty}")
print(f"Migrated posts: {migrated}")
