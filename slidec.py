from kivy.app import App
from kivy.core.audio import SoundLoader 


class SlideCApp(App):
	def build(self):
		self.load_sounds()
		

	def load_sounds(self):
		self.sounds = {}
		"""for i in range(4,8):
			filename = str(i+1) + '.wav'"""
			
		self.sounds = SoundLoader.load('5.wav')

	def play_sound(self):
		sound = self.sounds
		if sound is not None:
			sound.volume = 1
			sound.loop = True
			sound.play()

	def stop_sound(self):
		sound = self.sounds
		if sound is not None:
			if sound.state == "play":
				sound.stop()

    


if __name__ == '__main__':
    SlideCApp().run()