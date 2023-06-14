from build.ChatApp import *
from build.command_parse import aide_en_ligne

aide_en_ligne()

root = tk.Tk()
app = ChatApp(root)
app.run()


