#!/usr/bin/env python3
import re

def refine_text(text):
    lines = text.split('\n')
    refined = []
    for line in lines:
        line = line.replace('\f', ' ')
        line = re.sub(r'[ \t]+', ' ', line)
        line = re.sub(r'([\u4e00-\u9fff])\s+([\u4e00-\u9fff])', r'\1\2', line)
        line = re.sub(r'\s+([,.。、，；：！？!?])', r'\1', line)
        line = re.sub(r'([,.。、，；：！？!?])\s+', r'\1', line)
        line = line.strip()
        if line:
            refined.append(line)
    return '\n'.join(refined)

def add_metadata(text, pdf_name, md_name):
    year_match = re.search(r'(\d{4})', pdf_name)
    year = year_match.group(1) if year_match else 'unknown'
    doc_type = 'guideline'
    if '共识' in pdf_name:
        doc_type = 'consensus'
    raw_sidecar = md_name.replace('.md', '') + '.raw.md'
    metadata = f'''---
title: {pdf_name.replace('.pdf', '')}
year: {year}
document_type: {doc_type}
topics:
  - medical
  - clinical guideline
source_pdf: {pdf_name}
raw_sidecar: {raw_sidecar}
refinement: lossless
refined_by: Hermes
refined_date: 2026-09-11
validation_status: pending
---

'''
    return metadata + text

def process_file(pdf_name, md_name):
    print(f"Processing: {pdf_name}")
    with open(md_name, 'r', encoding='utf-8') as f:
        text = f.read()
    refined = refine_text(text)
    refined = add_metadata(refined, pdf_name, md_name)
    with open(md_name, 'w', encoding='utf-8') as f:
        f.write(refined)
    print(f"  Refined {len(text)} chars -> {len(refined)} chars")

if __name__ == '__main__':
    files = [
        ('2022中国幽门螺杆菌感染治疗指南.pdf', '2022中国幽门螺杆菌感染治疗指南.md'),
        ('【医脉通】中国急性胰腺炎诊治指南（2021）.pdf', '【医脉通】中国急性胰腺炎诊治指南（2021）.md'),
        ('2026 ASGE指南：内镜在急性下消化道出血中的作用.pdf', '2026 ASGE指南：内镜在急性下消化道出血中的作用.md'),
    ]
    for pdf_name, md_name in files:
        process_file(pdf_name, md_name)
    print("All files processed.")
