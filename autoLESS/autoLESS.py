from os.path import splitext, basename, dirname, join
import sublime, sublime_plugin


class AutoCompileCommand(sublime_plugin.EventListener):
    def on_post_save(self, view):
        
        print("Starting autoLESS...")
        
        if not view.file_name().endswith('.less'):
            return

        plugin_path = sublime.packages_path() + '\\autoLESS'
        args = plugin_path + '\\win\\dotless.exe'

        # execute our command
        view.window().run_command("exec", {"cmd": [args, view.file_name()]})
