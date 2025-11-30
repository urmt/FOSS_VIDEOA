# WARP.md - Project Status Tracking

**Last Updated**: 2025-11-30  
**Project**: FOSS_VIDEOA - Automated Ardour Short-Video Factory  
**Location**: C:\Users\Roman\Projects\FOSS_VIDEOA

## Current Session Summary

Repository successfully cloned from https://github.com/urmt/FOSS_VIDEOA and initialized with complete project structure.

## Project Status

### ✅ Completed
- Repository cloned from GitHub
- Directory structure created:
  - `pipeline/` - Main automation scripts
  - `02_finetune_announcer_voice/` - Voice model training
  - `assets/kde_wallpapers/` - Visual assets
  - `assets/music_loops_cc0/` - Audio assets
  - `output/` - Generated videos destination
- Documentation files created:
  - `00_SYSTEMS_ANALYSIS.md` - Full technical blueprint
  - `README.md` - Project overview
  - `WARP.md` - This status file
- Topic queue created with 100 Ardour DAW topics in `pipeline/topic_queue.json`

### ⏳ Pending Implementation
1. **Installation Script** (`01_install_fedora_kde.sh`)
   - Automated Fedora KDE setup for DGX hardware
   - Install all dependencies (OBS, Ardour, Python libs, AI models)
   
2. **Pipeline Scripts** (in `pipeline/` directory)
   - `script_generator.py` - LLM-powered JSON script generation
   - `dogtail_ardour_actions.py` - GUI automation for Ardour
   - `recorder.py` - OBS recording orchestration
   - `voice_synth.py` - XTTS-v2 TTS integration
   - `background_generator.py` - Stable Diffusion visuals
   - `assembler.py` - FFmpeg video composition
   - `uploader.py` - Multi-platform publishing
   - `run_full_pipeline.sh` - Main orchestration script

3. **Voice Model Training** (in `02_finetune_announcer_voice/`)
   - XTTS-v2 fine-tuning scripts
   - Sample audio collection for "Epic Announcer" style
   - Training configuration and checkpoints

4. **Assets Collection**
   - KDE Plasma wallpapers and themes
   - CC-0 music loops (from Helm, Surge XT, ZynAddSubFX)
   - End card graphics

## Technical Architecture

### Target Hardware
- NVIDIA DGX Spark with 8×H100/H200 GPUs
- Running Fedora 41+ KDE Plasma Edition
- 100% local processing, no cloud APIs

### Key Technologies
- **LLM**: Llama-3.1-405B-Instruct (GGUF Q4/Q5) via Ollama/vLLM
- **Vision**: Llama-3.2-11B-Vision for screenshot analysis
- **TTS**: Piper or XTTS-v2 fine-tuned for monster-truck announcer voice
- **Recording**: OBS Studio 30.2 + Wayland/KWin scripting
- **Automation**: Dogtail accessibility API or ydotool
- **Video**: FFmpeg 7.1 with complex filter graphs
- **AI Visuals**: Stable Diffusion 3 Medium + AnimateDiff v3 + ControlNet

### Pipeline Flow
```
Topic Queue → Script Gen (LLM) → GUI Automation → OBS Recording → 
Whisper Subtitles → XTTS Voice → SD3 Background → FFmpeg Assembly → 
Multi-platform Upload
```

## Topic Queue Status
- **Total Topics**: 100
- **Priority 1 (Ready to Start)**: 10 topics
- **Priority 2 (Core Features)**: 60 topics  
- **Priority 3 (Advanced)**: 30 topics
- **Completed**: 0

## Next Working Session - Start Here

### Immediate Actions
1. Review and validate project structure
2. Begin implementation of `01_install_fedora_kde.sh`
3. Create skeleton Python scripts in `pipeline/` directory
4. Set up development environment (Python venv, dependencies)
5. Research Dogtail API for Ardour automation on KDE

### Key Decisions Needed
- Confirm target Fedora version (41+ or 42 beta?)
- Select TTS engine (Piper vs XTTS-v2 - XTTS-v2 preferred for voice cloning)
- Determine LLM inference backend (Ollama vs vLLM - depends on DGX setup)
- Define video resolution/format standards (1080×1920 vertical confirmed)

### Development Notes
- All scripts must include extensive error checking per project rules
- Use detailed comments for maintainability
- Keep WARP.md and README.md synchronized with progress
- Test on actual Fedora KDE system before production deployment
- This is a Windows development environment; scripts target Linux deployment

## Philosophy Reminder
**Core Principles (Non-Negotiable)**
- 100% Open Source - Zero proprietary tools
- 100% Local - All models run on DGX hardware
- KDE Plasma visible in every frame
- High-energy, pro-FOSS messaging
- "This is why open source wins"

## Git Status
- Branch: `main`
- Remote: `origin` (https://github.com/urmt/FOSS_VIDEOA)
- Working tree: Clean (new files not yet committed)

## Commands to Resume Work
```powershell
cd C:\Users\Roman\Projects\FOSS_VIDEOA
git status
# Review uncommitted changes, then commit initial structure
```

---

**Note**: This file should be updated after every significant change or work session to maintain accurate project state for next session startup.
