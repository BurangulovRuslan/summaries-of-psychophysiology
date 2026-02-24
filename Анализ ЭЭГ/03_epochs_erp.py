# EEG Exam Cards (Q/A)

Use these as short prompts for fast recall.

1. What is EEG reference and why does it matter?
A: The reference defines the zero point for measured potentials; changing reference changes sensor-space waveforms and topographies and can affect ICA rank and interpretability.

2. Difference between Raw, Epochs, and Evoked?
A: Raw is continuous. Epochs are time-locked segments per event/trial. Evoked is the average of epochs per condition (ERP).

3. When is high-pass filtering dangerous for ERP?
A: High-pass that is too high can distort slow ERP components and baseline, producing artifactual deflections.

4. What evidence should you use to label an ICA component as “eye”?
A: (i) frontal topography, (ii) blink/saccade-like time series, (iii) low-frequency PSD dominance, (iv) correlation with EOG channel.

5. Typical signature of EMG contamination in PSD?
A: Broad-band increase at higher frequencies (often 20–80/100+ Hz), with “grainy” time series and peripheral/local topography.

6. What is baseline correction in ERP?
A: Subtract the mean of a pre-event interval to reduce offsets/drift and improve comparability across trials.

7. What is aliasing and how do you prevent it?
A: Spectral folding from insufficient sampling; prevent via anti-alias low-pass before downsampling and adequate sfreq.

8. What is cluster-based permutation testing?
A: A nonparametric multiple-comparisons control using spatiotemporal clustering and permutation-derived cluster statistics.

9. Evoked vs induced activity?
A: Evoked is phase-locked to events (visible in ERP). Induced is not necessarily phase-locked and is captured via time–frequency power.

10. Why do you need montage for topomaps?
A: Topomaps require sensor coordinates to interpolate scalp fields and define adjacency for cluster statistics.

MNE links (add to your personal notes):
- ICA tutorial: https://mne.tools/stable/auto_tutorials/preprocessing/40_artifact_correction_ica.html
- Spectrum: https://mne.tools/stable/auto_tutorials/time-freq/10_spectrum_class.html
- Stats background: https://mne.tools/stable/auto_tutorials/stats-sensor-space/10_background_stats.html
