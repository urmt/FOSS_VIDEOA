# FOSS_VIDEOA Control Center - Quick Start Guide

## 🚀 Getting Started (3 Steps)

### Step 1: Install Python Dependencies
```powershell
cd C:\Users\Roman\Projects\FOSS_VIDEOA\pipeline
pip install -r requirements.txt
```

### Step 2: Launch from Desktop
Double-click: **🎬 Start FOSS_VIDEOA Control Center.bat** on your desktop

The script will:
1. Check if Python is installed
2. Install Flask dependencies if needed
3. Start the backend server on http://localhost:5000
4. Your browser will automatically open the Control Center

### Step 3: Start Managing Your Pipeline!
The Control Center opens at `http://localhost:5000`

---

## 📂 Desktop Shortcuts

You have **3 files** on your desktop:

1. **🎬 Start FOSS_VIDEOA Control Center.bat** ← **USE THIS ONE**
   - Starts backend + opens browser automatically
   - Recommended for normal use

2. **🎬 FOSS_VIDEOA Control Center.bat**
   - Opens HTML file directly (no backend)
   - Will show connection errors (don't use this)

3. **FOSS_VIDEOA_Control_Center.html**
   - Standalone HTML copy
   - For reference only

---

## ✅ What's Working Now

### Frontend (Browser UI)
- ✅ Topic queue viewing (all 100 topics)
- ✅ Search and filter topics
- ✅ View topic details
- ✅ Mock script generation
- ✅ Pipeline monitoring UI
- ✅ Logging system
- ✅ Export functionality

### Backend (Flask API)
- ✅ RESTful API endpoints
- ✅ Topic queue management
- ✅ Persistent status updates (saves to topic_queue.json)
- ✅ Script generation (mock)
- ✅ Pipeline state tracking
- ✅ Centralized logging

### Connection
- ✅ CORS enabled (frontend ↔ backend)
- ✅ JSON file reading/writing
- ✅ Real-time status updates
- ✅ Error handling

---

## 🔧 Connection Issues - All Resolved!

### Issue 1: CORS Errors ✅ FIXED
**Problem:** Browser blocked requests from frontend to backend
**Solution:** `Flask-CORS` installed and enabled in backend_api.py

### Issue 2: File Access ✅ FIXED
**Problem:** Frontend couldn't read topic_queue.json from filesystem
**Solution:** Backend serves data via `/api/topics` endpoint

### Issue 3: State Persistence ✅ FIXED
**Problem:** Changes lost on page reload
**Solution:** Backend writes changes to topic_queue.json file

### Issue 4: No Backend Running ✅ FIXED
**Problem:** Original HTML file had no backend
**Solution:** Created Flask backend with full API

---

## 🌐 How to Use

### 1. Topic Queue Tab
- **View Topics:** See all 100 Ardour topics color-coded by priority
  - Red border = Priority 1 (foundational)
  - Orange border = Priority 2 (core features)
  - Blue border = Priority 3 (advanced)
- **Search:** Type keywords to filter topics
- **Filter:** Dropdown to filter by priority or status
- **Actions:**
  - 👁️ View - See topic details in modal
  - ✨ Generate - Create script for this topic
  - ✅ Complete - Mark topic as done

### 2. Script Generator Tab
- Select a topic from dropdown
- Click "Generate Script"
- Review:
  - Hook (opening line)
  - Tone (rant vs helpful)
  - Explanation steps
  - Demo actions for Ardour
  - Voiceover text (140-160 words)
  - On-screen text with timings
  - Hashtags
- Click "Approve" to queue for production

### 3. Pipeline Monitor Tab
- Start/Stop pipeline controls
- 8 pipeline stages with progress bars:
  1. Script Generation
  2. GUI Automation
  3. OBS Recording
  4. Subtitle Generation
  5. Voice Synthesis
  6. Background Generation
  7. FFmpeg Assembly
  8. Upload
- Real-time status updates (currently simulated)

### 4. Logs Tab
- View all system activity
- Color-coded messages:
  - Blue = Info
  - Green = Success
  - Red = Error
- Export logs to text file
- Clear logs button

---

## 📋 API Endpoints (for developers)

See `API_DOCUMENTATION.md` for complete details.

**Quick examples:**
```bash
# Get all topics
curl http://localhost:5000/api/topics

# Update topic status
curl -X PUT http://localhost:5000/api/topics/1/status \
  -H "Content-Type: application/json" \
  -d '{"status": "in_progress"}'

# Generate script
curl -X POST http://localhost:5000/api/script/generate \
  -H "Content-Type: application/json" \
  -d '{"topic_id": 1}'

# Start pipeline
curl -X POST http://localhost:5000/api/pipeline/start \
  -H "Content-Type: application/json" \
  -d '{"topic_id": 1}'
```

---

## 🔮 Recommended Next Enhancements

### 1. WebSockets for Real-time Updates
**Library:** Flask-SocketIO
```bash
pip install flask-socketio python-socketio
```
**Benefit:** Live pipeline progress without page refresh

### 2. Background Task Queue
**Library:** Celery + Redis
```bash
pip install celery redis
```
**Benefit:** Run video generation in background

### 3. Database Integration
**Library:** SQLAlchemy + SQLite
```bash
pip install sqlalchemy
```
**Benefit:** Better performance, complex queries

### 4. Actual LLM Integration
Connect to Ollama/vLLM for real script generation:
```bash
pip install ollama
```

---

## 🐛 Troubleshooting

### Backend won't start
```powershell
# Check Python version (need 3.8+)
python --version

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Can't access http://localhost:5000
- Check if backend is running (look for console window)
- Try restarting: close console, run desktop shortcut again
- Check firewall isn't blocking port 5000

### Topics not loading
- Verify `topic_queue.json` exists in `pipeline/` folder
- Check backend console for error messages
- Restart backend

### Browser shows old version
- Hard refresh: `Ctrl + Shift + R`
- Clear browser cache
- Close all browser windows and reopen

---

## 📞 Quick Reference

| Task | How To |
|------|--------|
| Start Control Center | Double-click desktop shortcut |
| Stop Backend | Close console window or `Ctrl+C` |
| View Topic Queue | Click "📋 Topic Queue" tab |
| Generate Script | Click "📝 Script Generator" tab |
| Monitor Pipeline | Click "⚙️ Pipeline Monitor" tab |
| View Logs | Click "📊 Logs" tab |
| Export Topics | "💾 Export Queue" button |
| Update Topic Status | Click ✅ button or "View" → change status |

---

## 📁 File Locations

```
C:\Users\Roman\Projects\FOSS_VIDEOA\pipeline\
├── backend_api.py           # Flask backend server
├── control_center.html      # Frontend UI
├── topic_queue.json         # 100 topics (editable)
├── requirements.txt         # Python dependencies
├── start_control_center.bat # Launcher script
├── logs/                    # Log files (auto-created)
└── API_DOCUMENTATION.md     # Full API reference

Desktop:
├── 🎬 Start FOSS_VIDEOA Control Center.bat  ← Use this!
├── 🎬 FOSS_VIDEOA Control Center.bat
└── FOSS_VIDEOA_Control_Center.html
```

---

**You're ready to manage your Ardour video factory! 🎬**
