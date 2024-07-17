from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button

class SizesPositionsScatterLayoutApp(App):
    def build(self):
        layout = ScatterLayout(do_scale=True, do_rotation=True, do_translation=True)
        
        btn1 = Button(text='Small Button', size_hint=(None, None), size=(100, 50), pos=(100, 200))
        btn2 = Button(text='Large Button', size_hint=(None, None), size=(300, 150), pos=(300, 400))
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout

if __name__ == '__main__':
    SizesPositionsScatterLayoutApp().run()
