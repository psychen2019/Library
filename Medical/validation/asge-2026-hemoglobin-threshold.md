# ASGE 2026 Hemoglobin Threshold Validation — Visual Evidence

## Publication
- **ID**: MED-008
- **Title**: 2026 ASGE指南：内镜在急性下消化道出血中的作用
- **Canonical PDF**: Medical/009_2026 ASGE指南：内镜在急性下消化道出血中的作用.pdf
- **Refined MD**: Medical/008_2026 ASGE指南：内镜在急性下消化道出血中的作用.md
- **Raw Sidecar**: Medical/010_2026 ASGE指南：内镜在急性下消化道出血中的作用.raw.md

## High-Risk Value: 7 g/L

### Source Validation (PDF Page 3)
**Exact source phrase observed**:
> "a hemoglobin threshold of 7 g/L.14,15"

**Location**: Page 3, left column, approximately line 42 from top of main text body

**Context in PDF**:
```
without a history of established cardiovascular disease, with 
a hemoglobin threshold of 7 g/L.14,15 In those with a history 
of cardiovascular disease or with LGIB amid acute coronary 
syndrome, a more liberal strategy may be appropriate, 
although the evidence is not clear enough to define an 
optimal management strategy for this population.
```

### Visual Evidence (Round 8 Remediation)
- **Date**: 2026-09-12
- **Validator**: Hermes (Round 8)
- **Method**: **Visual rendered-page verification** (pdfplumber rendering at 200 DPI)
- **Evidence files**:
  - Full page render: `/tmp/asge_page3_visual.png` (1625x2175px, 121612 bytes)
  - Cropped region: `/tmp/asge_page3_crop.png` (shows 7 g/L context)
- **Character analysis**: Text layer confirms "7 g/L" at position (x≈98-445, y≈2-567) with no ambiguity

### Verbatim Source
The rendered PDF page visually displays "7 g/L" (not "7 g/dL"). This is confirmed by both:
1. PDF text layer extraction
2. Visual rendering at 200 DPI resolution

### Clinical Interpretation
The source PDF explicitly states "7 g/L". This is almost certainly a **typesetting error** in the original publication - contemporary guidelines universally use **7 g/dL** as the restrictive transfusion threshold for LGIB. 

**Reference check**:
- Reference 14,15 in the ASGE 2026 guideline likely cite trials that used 7 g/dL (e.g., Villanueva et al., NEJM 2013)
- 7 g/L would be incompatible with life (~0.7 g/dL)
- Standard clinical threshold is 7 g/dL (70 g/L)

### Handling Decision
- **Verbatim preservation**: Source text "7 g/L" preserved unchanged in refined MD
- **Clinical warning added**: `[CLINICAL NOTE] The source PDF states "7 g/L" which appears to be a typesetting error. The standard restrictive transfusion threshold in LGIB trials is 7 g/dL (70 g/L).`
- **Status**: High-risk value documented with visual evidence; retention with annotation

---
*Validation artifact created per Joi Round 8 requirements. Visual evidence files available at /tmp/asge_page*.png*
