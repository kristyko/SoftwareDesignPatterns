from __future__ import annotations
from abc import ABC


#  ===========states=============
class State(ABC):
    def play(self, player: MediaPlayer): pass

    def pause(self, player: MediaPlayer): pass

    def stop(self, player: MediaPlayer): pass

    def next(self, player: MediaPlayer):
        player.set_track_num(player.current_track_num + 1)
        player.set_state(Play())
        print("next song:", player.current_track)

    def prev(self, player: MediaPlayer):
        player.set_track_num(player.current_track_num - 1)
        player.set_state(Play())
        print("previous song:", player.current_track)


class Play(State):
    def pause(self, player: MediaPlayer):
        player.set_state(Pause())
        print("Play -> Pause:", player.current_track)

    def stop(self, player: MediaPlayer):
        player.set_state(Stop())
        player.set_track_num(0)
        print("Play -> Stop:", player.current_track)


class Pause(State):
    def play(self, player: MediaPlayer):
        player.set_state(Play())
        print("Pause -> Play:", player.current_track)

    def stop(self, player: MediaPlayer):
        player.set_state(Stop())
        player.set_track_num(0)
        print("Pause -> Stop:", player.current_track)


class Stop(State):
    def play(self, player: MediaPlayer):
        player.set_state(Play())
        print("Stop -> Play:", player.current_track)


#  ===========media player=============
class MediaPlayer:
    def __init__(self, tracks=None):
        if tracks is None:
            tracks = []
        self._tracks = tracks
        self._state: State = Stop()
        self._current_track_num = 0

    @property
    def current_track(self):
        return self._tracks[self._current_track_num]

    def set_track_num(self, track_num):
        n = len(self._tracks)
        if 0 <= track_num < n:
            self._current_track_num = track_num
        elif track_num == -1:
            self._current_track_num = n
        elif track_num == n:
            self._current_track_num = 0

    @property
    def current_track_num(self):
        return self._current_track_num

    @property
    def tracks(self):
        return self._tracks

    def add_track(self, track):
        self._tracks.append(track)

    @property
    def state(self):
        return self._state

    def set_state(self, state: State):
        self._state = state

    def play(self):
        self._state.play(self)

    def pause(self):
        self._state.pause(self)

    def next(self):
        self._state.next(self)

    def prev(self):
        self._state.prev(self)

    def stop(self):
        self._state.stop(self)


if __name__ == '__main__':
    mediaPlayer = MediaPlayer()

    mediaPlayer.add_track("track1")
    mediaPlayer.add_track("track2")
    mediaPlayer.add_track("track3")
    mediaPlayer.add_track("track4")
    mediaPlayer.add_track("track5")
    mediaPlayer.add_track("track6")

    mediaPlayer.play()
    mediaPlayer.pause()
    mediaPlayer.play()
    mediaPlayer.next()
    mediaPlayer.next()
    mediaPlayer.prev()
    mediaPlayer.stop()
    mediaPlayer.play()
    mediaPlayer.stop()
