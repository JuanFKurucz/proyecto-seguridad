import sys
import os
import msvcrt
import time

from src.utils.config import INPUT_TIMEOUT
from inputimeout import inputimeout, TimeoutOccurred
from getpass import getpass


def clear_screen():
    os.system("cls")


def ask(text):
    return inputimeout(prompt=f"{text}\n", timeout=INPUT_TIMEOUT)


def ask_password(text):
    return getpass(prompt=f"{text}\n")
