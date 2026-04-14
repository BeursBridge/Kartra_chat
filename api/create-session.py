import os
import json
from http.server import BaseHTTPRequestHandler
from openai import OpenAI

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        try:
            client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
            session = client.beta.chatkit.sessions.create(
                workflow_id=os.environ.get('VITE_CHATKIT_WORKFLOW_ID'),
                user_id="vercel-user"
            )
            self.wfile.write(json.dumps({"client_secret": session.client_secret}).encode())
        except Exception as e:
            self.wfile.write(json.dumps({"error": str(e)}).encode())
            
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok"}).encode())
