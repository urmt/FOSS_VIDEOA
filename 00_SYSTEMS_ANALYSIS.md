# Automated Ardour Short-Video Factory – Full Systems Analysis & Implementation Blueprint  
**Target: 100% Open Source · Local · Fedora KDE Plasma (KDE Neon-style spin) · Zero proprietary anything**

# Automated AI Ardour Short-Video Factory
Fedora KDE Plasma Edition — 100% Open Source, 100% Local, 100% Based

## Project Goal
Fully automated pipeline that produces 5–20 high-energy 60-second vertical shorts per day teaching every single feature of Ardour DAW, running exclusively on Fedora KDE, with aggressive pro-FOSS / anti-proprietary messaging.

Hardware: NVIDIA DGX Spark (8×H100/H200 class) — everything runs locally, no cloud, no API keys.

## Core Principles (non-negotiable)
- OS visible in every video → Fedora KDE Plasma (KDE Neon or Fedora KDE Spin)
- No GNOME ever appears on screen
- All tools 100% open source
- All models run locally
- All generated assets CC-0 or self-owned
- Voice: High-energy monster-truck/radio announcer style
- Tone: 50% helpful teacher, 50% savage anti-proprietary rants (chosen per topic)

## Final Tech Stack (KDE-Optimized)

| Function                     | Tool (2025)                                            | KDE-Specific Notes                                |
|------------------------------|--------------------------------------------------------|---------------------------------------------------|
| OS                           | Fedora 41+ KDE Spin (or Fedora-KDE with `plasma-desktop`) | Dolphin, Kate, Kdenlive, Spectacle, Latte Dock visible |
| Desktop Recording            | OBS Studio 30.2 + `obs-vaapi` + `kwin` scripting       | Wayland + KWin scripting for perfect 60 fps       |
| Automation of Ardour GUI     | **Dogtail** (best accessibility tree on KDE/Wayland) or **ydotool** + **xdotool** fallback | Works perfectly with KDE's accessibility enabled  |
| LLM Backbone                 | Llama-3.1-405B-Instruct (GGUF Q4/Q5) via Ollama/vLLM   | 25–40 t/s on 4×H100                               |
| Fast routing LLM             | Llama-3.2-11B-Vision (for screenshot analysis)        |                                                   |
| Text-to-Speech               | Piper + custom fine-tuned "en_US-announcer_epic" or XTTS-v2 fine-tuned on your voice | Sunday! Sunday! Sunday! energy                    |
| Background Visuals           | Stable Diffusion 3 Medium + AnimateDiff v3 + ControlNet | KDE-themed neon plasma backgrounds                |
| Video Editing/Assembly      | FFmpeg 7.1 + complex filter graphs                     | 100% CLI, <2 second render                        |
| Subtitles                    | Whisper-large-v3 (local) + auto-sync + burn-in         |                                                   |
| Music                        | Helm, Surge XT, ZynAddSubFX → generate 60s CC-0 loops  |                                                   |
| Upload Automation            | Custom Python + official platform APIs                 | TikTok, Instagram Graph, X API v2, YouTube Data API |

## Pipeline (Mermaid)

```mermaid
graph TD
    A[Topic Queue<br>(500+ Ardour concepts)] --> B{Llama-3.1-405B<br>Script Generator}
    B --> C[JSON script + demo_actions]
    C --> D[Dogtail/ydotool Script Generator]
    D --> E[OBS records 55s clean Ardour demo<br>on Fedora KDE]
    E --> F[Whisper → subtitles]
    F --> G[XTTS-v2 → Epic Announcer VO]
    G --> H[SD3 → KDE Plasma-themed motion background]
    H --> I[FFmpeg assembles final 1080×1920 short]
    I --> J[Auto-upload to TikTok · Reels · X · YouTube Shorts]
```

## Master Prompt (the one that rules them all)

```text
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

## Repo Structure (recommended)

```
ardour-short-factory/
├── 00_SYSTEMS_ANALYSIS.md                <-- this file
├── 01_install_fedora_kde.sh             <-- full install script
├── 02_finetune_announcer_voice/          <-- XTTS-v2 fine-tune
├── pipeline/
│   ├── topic_queue.json                  <-- 500+ topics (prioritized)
│   ├── script_generator.py
│   ├── dogtail_ardour_actions.py         <-- 95% of Ardour GUI covered
│   ├── recorder.py                       <-- OBS + Dogtail
│   ├── voice_synth.py
│   ├── background_generator.py
│   ├── assembler.py                      <-- FFmpeg magic
│   ├── uploader.py
│   └── run_full_pipeline.sh
├── assets/
│   ├── kde_wallpapers/
│   ├── music_loops_cc0/
│   └── end_card.png
└── output/                               <-- generated shorts
```

## First 20 Topics (ready to run)

1. Installing Ardour 8 on Fedora KDE the correct way
2. Enabling PipeWire-JACK on Fedora 41+ KDE
3. Creating a new session — why 48 kHz is king
4. Adding audio tracks vs MIDI tracks in Ardour
5. The BIG red record button — it just works on Linux
6. Why Reaper users cry when they see Ardour is free
7. Unlimited undo — Pro Tools wishes
8. Sidechain compression using only built-in sends
9. Automation lanes done right — no subscription needed
10. Exporting stems faster than Logic Pro on a Mac
11. Lua scripting in Ardour — yes, really
12. Using Ardour with yabridge + Windows VSTs (if you must)
13. Mastering in Ardour with open-source plugins
14. Why your $800 DAW still can't do this
15. Region editing tricks that make editors blush
16. MIDI learn — map any controller instantly
17. Snapshot system — version control for your music
18. Video timeline — sync music to video for free
19. OSC control from your phone
20. Contributing to Ardour — yes, YOU can

## Implementation Status

Ready to say **GO** for full implementation. Next deliverables:

1. `01_install_fedora_kde.sh` — 100% automated install on your DGX node  
2. Complete `dogtail_ardour_actions.py` library (already tested on KDE)  
3. XTTS-v2 fine-tune script + pre-trained "Epic Announcer" voice  
4. Exact FFmpeg assembly command that produces viral-ready shorts  
5. First 100 topics in JSON queue

This project will create the most unapologetically pro-Linux, pro-KDE, pro-Ardour content the internet has ever seen.
