import sublime, sublime_plugin
import subprocess

settings = sublime.load_settings('gitup.sublime-settings')
path = settings.get('path', '/usr/local/bin/gitup')
class OpenGitupCommand(sublime_plugin.WindowCommand):
    def run(self):
        global path
        folder = self.window.extract_variables()['folder']
        subprocess.Popen([path], cwd = folder)
        print("gitup opened")
