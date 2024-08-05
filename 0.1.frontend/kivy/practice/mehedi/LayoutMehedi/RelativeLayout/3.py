from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class AlignWidgetsApp(App):
    def build(self):
        layout = RelativeLayout()

        btn1 = Button(text='Top Left', size_hint=(0.2, 0.2), pos_hint={'x': 0, 'top': 1})
        btn2 = Button(text='Top Right', size_hint=(0.2, 0.2), pos_hint={'right': 1, 'top': 1})
        btn3 = Button(text='Bottom Left', size_hint=(0.2, 0.2), pos_hint={'x': 0, 'y': 0})
        btn4 = Button(text='Bottom Right', size_hint=(0.2, 0.2), pos_hint={'right': 1, 'y': 0})

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout

if __name__ == '__main__':
    AlignWidgetsApp().run()
