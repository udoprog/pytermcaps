# -*- encoding: utf-8 -*-

from pytermcaps import TermCaps

class TestTermCaps(TermCaps):
    def error(self, desc, *args):
        self._writeall(self.c.red, self.c.bold, self._encode(desc), self.c.sgr0, ": ", self.c.red, self._join(args), self.c.sgr0, "\n");

    def prettyprint(self, *args):
        self._writeall(self.c.green, self.c.bold, self._join(args), self.c.sgr0, "\n");

tc = TestTermCaps();


tc.prettyprint("Google", "is", "your", "friend");

errorstring="Api failure";
tc.error("An error occured", errorstring);
