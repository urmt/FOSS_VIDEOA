#!/usr/bin/env python3
"""
FOSS_VIDEOA Control Center Backend API
Flask-based REST API for managing the video production pipeline
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Configuration
BASE_DIR = Path(__file__).parent
TOPIC_QUEUE_FILE = BASE_DIR / "topic_queue.json"
LOGS_DIR = BASE_DIR / "logs"
OUTPUT_DIR = BASE_DIR.parent / "output"

# Ensure directories exist
LOGS_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# In-memory pipeline state
pipeline_state = {
    "running": False,
    "current_topic": None,
    "stages": {
        "1": {"name": "Script Generation", "status": "Idle", "progress": 0, "details": ""},
        "2": {"name": "GUI Automation", "status": "Idle", "progress": 0, "details": ""},
        "3": {"name": "OBS Recording", "status": "Idle", "progress": 0, "details": ""},
        "4": {"name": "Subtitle Generation", "status": "Idle", "progress": 0, "details": ""},
        "5": {"name": "Voice Synthesis", "status": "Idle", "progress": 0, "details": ""},
        "6": {"name": "Background Generation", "status": "Idle", "progress": 0, "details": ""},
        "7": {"name": "FFmpeg Assembly", "status": "Idle", "progress": 0, "details": ""},
        "8": {"name": "Upload", "status": "Idle", "progress": 0, "details": ""}
    }
}

# Logs storage
logs = []


def log_message(message, log_type="info"):
    """Add a log entry with timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_entry = {
        "timestamp": timestamp,
        "type": log_type,
        "message": message
    }
    logs.append(log_entry)
    
    # Keep only last 1000 logs
    if len(logs) > 1000:
        logs.pop(0)
    
    print(f"[{timestamp}] [{log_type.upper()}] {message}")
    return log_entry


