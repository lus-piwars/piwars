"""
Synchronisation utilities to keep everything in sync.
"""
from threading import Thread
from typing import Optional

# the current challenge runs in a separate thread
# this can be used to abort the challenge
current_challenge: Optional[Thread] = None
