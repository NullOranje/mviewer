from datetime import datetime
from enum import Enum


class State(Enum):
    NEW = "new"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    UNKNOWN = "unknown"


class Track(object):
    source: str
    destination: str
    state: State
    track_id: str
    date: datetime

    def __init__(self, track_id, source="", destination=""):
        self.source = source
        self.destination = destination
        self.state = State.NEW
        self.track_id = track_id


# Mock database transactions for now
class TrackDB(object):
    tracks: dict[str, Track]

    def __init__(self):
        self.tracks = dict()

    def add(self, track):
        self.tracks[track.track_id] = track

    def get(self, track_id):
        return self.tracks.get(track_id)

    def list(self):
        return self.tracks
