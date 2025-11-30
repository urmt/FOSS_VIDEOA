# FOSS_VIDEOA Control Center - API Documentation

## Overview

The Control Center uses a **Flask REST API** backend to manage the video production pipeline. This separates the frontend (HTML/CSS/JavaScript) from the backend (Python), enabling:

- Real-time pipeline monitoring
- Persistent topic queue management
- Centralized logging
- Future integration with actual pipeline scripts

---

## Quick Start

### 1. Install Dependencies
```bash
cd C:\Users\Roman\Projects\FOSS_VIDEOA\pipeline
pip install -r requirements.txt
```

### 2. Start the Backend
```bash
python backend_api.py
```
Server will start on `http://localhost:5000`

### 3. Open Control Center
Navigate to `http://localhost:5000` in your browser, or double-click the desktop shortcut.

---

## API Endpoints

### System Status

#### `GET /api/status`
Get overall system status

**Response:**
```json
{
  "status": "ok",
  "pipeline_running": false,
  "current_topic": null,
  "timestamp": "2025-11-30T21:38:00"
}
```

---

### Topics Management

#### `GET /api/topics`
Get all topics from the queue

**Response:**
```json
{
  "topics": [
    {
      "id": 1,
      "title": "Installing Ardour 8 on Fedora KDE the correct way",
      "priority": 1,
      "status": "pending"
    },
    ...
  ],
  "metadata": {
    "total_topics": 100,
    "last_updated": "2025-11-30",
    "version": "1.0"
  }
}
```

#### `GET /api/topics/<topic_id>`
Get a specific topic by ID

**Response:**
```json
{
  "id": 1,
  "title": "Installing Ardour 8 on Fedora KDE the correct way",
  "priority": 1,
  "status": "pending"
}
```

#### `PUT /api/topics/<topic_id>/status`
Update a topic's status

**Request Body:**
```json
{
  "status": "in_progress"  // or "pending", "completed"
}
```

**Response:**
```json
{
  "success": true,
  "topic": {
    "id": 1,
    "title": "Installing Ardour 8 on Fedora KDE the correct way",
    "priority": 1,
    "status": "in_progress"
  }
}
```

---

### Script Generation

#### `POST /api/script/generate`
Generate a script for a topic

**Request Body:**
```json
{
  "topic_id": 1
}
```

**Response:**
```json
{
  "topic_id": 1,
  "topic_title": "Installing Ardour 8 on Fedora KDE the correct way",
  "hook": "While Pro Tools users are paying $600 a year, we're doing THIS for FREE!",
  "tone": "rant",
  "explanation": [...],
  "demo_actions": [...],
  "voiceover_text": "LADIES AND GENTLEMEN!...",
  "onscreen_text": [...],
  "hashtags": [...],
  "generated_at": "2025-11-30T21:38:00"
}
```

---

### Pipeline Control

#### `POST /api/pipeline/start`
Start the video production pipeline

**Request Body:**
```json
{
  "topic_id": 1
}
```

**Response:**
```json
{
  "success": true,
  "message": "Pipeline started",
  "topic_id": 1
}
```

#### `POST /api/pipeline/stop`
Stop the pipeline

**Response:**
```json
{
  "success": true,
  "message": "Pipeline stopped"
}
```

#### `GET /api/pipeline/status`
Get current pipeline status

**Response:**
```json
{
  "running": false,
  "current_topic": null,
  "stages": {
    "1": {
      "name": "Script Generation",
      "status": "Idle",
      "progress": 0,
      "details": ""
    },
    ...
  }
}
```

#### `PUT /api/pipeline/stages/<stage_id>`
Update a pipeline stage (for testing)

**Request Body:**
```json
{
  "status": "Running",
  "progress": 50,
  "details": "Processing topic #1"
}
```

---

### Logging

#### `GET /api/logs`
Get logs (optional query param: `?limit=100`)

**Response:**
```json
{
  "logs": [
    {
      "timestamp": "21:38:00",
      "type": "info",
      "message": "Backend API starting..."
    },
    ...
  ]
}
```

#### `POST /api/logs`
Add a log entry

**Request Body:**
```json
{
  "message": "Custom log message",
  "type": "info"  // or "success", "error"
}
```

#### `DELETE /api/logs`
Clear all logs

---

### Export

#### `GET /api/export/topics`
Export topics as JSON with export timestamp

---

## Frontend-Backend Connection Issues

### ✅ Resolved Issues

