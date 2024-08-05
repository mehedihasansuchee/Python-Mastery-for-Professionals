from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.image import Image

class ImageScatterLayoutApp(App):
    def build(self):
        layout = ScatterLayout(do_scale=True, do_rotation=True, do_translation=True)
        
        image = Image(source='kivy_logo.png', size_hint=(None, None), size=(300, 300))
        
        layout.add_widget(image)
        return layout

if __name__ == '__main__':
    ImageScatterLayoutApp().run()
