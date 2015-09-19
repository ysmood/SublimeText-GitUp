import sublime, sublime_plugin
import subprocess

settings = sublime.load_settings('gitup.sublime-settings')

class OpenGitupCommand(sublime_plugin.WindowCommand):
    def run(self):
        folder = self.window.extract_variables()['folder']
        path = settings.get('path', 'gitup')
        subprocess.Popen([path], cwd = folder)
        print("gitup opened")
