from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MixedWidgetsApp(App):
    def build(self):
        layout = RelativeLayout()

        label = Label(text='Centered Label', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn1 = Button(text='Left Button', size_hint=(0.2, 0.2), pos_hint={'x': 0.1, 'center_y': 0.5})
        btn2 = Button(text='Right Button', size_hint=(0.2, 0.2), pos_hint={'right': 0.9, 'center_y': 0.5})

        layout.add_widget(label)
        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout

if __name__ == '__main__':
    MixedWidgetsApp().run()
