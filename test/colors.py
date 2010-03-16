from pytermcaps import TermCaps

class TestTermCaps(TermCaps):
    def prettyprint(self, *args):
        self._writeall(self.c.green, self.c.bold, self._join(args), self.c.sgr0, "\n");

tc = TestTermCaps();

tc.prettyprint("Google", "is", "your", "friend");
