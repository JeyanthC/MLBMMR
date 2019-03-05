from kivy.app import App
from kivy.core.audio import Sound,SoundLoader 


class CSlideApp(App):
	def build(self):
		self.load_sounds()
		

	def load_sounds(self):
		self.sounds = []
		for i in range(3,6):
			fname = str(i+1) + '.wav'
			self.sounds.append(fname)
		

	def play_current(self):
		sound = SoundLoader.load(self.sounds[i])
		if sound is not None:
			sound.play()


	def play_next(self):
		sound = SoundLoader.load(self.sounds[i+1])
		if sound is not None:
			sound.play()
        	

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