def load_topics():
    """Load topics from JSON file with error checking"""
    try:
        if not TOPIC_QUEUE_FILE.exists():
            log_message(f"Topic queue file not found: {TOPIC_QUEUE_FILE}", "error")
            return None
        
        with open(TOPIC_QUEUE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            log_message(f"Successfully loaded {len(data.get('topics', []))} topics", "info")
            return data
    except json.JSONDecodeError as e:
        log_message(f"Invalid JSON in topic queue file: {e}", "error")
        return None
    except Exception as e:
        log_message(f"Error loading topics: {e}", "error")
        return None


def save_topics(data):
    """Save topics to JSON file with error checking"""
    try:
        with open(TOPIC_QUEUE_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        log_message("Topics saved successfully", "success")
        return True
    except Exception as e:
        log_message(f"Error saving topics: {e}", "error")
        return False


# ============================================================================
# API ROUTES
# ============================================================================

@app.route('/')
def index():
    """Serve the control center HTML"""
    return send_from_directory('.', 'control_center.html')


@app.route('/api/status', methods=['GET'])
def get_status():
    """Get overall system status"""
    return jsonify({
        "status": "ok",
        "pipeline_running": pipeline_state["running"],
        "current_topic": pipeline_state["current_topic"],
        "timestamp": datetime.now().isoformat()
    })


@app.route('/api/topics', methods=['GET'])
def get_topics():
    """Get all topics from queue"""
    data = load_topics()
    if data is None:
        return jsonify({"error": "Failed to load topics"}), 500
    return jsonify(data)


@app.route('/api/topics/<int:topic_id>', methods=['GET'])
def get_topic(topic_id):
    """Get a specific topic by ID"""
    data = load_topics()
    if data is None:
        return jsonify({"error": "Failed to load topics"}), 500
    
    topic = next((t for t in data['topics'] if t['id'] == topic_id), None)
    if topic is None:
        return jsonify({"error": f"Topic {topic_id} not found"}), 404
    
    return jsonify(topic)


@app.route('/api/topics/<int:topic_id>/status', methods=['PUT'])
def update_topic_status(topic_id):
    """Update a topic's status"""
    data = load_topics()
    if data is None:
        return jsonify({"error": "Failed to load topics"}), 500
    
    new_status = request.json.get('status')
    if new_status not in ['pending', 'in_progress', 'completed']:
        return jsonify({"error": "Invalid status"}), 400
    
    topic = next((t for t in data['topics'] if t['id'] == topic_id), None)
    if topic is None:
        return jsonify({"error": f"Topic {topic_id} not found"}), 404
    
    old_status = topic['status']
    topic['status'] = new_status
    
    if save_topics(data):
        log_message(f"Topic #{topic_id} status changed: {old_status} → {new_status}", "success")
        return jsonify({"success": True, "topic": topic})
    else:
        return jsonify({"error": "Failed to save topics"}), 500


@app.route('/api/script/generate', methods=['POST'])
def generate_script():
    """Generate a script for a topic (mock implementation)"""
    topic_id = request.json.get('topic_id')
    
    data = load_topics()
    if data is None:
        return jsonify({"error": "Failed to load topics"}), 500
    
    topic = next((t for t in data['topics'] if t['id'] == topic_id), None)
    if topic is None:
        return jsonify({"error": f"Topic {topic_id} not found"}), 404
    
    log_message(f"Generating script for topic #{topic_id}: {topic['title']}", "info")
    
    # Mock script generation
    script = {
        "topic_id": topic_id,
        "topic_title": topic['title'],
        "hook": "While Pro Tools users are paying $600 a year, we're doing THIS for FREE!" if topic['priority'] == 1 else "Check out this INSANE feature in Ardour that'll blow your mind!",
        "tone": "rant" if topic['priority'] == 1 else "helpful",
        "explanation": [
            f"Open Ardour on your Fedora KDE desktop",
            f"Navigate to the relevant menu or press the shortcut",
            f"Demonstrate the feature with clear visual feedback",
            f"Show KDE Plasma interface elements throughout"
        ],
        "demo_actions": [
            "Launch Ardour from KDE menu",
            "Show Dolphin file manager briefly",
            "Demonstrate the specific Ardour feature",
            "Capture KDE panel and theme"
        ],
        "voiceover_text": f"LADIES AND GENTLEMEN! Today we're showing you {topic['title']} in Ardour on Fedora KDE Plasma! This is the kind of power that proprietary DAWs charge HUNDREDS for! And we're giving it to you for FREE! Watch how smooth this runs on our open-source desktop! THIS is why open source wins! Star us on GitHub!",
        "onscreen_text": [
            f"00:00 {topic['title'].upper()}",
            "00:10 Step-by-step demonstration",
            "00:45 100% FREE & OPEN SOURCE",
            "00:52 ⭐ Star on GitHub!"
        ],
        "hashtags": ["#ArdourDAW", "#FedoraKDE", "#LinuxAudio", "#OpenSource", "#DitchAbleton", "#PlasmaGang"],
        "generated_at": datetime.now().isoformat()
    }
    
    log_message(f"Script generated for topic #{topic_id}", "success")
    return jsonify(script)


@app.route('/api/pipeline/start', methods=['POST'])
def start_pipeline():
    """Start the video production pipeline"""
    if pipeline_state["running"]:
        return jsonify({"error": "Pipeline is already running"}), 400
    
    topic_id = request.json.get('topic_id')
    
    pipeline_state["running"] = True
    pipeline_state["current_topic"] = topic_id
    
    log_message(f"Pipeline started for topic #{topic_id}", "success")
    
    # Reset all stages
    for stage_id in pipeline_state["stages"]:
        pipeline_state["stages"][stage_id]["status"] = "Queued"
        pipeline_state["stages"][stage_id]["progress"] = 0
    
    return jsonify({
        "success": True,
        "message": "Pipeline started",
        "topic_id": topic_id
    })


@app.route('/api/pipeline/stop', methods=['POST'])
def stop_pipeline():
    """Stop the video production pipeline"""
    if not pipeline_state["running"]:
        return jsonify({"error": "Pipeline is not running"}), 400
    
    pipeline_state["running"] = False
    pipeline_state["current_topic"] = None
    
    log_message("Pipeline stopped", "info")
    
    # Reset all stages
    for stage_id in pipeline_state["stages"]:
        pipeline_state["stages"][stage_id]["status"] = "Idle"
        pipeline_state["stages"][stage_id]["progress"] = 0
    
    return jsonify({"success": True, "message": "Pipeline stopped"})


@app.route('/api/pipeline/status', methods=['GET'])
def get_pipeline_status():
    """Get current pipeline status"""
    return jsonify(pipeline_state)


@app.route('/api/pipeline/stages/<int:stage_id>', methods=['PUT'])
def update_stage(stage_id):
    """Update a pipeline stage status (for testing/simulation)"""
    stage_key = str(stage_id)
    if stage_key not in pipeline_state["stages"]:
        return jsonify({"error": "Invalid stage ID"}), 404
    
    status = request.json.get('status')
    progress = request.json.get('progress', 0)
    details = request.json.get('details', '')
    
    pipeline_state["stages"][stage_key]["status"] = status
    pipeline_state["stages"][stage_key]["progress"] = progress
    pipeline_state["stages"][stage_key]["details"] = details
    
    return jsonify({"success": True, "stage": pipeline_state["stages"][stage_key]})


@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Get all logs"""
    limit = request.args.get('limit', 100, type=int)
    return jsonify({"logs": logs[-limit:]})


@app.route('/api/logs', methods=['DELETE'])
def clear_logs():
    """Clear all logs"""
    logs.clear()
    log_message("Logs cleared", "info")
    return jsonify({"success": True, "message": "Logs cleared"})


@app.route('/api/logs', methods=['POST'])
def add_log():
    """Add a log entry"""
    message = request.json.get('message')
    log_type = request.json.get('type', 'info')
    
    entry = log_message(message, log_type)
    return jsonify({"success": True, "log": entry})


@app.route('/api/export/topics', methods=['GET'])
def export_topics():
    """Export topics as JSON"""
    data = load_topics()
    if data is None:
        return jsonify({"error": "Failed to load topics"}), 500
    
    data['metadata']['exported'] = datetime.now().isoformat()
    return jsonify(data)


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("FOSS_VIDEOA Control Center Backend API")
    print("=" * 60)
    print(f"Base Directory: {BASE_DIR}")
    print(f"Topic Queue: {TOPIC_QUEUE_FILE}")
    print(f"Logs Directory: {LOGS_DIR}")
    print(f"Output Directory: {OUTPUT_DIR}")
    print("=" * 60)
    
    log_message("Backend API starting...", "info")
    log_message(f"Topic queue file: {TOPIC_QUEUE_FILE}", "info")
    
    # Test loading topics on startup
    initial_data = load_topics()
    if initial_data:
        log_message(f"Found {len(initial_data.get('topics', []))} topics in queue", "success")
    else:
        log_message("Warning: Could not load topic queue on startup", "error")
    
    print("\n🚀 Starting server on http://localhost:5000")
    print("📋 Open http://localhost:5000 in your browser\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
