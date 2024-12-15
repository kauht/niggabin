import subprocess
import time
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Your existing code goes here
        while True:
            print("Запуск app.py...")
            
            process = subprocess.Popen(["python", "app.py"])
            
            process.wait()
            
            if process.returncode != 0:
                print("app.py завершился с ошибкой. Перезапуск...")
            else:
                print("app.py завершился. Перезапуск...")
            
            time.sleep(1)
        
        self.wfile.write(b"Process started")
