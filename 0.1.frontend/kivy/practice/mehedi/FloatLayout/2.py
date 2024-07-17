from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyFloatLayout(FloatLayout):
    pass

class MyApp(App):
    def build(self):
        layout = MyFloatLayout()

        # Add a button
        btn1 = Button(
            text='Button 1',
            size_hint=(.2, .1),
            pos_hint={'x': .1, 'y': .7}
        )
        layout.add_widget(btn1)

        # Add another button
        btn2 = Button(
            text='Button 2',
            size_hint=(.3, .1),
            pos_hint={'right': 1, 'y': .5}
        )
        layout.add_widget(btn2)

        # Add a label
        label = Label(
            text='Hello, FloatLayout!',
            size_hint=(.4, .2),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        layout.add_widget(label)

        # Add a text input
        textinput = TextInput(
            size_hint=(.5, .1),
            pos_hint={'x': .25, 'y': .1}
        )
        layout.add_widget(textinput)

        return layout

if __name__ == '__main__':
    MyApp().run()
