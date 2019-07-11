from pynput.keyboard import Listener
from threading import Thread
from textblob import TextBlob
from textblob.exceptions import NotTranslated

from lib.replace_surroundings import replace_surroundings
from lib.char_mapper import CharMapper

import types


def log_output(output):
    print(output)


class KeySpy:
    def __init__(self, target_language, hook_function):
        self.target_language = target_language
        self.hook = self._validate_hook(hook_function)

        self._error_traces = list()
        self._output = str()
        self._input = str()
        self._setup_key_listener()
        self._mapper = CharMapper()

    @staticmethod
    def _validate_hook(hook_function):
        if isinstance(hook_function, types.FunctionType):
            return hook_function
        else:
            raise TypeError(f'Attempting to treat {type(hook_function)} as an Function.')

    def _translate(self):
        try:
            self._output = TextBlob(self._input).translate(to=self.target_language)
            self.hook(self._output)
        except NotTranslated as error:
            self._error_traces.append(str(error))

    def _on_key_pressed(self, key_pressed):
        converted_key = str(key_pressed)
        if converted_key not in self._mapper.excludes:
            if converted_key in self._mapper.includes:
                self._input = self._input + self._mapper.includes[converted_key]
            else:
                self._input = self._input + replace_surroundings("\x27", converted_key)
            self._translate()

    def _log_key_pressed(self):
        with Listener(on_press=self._on_key_pressed) as listener:
            listener.join()

    def _setup_key_listener(self):
        Thread(target=self._log_key_pressed).start()


if __name__ == "__main__":
    key_spy = KeySpy('pl', log_output)
