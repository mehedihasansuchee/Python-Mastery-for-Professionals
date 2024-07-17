from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class RelativeLayoutApp(App):
    def build(self):
        layout = RelativeLayout()

        btn1 = Button(text='Button 1', size_hint=(0.2, 0.2), pos_hint={'x': 0.1, 'y': 0.5})
        btn2 = Button(text='Button 2', size_hint=(0.2, 0.2), pos_hint={'right': 0.9, 'top': 0.9})

        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout

if __name__ == '__main__':
    RelativeLayoutApp().run()
