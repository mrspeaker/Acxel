import sublime, sublime_plugin

class AcxelCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		sel = self.view.sel()

		if len(sel) > 1:
			lines = [self.view.substr(region) for region in sel]
		else:
			lines = [list(line) for line in self.view.substr(sel[0]).split("\n")]

		# Duplicate the lines
		lines = [val for val in lines for _ in (0, 1)]

		w = max([len(line) for line in lines])
		h = len(lines)

		data = []

		for line in lines:
			for i in range(w):
				char = " " if i >= len(line) else line[i]
				alpha = 0 if char.isspace() else 255
				data.append(0)
				data.append(0)
				data.append(0)
				data.append(alpha)

		data = ",".join(str(d) for d in data)

		# Let's get all JavaScript-y!
		o = ""
		o += "var can = document.createElement('canvas'), c = can.getContext('2d'), "
		o += "data = c.createImageData(" + str(w) + ", " + str(h) + "), i = 0, d; "
		o += "can.width = " + str(w) + "; can.height = " + str(h) + "; "
		o += "d = [" + data + "];"
		o += "for (i = 0; i < d.length; i++) { data.data[i] = d[i]; }; "
		o += "c.putImageData(data, 0, 0); "
		o += "document.body.appendChild(c.canvas);"

		# to the clipboard!
		sublime.set_clipboard(o)
