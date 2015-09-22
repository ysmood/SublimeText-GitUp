import sublime, sublime_plugin
import subprocess

settings = sublime.load_settings('gitup.sublime-settings')
gitupPath = settings.get('path', '/usr/local/bin/gitup')

class OpenGitupCommand(sublime_plugin.WindowCommand):
    def run(self):
        global gitupPath
        try:
            path = self.window.extract_variables()['file_path']
        except:
            path = self.window.extract_variables()['folder']

        subprocess.Popen([gitupPath], cwd = path)
        print("gitup opened")
