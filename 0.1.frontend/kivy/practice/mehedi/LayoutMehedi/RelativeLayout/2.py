from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class OverlappingWidgetsApp(App):
    def build(self):
        layout = RelativeLayout()

        btn1 = Button(text='Button 1', size_hint=(0.3, 0.3), pos_hint={'x': 0.4, 'y': 0.4})
        btn2 = Button(text='Button 2', size_hint=(0.3, 0.3), pos_hint={'x': 0.5, 'y': 0.5})

        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout

if __name__ == '__main__':
    OverlappingWidgetsApp().run()
