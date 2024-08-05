from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class OverlappingApp(App):
    def build(self):
        layout = RelativeLayout()

        btn1 = Button(text='Button A', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.3, 'center_y': 0.7})
        btn2 = Button(text='Button B', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn3 = Button(text='Button C', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.7, 'center_y': 0.3})

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

if __name__ == '__main__':
    OverlappingApp().run()
