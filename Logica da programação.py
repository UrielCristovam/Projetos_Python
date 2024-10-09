from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(text='Fala Galera',
            size_hint=(.5, .5), #O comando size_hint informa ao Kivy as proporções aserem usadas ao criar o widget
            pos_hint={'center_x': .5, 'center_y': .5}) #Para isso são necessários dois números:O primeiro número (x): refere-se à largura do controle.O segundo número (y): refere-se à altura do controle.

        return label
    
if __name__ == '__main__': 
    app = MainApp()
    app.run()