from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
Window.clearcolor = (0, 0,0,0)
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.lang import Builder


class Sound(SoundLoader):
	sound = SoundLoader.load('he cares.wav')
	sound.play()
	
class MenuScreen(Screen):
	pass
class PlayScreen(Screen):
	
	answer=StringProperty('A')
	response=StringProperty(' ')
	question=StringProperty('Who was the first king of \n Isreal')

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def another_question(self, widget):
		q1='Who is the Father of Jesus?'
		q1a='A. Jesus'
		q1b='B. God'
		q1c='C. Joseph'
		q1d ='D. Jacob'
		
		#changing background-color and the current question
		self.ids.question_label.text=q1
		self.ids.a.text=q1a
		self.ids.a.background_color=(0,0.3,0,1)
		self.ids.b.text=q1b
		self.ids.b.background_color=(0,0.3,0,1)
		self.ids.c.text=q1c
		self.ids.c.background_color=(0,0.3,0,1)
		self.ids.d.text=q1d
		self.ids.d.background_color=(0,0.3,0,1)
		
	def on_answer_button(self,widget):
		answer=widget.text[0]
		if(answer== 'D'):
			success = SoundLoader.load('success.wav')
			success.play()
			
			widget.background_color='blue'
	
			popup = Popup(title=' ',content=Label(text='Correct!'),size_hint=(None, None), size=(dp(150), dp(150)),auto_dismiss=True)
			
			popup.open()
		
			Clock.schedule_once(popup.dismiss,2)
			Clock.schedule_once(self.another_question, 2)
			
			
	
		else:
			failure= SoundLoader.load('failure.wav')
			failure.play()
			
			popup = Popup(title=' ',content=Label(text='Wrong!'),size_hint=(None, None), size=(dp(150), dp(150)),auto_dismiss=True)
			
			popup.open()
		
			Clock.schedule_once(popup.dismiss,2)
		
			Clock.schedule_once(self.another_question, 2)
			
			widget.background_color='red'
		
			
	
'''class Grid(GridLayout):
	pass
class Stack(StackLayout):
	textme=StringProperty('Okay')
	def on_button_press(self):
		self.textme='You got it'
		self.background_color='red'
		
class Anchor(AnchorLayout):
		pass		
		
class Box(BoxLayout):
	pass
	
class Page(PageLayout):
	pass
	
class Scroll(ScrollView):
	pass
	
class Page(PageLayout):
	pass'''
		
class MyApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MenuScreen(name='menu'))
		sm.add_widget(PlayScreen(name='play'))
		return sm
		


if __name__=='__main__':
	MyApp().run()

