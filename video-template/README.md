# Video template project

Open this folder in Codex Desktop after installing the companion skill. Setup and troubleshooting are in `../HUONG_DAN_SETUP.md`; the illustrated guide is in `../docs/HUONG_DAN_CAI_DAT.pdf`.

Run `setup_windows.bat` first. It creates the Python environment, a private `.env` from `.env.example`, and original starter music/cue files. Set up your own ElevenLabs and CIT Voice Studio access before generating speech.

The current executable renderer is Mode B. Its sample data contains four paired-choice cards. Add a fifth card for 10 visible options, and supply original or properly licensed visuals in `source_research/reference_b_cutouts/`. Missing visuals appear as placeholders until replaced.
