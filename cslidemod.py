from kivy.app import App
from kivy.core.audio import Sound,SoundLoader 


class CSlideApp(App):
	def build(self):
		self.load_sound_list()
		

	def load_sound_list(self):
		self.sounds = []
		for i in range(3,6):
			fname = str(i+1) + '.wav'
			self.sounds.append(fname)
		

	def play_current(self):
		self.sound = SoundLoader.load(self.sounds[i])
		if self.sound is not None:
			self.sound.play()


	def play_next(self):
		if sound is None:
			self.sound = SoundLoader.load(self.sounds[i])
			self.sound.play()
		elif self.sound is not None:
			self.sound.unload()
			self.sound = SoundLoader.load(self.sounds[i+1])
			self.sound.play()
        	

	def play_prev(self):
		sound = SoundLoader.load(self.sounds[i-1])
		if sound is not None:
			sound.play()

	def stop_sound(self):
		sound = self.sounds[i]
		if sound is not None:
			if sound.state == "play":
				sound.stop()

    


if __name__ == '__main__':
	i = 1
	CSlideApp().run()