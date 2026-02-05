import uuid
from dataclasses import dataclass
from typing import TypedDict, List

from flask import render_template
from pyview.components import ComponentSocket, LiveComponent
from pyview.template.live_view_template import live_component

from tracks import Track, State


@dataclass
class TrackContext(TypedDict):
    track: Track


class TrackComponent(LiveComponent[TrackContext]):
    async def mount(self, socket: ComponentSocket[TrackContext], assigns: dict):
        socket.context = TrackContext(track=assigns.get("track"))

    async def handle_event(
        self, event: str, payload: dict, socket: ComponentSocket[TrackContext]
    ):
        """Handle component events"""
        if event == "update_state" and socket.context["track"].state != State.NEW:
            socket.context["track"].state = State(payload.get("new-state"))

    def template(self, socket: ComponentSocket[TrackContext], **kwargs):
        return render_template("components/track.html", track=socket.context["track"])


@dataclass
class TrackListContext(TypedDict):
    tracks: List[Track]


class TrackListComponent(LiveComponent[TrackListContext]):
    async def mount(self, socket: ComponentSocket[TrackListContext], assigns: dict):
        socket.context = TrackListContext(tracks=assigns.get("tracks"))

    def template(self, socket: ComponentSocket[TrackListContext], **kwargs):
        return render_template(
            "components/tracklist.html",
            tracks=socket.context["tracks"],
            live_component=live_component,
            component=TrackListComponent,
        )
