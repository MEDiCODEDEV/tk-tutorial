from tklib import *
app = App('File browser')

class FileBrowser(Treeview):
    """Create a file browser."""
    def __init__(self, **kwargs):
        cwd = os.getcwd()
        Label('Directory: ' + cwd)
        super(FileBrowser, self).__init__(height=20, **kwargs)
        self.bind('<Return>', self.open_file)

        dir = os.listdir()
        for item in dir:
            size = os.stat(item).st_size
            id = self.insert('', 'end', text=item, values=(size))
            if os.path.isdir(item):
                sub = os.listdir(item)
                for item2 in sub:
                    size = os.stat(item+'/'+item2).st_size
                    self.insert(id, 'end', text=item2, values=(size))

        self['columns'] = ('size')
        self.column('size', width=100, anchor='e')
        self.heading('size', text='Size')

    def open_file(self, event=None):
        id = self.focus()
        item = self.item(id)['text']
        print('open file', id, item)
        f = open(item)
        s = f.read()
        App.text.delete('1.0', 'end')
        App.text.insert('1.0', s)

FileBrowser()
App.text = Text(height=28)
App.text.grid(row=1, column=1)
Combobox('wrap', 'char;word;none', 'App.text["wrap"]=self.var.get()')

app.run()