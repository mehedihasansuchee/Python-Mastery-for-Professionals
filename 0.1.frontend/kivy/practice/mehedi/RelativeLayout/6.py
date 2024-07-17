from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class EdgesApp(App):
    def build(self):
        layout = RelativeLayout()

        btn1 = Button(text='Top Edge', size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'top': 1})
        btn2 = Button(text='Bottom Edge', size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0})
        btn3 = Button(text='Left Edge', size_hint=(0.2, 0.2), pos_hint={'x': 0, 'center_y': 0.5})
        btn4 = Button(text='Right Edge', size_hint=(0.2, 0.2), pos_hint={'right': 1, 'center_y': 0.5})

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout

if __name__ == '__main__':
    EdgesApp().run()
