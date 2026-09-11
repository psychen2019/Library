# ASGE 2026 Hemoglobin Threshold Validation

## Publication
- **ID**: MED-2026-2026ASGE指南内镜在急性下
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

### Validator Note
- **Date**: 2026-09-12
- **Validator**: Hermes (automated extraction + manual verification)
- **Method**: pdfplumber text extraction from PDF page 3
- **Verbatim source**: "7 g/L" (as written in the PDF)

### Clinical Interpretation
The source PDF explicitly states "7 g/L". This is almost certainly a **typesetting error** in the original publication - contemporary guidelines universally use **7 g/dL** as the restrictive transfusion threshold for LGIB. 

**Reference check**:
- Reference 14,15 in the ASGE 2026 guideline likely cite trials that used 7 g/dL (e.g., Villanueva et al., NEJM 2013)
- 7 g/L would be incompatible with life (~0.7 g/dL)
- Standard clinical threshold is 7 g/dL (70 g/L)

### Handling Decision
**Preserved verbatim as "7 g/L"** in refined MD with the following annotation:

```markdown
[CLINICAL NOTE: The value '7 g/L' appears exactly as shown in the source PDF (Page 3). 
This is almost certainly a typesetting error for '7 g/dL' (70 g/L), which is the 
standard restrictive transfusion threshold per contemporary guidelines and cited references. 
If clinically relevant, interpret as 7 g/dL.]
```

This approach:
1. **Preserves source fidelity** - we do not silently correct the PDF
2. **Provides clinical context** - flags the likely error for the reader
3. **Does not fabricate** - we do not claim the PDF says "7 g/dL" when it says "7 g/L"

### Verification Status
- `verification_status`: **partially-verified**
- Rationale: The high-risk numeric value has been validated against the PDF source, but the broader clinical content (tables, recommendations) requires additional verification.

---
**Generated**: 2026-09-12 by Hermes (Round 7 remediation)
