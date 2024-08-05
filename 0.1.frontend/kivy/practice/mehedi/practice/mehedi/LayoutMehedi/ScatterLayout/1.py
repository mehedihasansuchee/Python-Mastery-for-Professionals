from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button

class BasicScatterLayoutApp(App):
    def build(self):
        layout = ScatterLayout(do_scale=True, do_rotation=True, do_translation=True)
        
        button = Button(text='Drag, Scale, Rotate Me', size_hint=(None, None), size=(200, 100))
        
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    BasicScatterLayoutApp().run()
