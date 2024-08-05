from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MultipleWidgetsScatterLayoutApp(App):
    def build(self):
        layout = ScatterLayout(do_scale=True, do_rotation=True, do_translation=True)
        
        button = Button(text='Button', size_hint=(None, None), size=(150, 100))
        label = Label(text='Label', size_hint=(None, None), size=(150, 100))
        
        layout.add_widget(button)
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    MultipleWidgetsScatterLayoutApp().run()
