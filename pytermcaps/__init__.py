#
# Termcaps library
#

import os;
import sys;
import curses

class TermCapHolder(object):
    pass;

class TermCaps:
    """
    checks for termcaps and simplifies colored terminal interface.
    """
    
    _colors=["black","blue","green","cyan","red","magenta","yellow","white"];
    _acolors=["black","red","green","yellow","blue","magenta","cyan","white"];
    _capabilites=["bold","rev","smul","cuf1","clear","sgr0","el","ed","cuu1","cr"];
    
    _encoding = "utf-8";
    
    def __init__(self, **kw):
        self.haslogged = False;
        self.tc = True;
        self.stream = kw.pop("stream", sys.stdout);
        self.encoding = kw.pop("encoding", self._encoding);
        
        self.caps=None;
        self.setf=None;
        self.col = {};
        self.c = TermCapHolder();
        
        if not self.stream.isatty():
            self.blankcaps();
            self.tc = False;
            return
        
        try:
            curses.setupterm(os.environ.get("TERM", "xterm"), self.stream.fileno());
        except Exception, e:
            self.blankcaps();
            self.tc = False;
            # if caps for some reason are not possible. Set them to blanks.
            self._writeall("cannot get capabilities: " + str(e));
            return;
        
        for cap in self._capabilites:
            v = curses.tigetstr(cap);
            
            if not v:
                v = "";
            
            self.col[cap] = v;
            setattr(self.c, cap, v);
        
        self.setf=curses.tigetstr("setf");
        self.setaf=curses.tigetstr("setaf");
        
        colors = {};
        tf = None;
        
        if self.setf:
            tf = self.setf;
            colors = self._colors;
        elif self.setaf:
            tf = self.setaf;
            colors = self._acolors;
        
        for num, color in enumerate(colors):
            v = curses.tparm(tf, num);
            self.col[color] = v;
            setattr(self.c, color, v);
    
    def blankcaps(self):
        """
        Resets all capabilities to blanks.
        """
        for x in self._capabilites:
            self.col[x]="";
            setattr(self.c, x, "");
        
        for x in self._colors:
            self.col[x]="";
            setattr(self.c, x, "");
    
    def setstream(stream):
        """
        Change standard stream.
        """
        self.stream=stream;
    
    def _writeall(self, *args, **kw):
        """
        Write all arguments to stdout.
        """
        kw.get("stream", self.stream).write(''.join(args));
    
    def _encode(self, s):
        """
        Encode a string to the output encoding.
        """
        
        if isinstance(s, unicode):
            return s.encode(self.encoding);
        elif isinstance(s, basestring):
            return s;
        else:
            return str(s);
    
    def _encodeall(self, items):
        """
        Encode a sequence of strings to the output encoding.
        """
        
        return map(lambda s: self._encode(s), items);
    
    def _join(self, items, separator=' '):
        """
        Join and encode an array of strings with the default separator ' '
        """
        
        return separator.join(map(lambda s: self._encode(s), items));
