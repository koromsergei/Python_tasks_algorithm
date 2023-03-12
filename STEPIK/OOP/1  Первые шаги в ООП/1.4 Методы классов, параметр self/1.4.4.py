class MediaPlayer:
    def __init__(self):
        self.filename = None

    def open(self, file: str):
        self.filename = file

    def play(self):
        print(f"Воспроизведение{self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open('filemedia1')
media2.open('filemedia2')

media1.play()
media2.play()
