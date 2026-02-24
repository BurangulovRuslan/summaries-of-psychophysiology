# EEG–MNE Study Pack (private repo starter)

This repository is a compact, exam-oriented knowledge base + practical MNE-Python starter pipeline.

Contents
- `docs/EEG_Glossary_MNE.md` — detailed glossary (academic terms + “how it shows up in data” + MNE pointers)
- `docs/EEG_Pipeline_Checklist.md` — QC→preproc→ICA→epochs→ERP/TFR→stats checklist
- `docs/EEG_Exam_Cards.md` — short Q/A cards for fast revision
- `templates/Methods_EEG_MNE.md` — write-up template for Methods section (fill-in-the-blanks)
- `scripts/` — runnable examples (Raw QC, ICA clean, Epochs/ERP, Resting PSD, Task TFR)
- `environment/requirements.txt` — minimal dependencies

How to use (recommended)
1. Read the checklist once: `docs/EEG_Pipeline_Checklist.md`
2. Use the glossary while reading papers: `docs/EEG_Glossary_MNE.md`
3. Review cards before exams: `docs/EEG_Exam_Cards.md`
4. When analyzing your own data, start from `scripts/01_qc_raw.py` and proceed sequentially.

Notes
- The scripts are designed as templates. You must adapt file paths, channel names/types, event codes, and frequency bands.
- Links in docs point to the official MNE-Python documentation (`mne.tools`).
