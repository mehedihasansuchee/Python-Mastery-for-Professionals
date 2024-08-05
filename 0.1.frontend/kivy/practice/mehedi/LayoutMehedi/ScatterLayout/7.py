from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TouchScatterLayoutApp(App):
    def build(self):
        layout = ScatterLayout(do_scale=True, do_rotation=True, do_translation=True)
        
        button = Button(text='Touch Me', size_hint=(None, None), size=(200, 100))
        button.bind(on_touch_down=self.on_touch_down)
        
        layout.add_widget(button)
        return layout

    def on_touch_down(self, instance, touch):
        if instance.collide_point(*touch.pos):
            instance.text = "Touched!"

if __name__ == '__main__':
    TouchScatterLayoutApp().run()
