from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button

class NestedScatterLayoutsApp(App):
    def build(self):
        outer_layout = ScatterLayout(do_scale=True, do_rotation=True, do_translation=True)
        
        inner_layout = ScatterLayout(size_hint=(None, None), size=(300, 300), do_scale=True, do_rotation=True, do_translation=True)
        
        button1 = Button(text='Outer Button', size_hint=(None, None), size=(200, 100))
        button2 = Button(text='Inner Button', size_hint=(None, None), size=(150, 100))
        
        inner_layout.add_widget(button2)
        outer_layout.add_widget(button1)
        outer_layout.add_widget(inner_layout)
        
        return outer_layout

if __name__ == '__main__':
    NestedScatterLayoutsApp().run()
