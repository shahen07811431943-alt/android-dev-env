from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class DevApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.lbl = Label(text="بيئة التطوير تعمل!", font_size='22sp')
        btn = Button(text="اضغط هنا", size_hint=(1, 0.3))
        btn.bind(on_press=lambda x: setattr(self.lbl, 'text', 'تم ✅'))
        root.add_widget(self.lbl)
        root.add_widget(btn)
        return root

if __name__ == '__main__':
    DevApp().run()
