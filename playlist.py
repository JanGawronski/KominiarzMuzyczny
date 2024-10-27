from random import shuffle
import config


class Playlist():
    
    def __init__(self):
        
        self.playlist = []
        self.history = []
        
        self.loop = False

    
    def __len__(self):
        return len(self.playlist)
    

    def add(self, song):

        self.playlist.append(song)
    

    def next(self):

        if self.loop == False:

            if len(self.history) >= config.MAX_HISTORY_LENGTH and config.MAX_HISTORY_LENGTH != -1:
                self.history.pop()

            self.history.insert(0, self.playlist[0])
            if len(self.playlist) > 2 and self.playlist[0] == self.playlist[2]:
                self.history.pop(0)
            self.playlist.pop(0)
        
        elif self.loop == "Skip, but still True":

            self.loop = True
            if len(self.history) >= config.MAX_HISTORY_LENGTH and config.MAX_HISTORY_LENGTH != -1:
                self.history.pop()

            self.history.insert(0, self.playlist[0])
            if len(self.playlist) > 2 and self.playlist[0] == self.playlist[2]:
                self.history.pop(0)
            self.playlist.pop(0)


    def previous(self):

        if len(self.playlist) == 0:
            self.playlist.append(self.history[0])
    
        else:
            self.playlist.insert(1, self.history[0])
            self.playlist.insert(2, self.playlist[0])
        
        self.history.pop(0)
        
    
    def toggleLoop(self):


        if self.loop == False:
            self.loop = True
        
        else:
            self.loop = False
    
    
    def shuffle(self):
        
        current = self.playlist[0]
        self.playlist.pop(0)
        shuffle(self.playlist)
        self.playlist.insert(0, current)


    def clear_queue(self):

        current = self.playlist[0]
        self.playlist = [current]
    

    def clear_history(self):
        
        self.history = []