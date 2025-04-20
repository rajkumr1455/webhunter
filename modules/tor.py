import subprocess

class TorProxy:
    def __init__(self, tor_port=9050):
        self.tor_port = tor_port

    def set_proxy(self):
        subprocess.run(f"export http_proxy=socks5h://127.0.0.1:{self.tor_port} && export https_proxy=socks5h://127.0.0.1:{self.tor_port}", shell=True)

    def stop_tor(self):
        subprocess.run("sudo systemctl stop tor", shell=True)

    def start_tor(self):
        subprocess.run("sudo systemctl start tor", shell=True)
