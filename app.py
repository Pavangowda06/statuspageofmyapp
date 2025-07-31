import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8000))  # Azure provides PORT env var

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"Request: {self.client_address[0]} - {format % args}")

try:
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"✅ Serving at port {PORT}")
        httpd.serve_forever()
except Exception as e:
    print(f"❌ Server failed to start: {e}")
