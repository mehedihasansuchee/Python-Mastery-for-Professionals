from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class RelativePositioningApp(App):
    def build(self):
        layout = RelativeLayout()

        btn1 = Button(text='Button 1', size_hint=(0.3, 0.3), pos_hint={'x': 0.1, 'y': 0.1})
        btn2 = Button(text='Button 2', size_hint=(0.3, 0.3), pos_hint={'x': 0.1, 'top': 0.9})
        btn3 = Button(text='Button 3', size_hint=(0.3, 0.3), pos_hint={'right': 0.9, 'y': 0.1})
        btn4 = Button(text='Button 4', size_hint=(0.3, 0.3), pos_hint={'right': 0.9, 'top': 0.9})

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout

if __name__ == '__main__':
    RelativePositioningApp().run()
