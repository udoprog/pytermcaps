from pytermcaps import TermCaps

class TestTermCaps(TermCaps):
    def prettyprint(*args):
        self._writeall(self.c.red, self.c.bold, self._join(args), self.c.sgr0);

tc = TestTermCaps();

tc.prettyprint("Google", "is", "your", "friend");
