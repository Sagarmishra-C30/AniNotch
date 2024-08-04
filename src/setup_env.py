# src/setup_env.py
import sys
import os

def setup_path():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config'))
    if config_path not in sys.path:
        sys.path.append(config_path)
