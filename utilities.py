from settings import *
from pathlib import Path


def getFontPath():
    return str(next(Path(f"{Path.cwd()}\\graphics\\font").iterdir()))