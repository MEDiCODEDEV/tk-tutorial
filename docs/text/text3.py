"""Selecting text. Cut, Copy, Paste."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Cut, Copy and Paste", font="Arial 18")

        App.text = Text('Initial text...')
        App.text.config(undo=True)

        Button('Selection')
        Button('Edit Undo', 'App.text.edit_undo()')
        Button('Edit Redo', 'App.text.edit_redo()')
        Inspector(App.text, height=20)

if __name__ == '__main__':
    Demo().run()