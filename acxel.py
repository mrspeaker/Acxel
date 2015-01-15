import sublime, sublime_plugin

class AcxelCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		sel = self.view.sel()

		if len(sel) > 1:
			lines = [self.view.substr(region) for region in sel]
		else:
			lines = [list(line) for line in self.view.substr(sel[0]).split("\n")]

		w = max([len(line) for line in lines])
		h = len(lines)

		makey = ""
		makey += "var can = document.createElement('canvas'), c = can.getContext('2d'),"
		makey += "data = c.createImageData(" + str(w) + ", " + str(h) + "), i = 0;"
		makey += "can.width = " + str(w) + "; can.height = " + str(h) + "; d = ["

		for line in lines:
			for i in range(w):
				char = " " if i >= len(line) else line[i]
				alpha = 0 if char.isspace() else 255
				makey += "0,0,0," + str(alpha) + ","

		makey = makey[:-1] + "]; "
		makey += "for (i = 0; i < d.length; i++) { data.data[i] = d[i]; }; "
		makey += "c.putImageData(data, 0, 0); "
		makey += "document.body.appendChild(c.canvas);"

		sublime.set_clipboard(makey)

# ********
# *      *
# ***  ***
#   *  *
#   *  *
#   ****
