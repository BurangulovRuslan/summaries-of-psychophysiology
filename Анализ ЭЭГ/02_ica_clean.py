# EEG Pipeline Checklist (MNE-Python)

This is a practical checklist you can follow per subject/session. It is intentionally conservative (prioritizes data integrity over “maximal cleaning”).

## A. Intake / integrity
1. Confirm recording metadata: montage, reference used during acquisition, sfreq, channel names/types.
2. Verify triggers/events: check event codes, timing, and whether latency/jitter exists (especially if events come via software).
3. Make a quick visual pass over Raw (10–30 s window) to catch gross problems: clipping, flat channels, huge drifts, missing channels.

MNE links (tutorials):
- https://mne.tools/stable/auto_tutorials/raw/10_raw_overview.html
- https://mne.tools/stable/auto_tutorials/raw/40_visualize_raw.html

## B. Channel types / montage / reference
1. Set correct channel types (EEG/EOG/ECG/EMG/stim/misc).
2. Apply the montage (sensor locations); verify left–right orientation.
3. Decide and document your analysis reference:
   - average reference (common default for EEG with adequate montage),
   - linked mastoids (common in ERP traditions),
   - CSD (surface Laplacian) for spatial sharpening (be explicit: it changes the data type).

MNE links:
- https://mne.tools/stable/auto_tutorials/preprocessing/55_setting_eeg_reference.html
- https://mne.tools/stable/auto_tutorials/intro/40_sensor_locations.html
- https://mne.tools/stable/generated/mne.preprocessing.compute_current_source_density.html

## C. Filtering / resampling (only after basics above)
1. Choose filter goals by analysis type:
   - ERP: modest high-pass (e.g., 0.1–0.5 Hz) + low-pass (e.g., 30–40 Hz).
   - Spectral/TFR: keep frequencies of interest; avoid unnecessary low-pass if you analyze beta/gamma.
2. Use notch filtering only if line noise is visible in PSD.
3. Resample after anti-alias low-pass (or rely on MNE’s resample path).

MNE links:
- https://mne.tools/stable/auto_tutorials/preprocessing/25_background_filtering.html
- https://mne.tools/stable/auto_tutorials/preprocessing/30_filtering_resampling.html

## D. QC: bad channels and bad segments
1. Mark bad channels (visual + statistics). Keep criteria consistent across subjects.
2. Annotate bad segments (movement, pops, saturations).
3. Consider automated helpers:
   - `annotate_amplitude` for peak/flat,
   - `annotate_muscle_zscore` for high-frequency muscle bursts.
4. Interpolate bad channels only after you have a correct montage.

MNE links:
- https://mne.tools/stable/auto_tutorials/raw/30_annotate_raw.html
- https://mne.tools/stable/generated/mne.preprocessing.annotate_amplitude.html
- https://mne.tools/stable/auto_examples/preprocessing/muscle_detection.html

## E. Artifact correction (ICA / SSP / regression)
1. Decide which approach is justified:
   - ICA: standard for EOG/ECG; muscle is trickier (often better as annotation/reject).
   - SSP: alternative for EOG/ECG.
   - EOG regression: niche; can overcorrect frontal brain signals.
2. Fit ICA on reasonably clean data (exclude annotated BAD segments).
3. Identify components using multiple evidence sources:
   - topography,
   - time series morphology (blinks/saccades vs “grainy” EMG),
   - PSD characteristics (EOG low-freq; EMG broad high-freq),
   - correlation with EOG/ECG channels if available.
4. Apply ICA and re-check PSD + raw browsing.

MNE links:
- https://mne.tools/stable/auto_tutorials/preprocessing/40_artifact_correction_ica.html
- https://mne.tools/stable/generated/mne.preprocessing.ICA.html
- https://mne.tools/stable/auto_tutorials/preprocessing/45_projectors_background.html

## F. Epoching / ERP (event-related)
1. Verify event mapping and timing.
2. Choose epoch window and baseline (pre-registered or literature-based).
3. Reject epochs by peak-to-peak (with calibrated thresholds) and/or by annotations.
4. Keep track of retained trial counts per condition.
5. Generate Evoked per condition; inspect joint plots and topomaps.

MNE links:
- https://mne.tools/stable/auto_tutorials/epochs/10_epochs_overview.html
- https://mne.tools/stable/auto_tutorials/evoked/10_evoked_overview.html

## G. Spectral / Resting-state
1. Confirm stationarity per segment (EO vs EC; pre vs post blocks).
2. Compute PSD using Spectrum interface; inspect alpha peak and line noise.
3. Use consistent band definitions (or individual alpha frequency where justified).
4. Document whether you use absolute or relative power and any log transforms.

MNE links:
- https://mne.tools/stable/auto_tutorials/time-freq/10_spectrum_class.html

## H. Time–frequency (task dynamics)
1. Select frequencies and time resolution (Morlet `n_cycles` or multitaper bandwidth).
2. Baseline-correct power appropriately (often logratio/dB).
3. Distinguish evoked vs induced effects (if relevant).
4. Plan statistics with multiple-comparisons control.

MNE links:
- https://mne.tools/stable/api/time_frequency.html

## I. Statistics / reporting
1. Predefine hypotheses, ROIs (channels), time windows, bands.
2. Use appropriate correction (FDR or cluster-based permutation).
3. Report effect sizes and trial counts, not only p-values.
4. Save QC plots and a reproducible log of parameters.

MNE links:
- https://mne.tools/stable/auto_tutorials/stats-sensor-space/10_background_stats.html
