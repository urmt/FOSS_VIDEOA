# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

**Last Updated**: 2025-11-30
**Project**: FOSS_VIDEOA - Automated Ardour Short-Video Factory
**Location**: C:\Users\Roman\Projects\FOSS_VIDEOA
**GitHub**: https://github.com/urmt/FOSS_VIDEOA

## Project Overview

Automated pipeline for creating high-energy educational short-form videos (60 seconds) teaching Ardour DAW features on Fedora KDE Plasma. Produces 5-20 shorts per day with aggressive pro-FOSS messaging.

**Target Platform**: Fedora 41+ KDE Spin running on NVIDIA DGX Spark (8×H100/H200 GPUs)
**Philosophy**: 100% open source, 100% local processing, zero proprietary software

## Architecture

### Pipeline Flow
```
Topic Queue (100 topics) → 
Script Generation (Llama-3.1-405B) → 
GUI Automation (Dogtail) → 
OBS Recording (55s) → 
Subtitles (Whisper-large-v3) → 
Voiceover (XTTS-v2) → 
Background Visuals (Stable Diffusion 3) → 
Assembly (FFmpeg) → 
Multi-platform Upload
```

### Tech Stack
- **LLM**: Llama-3.1-405B-Instruct (GGUF Q4/Q5) via Ollama/vLLM
- **Vision**: Llama-3.2-11B-Vision for screenshot analysis
- **TTS**: XTTS-v2 fine-tuned for monster-truck announcer voice (or Piper)
- **Recording**: OBS Studio 30.2 + Wayland/KWin scripting
- **Automation**: Dogtail accessibility API (primary) or ydotool (fallback)
- **Video**: FFmpeg 7.1 with complex filter graphs
- **AI Visuals**: Stable Diffusion 3 Medium + AnimateDiff v3 + ControlNet
- **Subtitles**: Whisper-large-v3 (local)
- **Music**: Helm, Surge XT, ZynAddSubFX for CC-0 loops

### Directory Structure
```
FOSS_VIDEOA/
├── 00_SYSTEMS_ANALYSIS.md           # Full technical specification
├── 01_install_fedora_kde.sh         # Installation script (not yet created)
├── Systems-Analysis.md              # Original project spec
├── README.md                        # Project overview
├── WARP.md                          # This file
├── 02_finetune_announcer_voice/     # XTTS-v2 voice training (empty)
├── pipeline/
│   └── topic_queue.json             # 100 Ardour topics (prioritized)
├── assets/
│   ├── kde_wallpapers/              # KDE-themed backgrounds (empty)
│   └── music_loops_cc0/             # Creative Commons music (empty)
└── output/                          # Generated videos destination (empty)
```

## Development Commands

### Testing & Validation
No automated tests exist yet. When created:
- Python tests will likely use `pytest`
- Scripts must be tested on actual Fedora KDE system before deployment

### Pipeline Execution (Future)
```bash
# Full pipeline (Linux only, not yet implemented)
cd pipeline
./run_full_pipeline.sh

# Individual components (when created)
python script_generator.py --topic-id 1
python dogtail_ardour_actions.py --script demo_script.json
python recorder.py --duration 55
python voice_synth.py --input script.json
python background_generator.py --theme kde-plasma
python assembler.py --input assets/ --output output/
python uploader.py --video output/video.mp4
```

### Git Workflow
```powershell
cd C:\Users\Roman\Projects\FOSS_VIDEOA
git status
git add .
git commit -m "Descriptive message"
git push origin main
```

## Key Implementation Areas

### 1. Installation Script (01_install_fedora_kde.sh)
Automated Fedora KDE setup targeting DGX hardware:
- Install OBS Studio, Ardour, Python libs
- Configure PipeWire-JACK
- Install AI models (Llama, Whisper, Stable Diffusion, XTTS-v2)
- Enable KDE accessibility for Dogtail
- Configure Wayland/KWin scripting

### 2. Pipeline Scripts (pipeline/ directory)
All scripts need to be created with:
- **Extensive error checking** (per project rules)
- **Detailed comments** for maintainability
- **JSON-based configuration** where applicable
- **Real data only** - no placeholders or fake data

**Priority Order for Implementation:**
1. `topic_queue.json` management utilities
2. `script_generator.py` - LLM integration for script creation
3. `dogtail_ardour_actions.py` - GUI automation library
4. `recorder.py` - OBS recording orchestration
5. `voice_synth.py` - XTTS-v2 TTS integration
6. `background_generator.py` - Stable Diffusion visuals
7. `assembler.py` - FFmpeg video composition
8. `uploader.py` - Multi-platform publishing
9. `run_full_pipeline.sh` - Main orchestration script

### 3. Voice Model Training (02_finetune_announcer_voice/)
XTTS-v2 fine-tuning for "Epic Announcer" style:
- Collect sample audio with monster-truck rally announcer energy
- Create training dataset
- Fine-tune XTTS-v2 model
- Save checkpoints and configuration

### 4. Assets Collection
- KDE Plasma wallpapers and themes (kde_wallpapers/)
- CC-0 music loops from Helm, Surge XT, ZynAddSubFX (music_loops_cc0/)
- End card graphics (end_card.png - not yet created)

## Topic Queue Management

The `pipeline/topic_queue.json` contains 100 Ardour DAW topics:
- **Priority 1**: 10 topics (foundational, ready to start)
- **Priority 2**: 60 topics (core features)
- **Priority 3**: 30 topics (advanced features)
- **Status**: All currently "pending"

When working on videos:
1. Select next topic by priority
2. Generate script using LLM
3. Update topic status to "in_progress"
4. After successful video generation, update to "completed"

## Master Prompt for Script Generation

When implementing `script_generator.py`, use this prompt structure:

```
You are the most hyped Fedora KDE + Ardour evangelist alive.
You speak like a monster-truck rally announcer who discovered Linux in 1999 and never looked back.

Write ONE 55-second vertical short teaching exactly one Ardour concept on Fedora KDE Plasma.

Topic: {{TOPIC}}

Rules:
- Show KDE Plasma panel, Dolphin, or Latte Dock at least once
- Start with a 4–6s hook: 50% chance savage proprietary roast, 50% pure hype
- Teach completely and correctly
- Use exact menu names and shortcuts
- Say "Fedora KDE" at least once
- End with "This is why open source wins" + GitHub star call
- Voiceover: 140–160 words (perfect for 55s at announcer speed)

Output ONLY valid JSON:
{
  "hook": "string",
  "tone": "rant" | "helpful",
  "explanation": ["step 1", "..."],
  "demo_actions": ["click Edit > Preferences", "press Ctrl+Shift+R", ...],
  "voiceover_text": "full spoken script",
  "onscreen_text": ["00:00 HOOK TEXT", "00:15 Step 1", ...],
  "hashtags": ["#ArdourDAW", "#FedoraKDE", "#LinuxAudio", "#OpenSource", "#DitchAbleton", "#PlasmaGang"]
}
```

## Core Principles (Non-Negotiable)

1. **Fedora KDE Visible**: Every video shows KDE Plasma interface (Dolphin, Kate, Latte Dock, etc.)
2. **100% Open Source**: All tools, models, and generated assets are FOSS or CC-0
3. **Local Processing**: All AI models run on local hardware - no cloud APIs
4. **High Energy**: Monster-truck rally announcer style voiceover
5. **Dual Tone**: 50% helpful teacher, 50% anti-proprietary rants
6. **Extensive Error Checking**: All scripts must include detailed error handling
7. **Real Data Only**: Never use placeholders, fillers, or hallucinated data
8. **Documentation**: Always update WARP.md and README.md after significant changes

## Development Environment Notes

- **Current Environment**: Windows (development)
- **Target Environment**: Fedora 41+ KDE Plasma (production)
- **Cross-platform Considerations**: All scripts written for Linux deployment
- **Testing Strategy**: Must test on actual Fedora KDE system before production
- **Hardware Requirements**: Scripts optimized for NVIDIA DGX Spark (8×H100/H200)

## Current Project Status

**Completed:**
- ✅ Repository structure created
- ✅ Documentation files (README.md, 00_SYSTEMS_ANALYSIS.md, Systems-Analysis.md)
- ✅ Topic queue with 100 prioritized Ardour topics
- ✅ Asset directories created
- ✅ **Web-based Control Center UI (fully functional)**
- ✅ **Flask REST API backend (tested and working)**
- ✅ **Frontend-backend integration (operational)**
- ✅ **Desktop shortcuts for easy launch**
- ✅ **API documentation and quick start guides**

**Pending:**
- ⏳ Installation script (01_install_fedora_kde.sh)
- ⏳ Pipeline Python scripts (script_generator.py, recorder.py, etc.)
- ⏳ Voice model training scripts and datasets
- ⏳ Asset collection (wallpapers, music, end cards)
- ⏳ First video production test
- ⏳ Real LLM integration (currently mock data)

## Next Steps for Development

1. Create `01_install_fedora_kde.sh` with DGX-specific setup
2. Build Dogtail automation library for Ardour GUI control
3. Implement `script_generator.py` with LLM integration
4. Fine-tune XTTS-v2 voice model for announcer style
5. Develop FFmpeg assembly templates for 1080×1920 vertical video
6. Test full pipeline with Priority 1 topic
7. Scale to automated daily production

---

**Remember**: Update this file after every significant change to maintain accurate project state.
