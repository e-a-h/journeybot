import json

from utils import Logging, Utils

MASTER_CONFIG = dict()
MASTER_LOADED = False
PERSISTENT = dict()
PERSISTENT_LOADED = False


def save():
    global MASTER_CONFIG
    with open('config.json', 'w') as json_file:
        json_file.write((json.dumps(MASTER_CONFIG, indent=4, skipkeys=True, sort_keys=True)))


# Ugly but this prevents import loop errors
def load():
    global MASTER_CONFIG, MASTER_LOADED
    try:
        with open('config.json', 'r') as json_file:
            MASTER_CONFIG = json.load(json_file)
            MASTER_LOADED = True
    except FileNotFoundError:
        Logging.error("Unable to load config, running with defaults.")
    except Exception as e:
        Logging.error("Failed to parse configuration.")
        print(e)
        raise e


def get_var(key, default=None):
    global MASTER_CONFIG, MASTER_LOADED
    if not MASTER_LOADED:
        load()
    if key not in MASTER_CONFIG.keys():
        MASTER_CONFIG[key] = default
        save()
    return MASTER_CONFIG[key]


def load_persistent():
    global PERSISTENT_LOADED, PERSISTENT
    PERSISTENT = Utils.fetch_from_disk('persistent')
    PERSISTENT_LOADED = True


def get_persistent_var(key, default=None):
    if not PERSISTENT_LOADED:
        load_persistent()
    return PERSISTENT[key] if key in PERSISTENT else default


def set_persistent_var(key, value):
    PERSISTENT[key] = value
    Utils.save_to_disk("persistent", PERSISTENT)
