from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button

class GestureControlScatterLayoutApp(App):
    def build(self):
        layout = ScatterLayout(do_scale=True, do_rotation=False, do_translation=True)
        
        button = Button(text='No Rotation', size_hint=(None, None), size=(200, 100))
        
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    GestureControlScatterLayoutApp().run()
