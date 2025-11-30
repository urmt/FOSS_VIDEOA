# FOSS_VIDEOA - Automated Ardour Short-Video Factory

**100% Open Source · 100% Local · 100% Based**

## Overview

This project is an ambitious automated pipeline for creating high-energy, educational short-form videos (60 seconds) teaching Ardour DAW features on Fedora KDE Plasma. The goal is to produce 5-20 shorts per day with aggressive pro-FOSS messaging.

## Target Platform

- **OS**: Fedora 41+ KDE Spin (KDE Plasma Desktop)
- **Hardware**: NVIDIA DGX Spark (8×H100/H200 class GPUs)
- **Philosophy**: Everything runs locally, no cloud APIs, zero proprietary software

## Core Principles

1. **Fedora KDE Visible**: Every video shows KDE Plasma interface (Dolphin, Kate, Latte Dock, etc.)
2. **100% Open Source**: All tools, models, and generated assets are FOSS or CC-0
3. **Local Processing**: All AI models run on local hardware
4. **High Energy**: Monster-truck rally announcer style voiceover
5. **Dual Tone**: 50% helpful teacher, 50% anti-proprietary rants

## Tech Stack

- **LLM**: Llama-3.1-405B-Instruct (local via Ollama/vLLM)
- **Vision**: Llama-3.2-11B-Vision for screenshot analysis
- **TTS**: Piper or XTTS-v2 (fine-tuned for epic announcer voice)
- **Recording**: OBS Studio 30.2 with Wayland/KWin scripting
- **Automation**: Dogtail or ydotool for GUI control
- **Visuals**: Stable Diffusion 3 Medium + AnimateDiff v3
- **Video**: FFmpeg 7.1 for assembly
- **Subtitles**: Whisper-large-v3 (local)
- **Music**: Helm, Surge XT, ZynAddSubFX for CC-0 loops

## Project Structure

```
FOSS_VIDEOA/
├── 00_SYSTEMS_ANALYSIS.md           # Full technical documentation
├── 01_install_fedora_kde.sh         # Automated installation script
├── Systems-Analysis.md              # Original project specification
├── README.md                        # This file
├── WARP.md                          # Project status tracking
├── 02_finetune_announcer_voice/     # XTTS-v2 voice training
├── pipeline/
│   ├── topic_queue.json             # 100 Ardour topics (prioritized)
│   ├── script_generator.py          # LLM-powered script creation
│   ├── dogtail_ardour_actions.py    # Ardour GUI automation
│   ├── recorder.py                  # OBS recording automation
│   ├── voice_synth.py               # TTS generation
│   ├── background_generator.py      # Visual effects creation
│   ├── assembler.py                 # FFmpeg video assembly
│   ├── uploader.py                  # Multi-platform upload
│   └── run_full_pipeline.sh         # Main execution script
├── assets/
│   ├── kde_wallpapers/              # KDE-themed backgrounds
│   ├── music_loops_cc0/             # Creative Commons music
│   └── end_card.png                 # Video outro graphic
└── output/                          # Generated short videos
```

## Pipeline Flow

1. **Topic Selection**: Pick next topic from queue (100 Ardour concepts)
2. **Script Generation**: Llama-3.1-405B creates JSON script with demo actions
3. **GUI Automation**: Dogtail/ydotool script controls Ardour
4. **Recording**: OBS captures 55-second Fedora KDE screen recording
5. **Subtitles**: Whisper generates and syncs captions
6. **Voiceover**: XTTS-v2 creates epic announcer audio
7. **Background**: Stable Diffusion generates KDE Plasma-themed visuals
8. **Assembly**: FFmpeg combines all elements into 1080×1920 vertical short
9. **Upload**: Auto-publish to TikTok, Instagram Reels, X, YouTube Shorts

## Topic Categories (100 Total)

- **Getting Started**: Installation, setup, basic concepts (Priority 1)
- **Core Features**: Tracks, recording, editing, mixing (Priority 2)
- **Advanced**: Lua scripting, OSC control, video timeline (Priority 3)
- **Plugins**: Open-source plugin ecosystem (Calf, LSP, X42)
- **MIDI**: Controllers, virtual instruments, sequencing
- **Export**: Formats, stems, mastering, loudness
- **Workflow**: Shortcuts, templates, organization

## Current Status

✅ Repository cloned and initialized  
✅ Directory structure created  
✅ 100 topics queued in JSON format  
✅ Project documentation complete  
⏳ Implementation scripts pending  
⏳ Voice model training pending  
⏳ Pipeline automation pending  

## Next Steps

1. Create installation script (`01_install_fedora_kde.sh`)
2. Build Dogtail automation library for Ardour
3. Fine-tune XTTS-v2 voice model for announcer style
4. Develop FFmpeg assembly templates
5. Test full pipeline with first topic
6. Scale to daily automated production

## Contributing

This is an open-source project! Contributions welcome for:
- Additional Ardour topics
- Voice model improvements
- Automation scripts
- KDE-themed visual assets
- Pipeline optimizations

## License

All code and assets are open source. Generated videos will be CC-0 or self-owned.

## Philosophy

> "This is why open source wins."

We're making unapologetically pro-Linux, pro-KDE, pro-Ardour content that teaches while inspiring people to ditch proprietary tools. Every video celebrates the power of FOSS software running on community-driven platforms.

---

**Let's make KDE and Ardour famous. 🚀**
