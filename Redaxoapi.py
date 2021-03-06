# Original Version for CakePHP written by Jad Bitar (@jadb / www.jadbitar.com)
# ripped of by jdlx for Redaxo API Searches..

# available commands
#   redaxoapi_search_selection
#   redaxoapi_search_from_input

# changelog
# Jad Bitar - first implementation of search selection and search from input

# SETTINGS: Redaxo Version - currently available: "4.2.1" , "4.3.1" , "4.3.2" , "4.4.1", "5.x.x"
rex_version = '4.4.1'

import sublime
import sublime_plugin

import subprocess
import webbrowser


def SearchFor(text):
    url = 'http://docs.redaxo.com/en/' + rex_version + '/search.php?query=' + text.replace(' ', '%20')
    webbrowser.open_new_tab(url)


class RedaxoapiSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)

            SearchFor(text)


class RedaxoapiSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search Redaxo API for', '',
            self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
        SearchFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass
