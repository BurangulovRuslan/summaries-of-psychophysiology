# Methods Template (EEG, MNE-Python)

Use this as a fill-in template for a thesis/paper. Replace bracketed fields.

## Participants
[Number of participants], [age range / mean±SD], [inclusion criteria], [ethics approval], [consent].

## Experimental design
[Within-subject / between-subject], conditions: [A, B, ...]. Order: [counterbalanced / fixed]. Tasks: [describe]. Resting-state: [EO/EC durations, number of blocks, purpose (QC / drift / baseline)].

## EEG acquisition
EEG was recorded using [system/model] with [N] channels positioned according to the [10–20 / 10–10] system. Sampling rate was [sfreq] Hz. Online reference was [reference]. Electrode impedances were maintained below [threshold] kΩ when possible.

## Preprocessing (MNE-Python)
All preprocessing was performed in MNE-Python ([version pinned in repository]).

### Channel setup and montage
Channel types were assigned (EEG/EOG/ECG/EMG/stim). Electrode positions were set using [standard montage name] / [digitized montage].

### Filtering and resampling
Data were filtered using [FIR/IIR] with a high-pass cutoff of [l_freq] Hz and low-pass cutoff of [h_freq] Hz. A notch filter at [50/60] Hz was applied if line noise was present. Data were resampled to [new_sfreq] Hz after anti-alias filtering.

### Bad channels and segment annotation
Bad channels were identified by [criteria: high variance, flatness, visual inspection] and marked as bad. Bad segments were annotated using a combination of visual inspection and automated methods (`annotate_amplitude` with thresholds [..], and `annotate_muscle_zscore` with parameters [..]) and excluded from ICA fitting and epoching. Bad channels were interpolated using spherical splines after montage assignment.

### Artifact correction
Ocular and cardiac artifacts were addressed using [ICA / SSP / regression]. For ICA, an [algorithm] decomposition was fit on [filtered range] data excluding annotated bad segments. Artifact components were identified using topography, time-series morphology, power spectral characteristics, and correlation with EOG/ECG channels. Identified components were excluded and the cleaned signal was reconstructed.

### Epoching and baseline correction (task)
Events were extracted using [find_events / events_from_annotations]. Data were epoched from [tmin] to [tmax] s relative to event onset. Baseline correction was applied using the interval [baseline]. Epochs were rejected using peak-to-peak thresholds of [..] for EEG and [..] for EOG and by excluding epochs overlapping BAD annotations.

### ERP analysis
Evoked responses were computed by averaging retained epochs per condition. Amplitudes were quantified as [mean amplitude in window / peak] in the window [..] ms at channels/ROIs [..].

### Spectral analysis (resting/task)
Power spectral density was estimated using Welch’s method with [window length / overlap] as implemented in MNE’s Spectrum interface. Band power was computed for [bands], using [absolute/relative] power and [log transform] where appropriate.

### Time–frequency analysis
Time–frequency representations were computed using [Morlet wavelets / multitaper], frequencies [..], `n_cycles` or bandwidth [..], and baseline correction method [logratio/percent/zscore] relative to [baseline].

## Statistical analysis
Hypotheses were tested using [paired t-tests / repeated-measures ANOVA / mixed-effects models]. Multiple-comparison control used [FDR / cluster-based permutation] with [parameters]. Effect sizes [..] were reported alongside p-values. Trial counts per condition were recorded and compared to ensure comparable SNR.

## Reproducibility
All scripts and parameters used for preprocessing and analysis are provided in the private repository. Package versions were pinned in `environment/requirements.txt` (or an equivalent lockfile). QC plots and logs were stored per subject.
