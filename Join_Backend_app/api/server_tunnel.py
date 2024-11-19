from pyngrok import ngrok

http_tunnel = ngrok.connect(8000)  # Ändere den Port, falls nötig
print(f"Ngrok Tunnel URL: {http_tunnel.public_url}")
try:
    input("Drücke ENTER, um den Tunnel zu stoppen...")
finally:
    ngrok.disconnect(http_tunnel.public_url)