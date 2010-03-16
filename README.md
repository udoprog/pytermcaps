A simple library which wraps terminal capabilities in an object-oriented fashion.

The following is an example of how it works:

    from pytermcaps import TermCaps

    class TestTermCaps(TermCaps):
        def prettyprint(self, *args):
            self._writeall(self.c.green, self.c.bold, self._join(args), self.c.sgr0, "\n");

    tc = TestTermCaps();
    
    tc.prettyprint("Google", "is", "your", "friend");
    # => would output: "Google is your friend" to stdout (by default) in green colors.

Terminal capabilities is nice, since it allows you to detect what the client can (or cannot) see.

If you for example pipe the output of a program to 'less' it will detect that stdout is not a tty, and therefore will not attempt to color the output.
