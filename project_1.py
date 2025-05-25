

"""
project 1
input from user and display it
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class interface(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.btn = Button(text="click",size_hint=(0.2,0.1),font_size="18sp",
                     pos_hint={"center_x":0.5,"center_y":0.4})
        self.btn.bind(on_press = self.ret_inp)
        self.label = Label(text="Show your name ",font_size= "18sp" ,
                      pos_hint={"center_x":0.5,"center_y":0.3})
        self.txt = TextInput (hint_text = "Enter your name here: ",size_hint = (0.4,0.1),
                         pos_hint = {"center_x":0.5,"center_y":0.5},multiline =False,
                          background_color = (0.5,0.5,1,0.25),background_normal="",)
        self.txt.bind(on_text_validate=self.ret_inp)
        self.label2 = Label(text="",font_size= "18sp" ,
                      pos_hint={"center_x":0.5,"center_y":0.2})
        
        self.add_widget(self.btn)
        self.add_widget(self.label)
        self.add_widget(self.txt)
        self.add_widget(self.label2)
        

    def ret_inp(self,obj):
        ret = self.txt.text
        print(ret)


class Pro_jectApp(App):
    def build(self):
        return interface()        
    

Pro_jectApp().run()    


# same code with kivy lang

# from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput


# class Interface(FloatLayout):

#     def  ret_inp(self, obj):
#         data = self.ids.txt.text
#         print(data)  # ইউজারের লেখা টার্মিনালে প্রিন্ট হবে




# class Pro_jectApp(App):
#     def build(self):
#         return Interface()
    
# Pro_jectApp().run()    

