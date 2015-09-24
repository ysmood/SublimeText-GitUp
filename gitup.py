import sublime, sublime_plugin
import subprocess


class OpenGitupCommand(sublime_plugin.WindowCommand):
    def __init__(self, arg):
        settings = sublime.load_settings('gitup.sublime-settings')
        self.gitupPath = settings.get('path', '/usr/local/bin/gitup')
        sublime_plugin.WindowCommand.__init__(self, arg)

    def run(self):
        try:
            path = self.window.extract_variables()['file_path']
        except:
            path = self.window.extract_variables()['folder']

        subprocess.Popen([self.gitupPath], cwd = path)
        print("gitup opened")