1. **CORS (Cross-Origin Resource Sharing)**
   - **Problem:** Browser blocks requests from `file://` to `http://localhost:5000`
   - **Solution:** Flask-CORS enabled in backend (`CORS(app)`)

2. **JSON File Loading**
   - **Problem:** Frontend couldn't load `topic_queue.json` directly from filesystem
   - **Solution:** Backend serves topics via `/api/topics` endpoint

3. **State Persistence**
   - **Problem:** Topic status changes were lost on page reload
   - **Solution:** Backend persists changes to `topic_queue.json`

4. **Real-time Updates**
   - **Problem:** Frontend didn't reflect backend changes
   - **Solution:** API endpoints provide current state; frontend polls/refreshes

---

## Recommended APIs & Tools

### Current Stack
- **Flask** (v3.0.0) - Lightweight Python web framework
- **Flask-CORS** (v4.0.0) - Handles cross-origin requests

### Future Enhancements

#### 1. **WebSockets for Real-time Updates**
**Library:** `Flask-SocketIO`
```bash
pip install flask-socketio python-socketio
```
**Benefit:** Push updates to frontend without polling (e.g., pipeline progress)

#### 2. **Background Task Queue**
**Library:** `Celery` + `Redis`
```bash
pip install celery redis
```
**Benefit:** Run pipeline scripts asynchronously without blocking API

#### 3. **Database for Advanced Querying**
**Library:** `SQLAlchemy` + `SQLite`
```bash
pip install sqlalchemy
```
**Benefit:** Complex queries, relationships, better performance for large datasets

#### 4. **Authentication (if needed)**
**Library:** `Flask-Login` or `Flask-JWT-Extended`
```bash
pip install flask-login
```
**Benefit:** Secure multi-user access

#### 5. **API Rate Limiting**
**Library:** `Flask-Limiter`
```bash
pip install flask-limiter
```
**Benefit:** Prevent API abuse

#### 6. **Monitoring & Metrics**
**Library:** `Prometheus` + `Grafana`
**Benefit:** Visualize pipeline performance, track video generation stats

---

## Connection Flow

```
┌──────────────┐
│   Browser    │
│  (Frontend)  │
└──────┬───────┘
       │ HTTP Requests
       │ (fetch API)
       ↓
┌──────────────┐
│ Flask Server │
│  (Backend)   │ ← Reads/Writes topic_queue.json
└──────┬───────┘
       │
       ↓
┌──────────────┐
│   Pipeline   │
│   Scripts    │ ← Future integration
│              │   (script_generator.py, etc.)
└──────────────┘
```

---

## Testing the Connection

### 1. Test Backend is Running
```bash
curl http://localhost:5000/api/status
```

### 2. Test Topic Loading
```bash
curl http://localhost:5000/api/topics
```

### 3. Test Topic Update
```bash
curl -X PUT http://localhost:5000/api/topics/1/status \
  -H "Content-Type: application/json" \
  -d "{\"status\": \"in_progress\"}"
```

### 4. Test Script Generation
```bash
curl -X POST http://localhost:5000/api/script/generate \
  -H "Content-Type: application/json" \
  -d "{\"topic_id\": 1}"
```

---

## Error Handling

The API includes comprehensive error checking:

- **404 Not Found:** Invalid endpoint or resource ID
- **400 Bad Request:** Invalid request data
- **500 Internal Server Error:** Backend failure (check console logs)

All errors return JSON:
```json
{
  "error": "Description of the error"
}
```

---

## Development Notes

### Running in Debug Mode
Flask debug mode is enabled by default (`debug=True` in `backend_api.py`):
- Auto-reload on code changes
- Detailed error messages
- **WARNING:** Disable in production!

### Logs Directory
Logs are stored in `pipeline/logs/` (auto-created on first run)

### Port Configuration
Default port is `5000`. To change:
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

---

## Next Steps

1. **Connect Real Scripts:** Replace mock script generation with actual LLM integration
2. **Pipeline Automation:** Link API endpoints to `script_generator.py`, `recorder.py`, etc.
3. **WebSocket Integration:** Add real-time progress updates
4. **Database Migration:** Move from JSON to SQLite for better performance
5. **Deployment:** Configure for production on Fedora KDE server

---

## Support

For issues or questions:
- Check Flask docs: https://flask.palletsprojects.com/
- Check CORS docs: https://flask-cors.readthedocs.io/
- Review backend logs in console
- Inspect browser console for frontend errors (F12)
