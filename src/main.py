# src/main.py
from setup_env import setup_path
# Set up the environment
setup_path()
from logging_config import setup_logging # type: ignore
from config import ENVIRONMENT

def main():
    setup_logging(ENVIRONMENT)
    from jikan_api.jikan_main import run
    run()

if __name__ == "__main__":
    main()
