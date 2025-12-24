# app.py
"""Vulnerable PKI tool for security demo."""

import pickle
import subprocess
import hashlib

PASSWORD = "12345"  # Hardcoded secret


def dangerous_eval(user_input):
    return eval(user_input)  # RCE risk


def load_data(data):
    return pickle.loads(data)  # RCE risk


def clean_cache():
    # Command injection risk
    subprocess.call("rm -rf /tmp", shell=True)


def weak_hash(data):
    # Broken crypto (MD5)
    return hashlib.md5(data.encode()).hexdigest()


if __name__ == "__main__":
    print("PKI Tool Running...")
