from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "-", "+"]
        #self.last_was_operator = None
        #self.last_button = None
        
        main_layout = BoxLayout(orientation="vertical")
        
        self.solution = TextInput(
            readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        
        return main_layout
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = instance
        self.last_was_operator = button_text in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception as e:
                self.solution.text = "Error"
        self.last_button = instance
        self.last_was_operator = False

if __name__ == "__main__":
    CalculatorApp().run()
