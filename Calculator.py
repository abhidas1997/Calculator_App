from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.widget import MDWidget
from kivymd.uix.button import MDRectangleFlatButton
from functools import partial
import re


class CalLayout(MDWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bxlayout = MDBoxLayout(orientation="vertical", size=(1, 1), padding=10, spacing=10,
                                    md_bg_color=(32 / 255, 148 / 255, 139 / 255))

        self.output_txt = MDTextField(text="0", readonly=True, mode="fill", multiline=False,
                                      size_hint_y=0.20, halign="right", font_size=43)
        self.equestion_text = MDTextField(text="", hint_text="History", multiline=False, readonly=True, mode="fill",
                                          size_hint=(1, 0.1),
                                          halign="right")

        self.gridlayout = MDGridLayout(cols=4, rows=5, spacing=10, size_hint_y=0.7)

        #### Row 1 ####
        self.btn1 = MDRectangleFlatButton(text="C", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                          size_hint=(1, 1), md_bg_color=(106 / 255, 177 / 255, 135 / 255),
                                          line_color=(0, 0, 0, 0), on_release=self.clear)
        self.btn2 = MDRectangleFlatButton(text="<<", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                          size_hint=(1, 1), md_bg_color=(106 / 255, 177 / 255, 135 / 255),
                                          line_color=(0, 0, 0, 0), on_release=self.clear_1)
        self.btn3 = MDRectangleFlatButton(text="%", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                          size_hint=(1, 1),
                                          md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                          on_release=partial(self.value_print, number="%"))
        self.btn4 = MDRectangleFlatButton(text="/", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                          size_hint=(1, 1),
                                          md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                          on_release=partial(self.value_print, number="/"))

        #### Row 2 ####
        self.btn5 = MDRectangleFlatButton(text="7", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                          size_hint=(1, 1),
                                          md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                          on_release=partial(self.value_print, number=7))
        self.btn6 = MDRectangleFlatButton(text="8", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                          size_hint=(1, 1),
                                          md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                          on_release=partial(self.value_print, number=8))
        self.btn7 = MDRectangleFlatButton(text="9", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                          size_hint=(1, 1),
                                          md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                          on_release=partial(self.value_print, number=9))
        self.btn8 = MDRectangleFlatButton(text="*", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                          size_hint=(1, 1),
                                          md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                          on_release=partial(self.value_print, number="*"))

        #### Row 3 ####
        self.btn9 = MDRectangleFlatButton(text="4", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                          size_hint=(1, 1),
                                          md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                          on_release=partial(self.value_print, number=4))
        self.btn10 = MDRectangleFlatButton(text="5", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                           size_hint=(1, 1),
                                           md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                           on_release=partial(self.value_print, number=5))
        self.btn11 = MDRectangleFlatButton(text="6", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                           size_hint=(1, 1),
                                           md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                           on_release=partial(self.value_print, number=6))
        self.btn12 = MDRectangleFlatButton(text="-", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                           size_hint=(1, 1),
                                           md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                           on_release=partial(self.value_print, number="-"))

        #### Row 4 ####
        self.btn13 = MDRectangleFlatButton(text="1", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                           size_hint=(1, 1),
                                           md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                           on_release=partial(self.value_print, number=1))
        self.btn14 = MDRectangleFlatButton(text="2", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                           size_hint=(1, 1),
                                           md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                           on_release=partial(self.value_print, number=2))
        self.btn15 = MDRectangleFlatButton(text="3", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                           size_hint=(1, 1),
                                           md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                           on_release=partial(self.value_print, number=3))
        self.btn16 = MDRectangleFlatButton(text="+", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                           size_hint=(1, 1),
                                           md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                           on_release=partial(self.value_print, number="+"))

        #### Row 5 ####
        self.btn17 = MDRectangleFlatButton(text="+/-", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                           size_hint=(1, 1), md_bg_color=(106 / 255, 177 / 255, 135 / 255),
                                           line_color=(0, 0, 0, 0), on_release=self.plus_minus)
        self.btn18 = MDRectangleFlatButton(text="0", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                           size_hint=(1, 1),
                                           md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                           on_release=partial(self.value_print, number=0))
        self.btn19 = MDRectangleFlatButton(text=".", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                           size_hint=(1, 1),
                                           md_bg_color=(106 / 255, 177 / 255, 135 / 255), line_color=(0, 0, 0, 0),
                                           on_release=partial(self.dots, sign="."))
        self.btn20 = MDRectangleFlatButton(text="=", font_size=32, text_color=(117 / 255, 76 / 255, 128 / 255),
                                           size_hint=(1, 1), md_bg_color=(106 / 255, 177 / 255, 135 / 255),
                                           line_color=(0, 0, 0, 0), on_release=self.calculation)

        #### Row 1 Add widget ####
        self.gridlayout.add_widget(self.btn1)
        self.gridlayout.add_widget(self.btn2)
        self.gridlayout.add_widget(self.btn3)
        self.gridlayout.add_widget(self.btn4)

        #### Row 2 Add widget ####
        self.gridlayout.add_widget(self.btn5)
        self.gridlayout.add_widget(self.btn6)
        self.gridlayout.add_widget(self.btn7)
        self.gridlayout.add_widget(self.btn8)

        #### Row 3 Add widget ####
        self.gridlayout.add_widget(self.btn9)
        self.gridlayout.add_widget(self.btn10)
        self.gridlayout.add_widget(self.btn11)
        self.gridlayout.add_widget(self.btn12)

        #### Row 4 Add widget ####
        self.gridlayout.add_widget(self.btn13)
        self.gridlayout.add_widget(self.btn14)
        self.gridlayout.add_widget(self.btn15)
        self.gridlayout.add_widget(self.btn16)

        #### Row 5 Add widget ####
        self.gridlayout.add_widget(self.btn17)
        self.gridlayout.add_widget(self.btn18)
        self.gridlayout.add_widget(self.btn19)
        self.gridlayout.add_widget(self.btn20)

        self.bxlayout.add_widget(self.equestion_text)
        self.bxlayout.add_widget(self.output_txt)
        self.bxlayout.add_widget(self.gridlayout)

    def clear(self, instance):
        self.output_txt.text = "0"
        self.equestion_text.text = ""

    def clear_1(self, instance):
        value = self.output_txt.text
        if value == "0" and len(value) == 1:
            self.output_txt.text = "0"
        elif value != "0" and len(value) == 1:
            self.output_txt.text = "0"
        else:
            self.output_txt.text = value[:-1]

    def value_print(self, instance, number):
        #prev_number = self.output_txt.text
        if self.output_txt.text == "0":
            self.output_txt.text = ""
            self.output_txt.text = f"{number}"

        elif self.output_txt.text == "Wrong Equation":
            self.output_txt.text = f"{number}"

        elif self.output_txt.text == "Invalid Place":
            self.output_txt.text = f"{number}"

        elif self.output_txt.text == "Invalid Number":
            self.output_txt.text = f"{number}"

        else:
            self.output_txt.text += f"{number}"

    def calculation(self, instance):
        prev = self.output_txt.text
        try:
            value = eval(str(self.output_txt.text))
            self.equestion_text.text = prev
            self.output_txt.text = str(value)
        except:
            self.equestion_text.text = prev
            self.output_txt.text = "Wrong Equation"

    def dots(self, instance, sign):
        prev_number = self.output_txt.text
        sign_list = re.split("\+|\-|\*|\/|\%", prev_number)
        if ((
                "+" in prev_number or "-" in prev_number or "*" in prev_number or "%" in prev_number or "/" in prev_number) and "." not in
                sign_list[-1]):
            prev_number = f"{prev_number}" + f"{sign}"
            self.output_txt.text = prev_number
        elif "." in prev_number:
            pass
        elif prev_number == "Wrong Equation":
            self.output_txt.text = "Invalid Place"
        else:
            prev_number = f"{prev_number}" + f"{sign}"
            self.output_txt.text = prev_number

    def plus_minus(self, instance):
        value = self.output_txt.text
        if value.startswith("-"):
            try:
                value = int(value)
                self.output_txt.text = str(abs(value))
            except:
                try:
                    value = float(value)
                    self.output_txt.text = str(abs(value))
                except:
                    self.output_txt.text = 'Invalid Number'
        else:
            try:
                value = int(value)
                self.output_txt.text = str(value * (-1))
            except:
                try:
                    value = float(value)
                    self.output_txt.text = str(value * (-1))
                except:
                    self.output_txt.text = 'Invalid Number'


class CalculatorAPP(MDApp):
    def build(self):
        return CalLayout().bxlayout


if __name__ == "__main__":
    CalculatorAPP().run()
