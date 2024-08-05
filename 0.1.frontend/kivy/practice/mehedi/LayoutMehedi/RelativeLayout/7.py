from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class NestedRelativeLayoutApp(App):
    def build(self):
        outer_layout = RelativeLayout()

        inner_layout = RelativeLayout(size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        btn1 = Button(text='Button 1', size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        btn2 = Button(text='Button 2', size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.3})

        inner_layout.add_widget(btn1)
        inner_layout.add_widget(btn2)

        outer_layout.add_widget(inner_layout)

        return outer_layout

if __name__ == '__main__':
    NestedRelativeLayoutApp().run()
