from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class RoshanApp(App):
    def build(self):
        self.title = "روشن / Roshan"
        layout = BoxLayout(orientation="vertical", padding=50, spacing=20)

        label = Label(
            text="اپلیکیشن سفارش بسته روشن\nآماده برای توسعه!",
            font_size="24sp",
            halign="center",
        )
        button = Button(
            text="دکمه تست",
            size_hint=(1, 0.3),
            background_color=(0.1, 0.7, 0.2, 1),
        )

        layout.add_widget(label)
        layout.add_widget(button)
        return layout


if __name__ == "__main__":
    RoshanApp().run()