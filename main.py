from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.2, 1)


class SimpleRoshanApp(App):
    def build(self):
        self.title = "Roshan Simple App"
        layout = BoxLayout(orientation="vertical", padding=40, spacing=30)

        label = Label(
            text="اپلیکیشن سفارش بسته روشن\nبه نسخه آزمایشی خوش آمدید",
            font_size="22sp",
            halign="center",
            color=(1, 1, 1, 1),
        )
        button = Button(
            text="ثبت سفارش جدید",
            font_size="20sp",
            size_hint=(1, 0.3),
            background_color=(0.2, 0.7, 0.3, 1),
        )
        button.bind(on_press=self.on_button_click)

        layout.add_widget(label)
        layout.add_widget(button)
        return layout

    def on_button_click(self, instance):
        instance.text = "سفارش ثبت شد! ✅"
        instance.background_color = (0.7, 0.2, 0.2, 1)


if __name__ == "__main__":
    SimpleRoshanApp().run()