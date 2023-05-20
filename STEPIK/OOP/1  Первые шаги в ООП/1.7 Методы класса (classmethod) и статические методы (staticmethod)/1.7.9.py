class Video:
    def __init__(self):
        self.name = 'Default'

    def create(self, name):
        self.name = name

    def play(self):
        print(f'воспроизведение видео: {self.name}')


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video: Video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_index: int):
        cls.videos[video_index].play()


v1 = Video()
v2 = Video()
v3 = Video()

v1.create('Lol')
v2.create('Kek')
v3.create('Kek1')

YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.add_video(v3)
YouTube.play(2)
