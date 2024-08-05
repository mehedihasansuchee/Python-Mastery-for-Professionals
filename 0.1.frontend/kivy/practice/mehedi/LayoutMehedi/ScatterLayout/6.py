from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class DynamicScatterLayoutApp(App):
    def build(self):
        self.layout = ScatterLayout(do_scale=True, do_rotation=True, do_translation=True)

        box_layout = BoxLayout(size_hint=(None, None), size=(200, 100))
        add_button = Button(text='Add', on_press=self.add_widget)
        remove_button = Button(text='Remove', on_press=self.remove_widget)
        box_layout.add_widget(add_button)
        box_layout.add_widget(remove_button)

        self.layout.add_widget(box_layout)
        return self.layout

    def add_widget(self, instance):
        new_button = Button(text='New Button', size_hint=(None, None), size=(150, 100))
        self.layout.add_widget(new_button)

    def remove_widget(self, instance):
        if len(self.layout.children) > 1:
            self.layout.remove_widget(self.layout.children[0])

if __name__ == '__main__':
    DynamicScatterLayoutApp().run()
