from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button

class RotationConstraintsScatterLayoutApp(App):
    def build(self):
        layout = ScatterLayout(do_scale=True, do_rotation=True, do_translation=True, rotation=45)
        
        button = Button(text='Rotated', size_hint=(None, None), size=(200, 100))
        
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    RotationConstraintsScatterLayoutApp().run()
