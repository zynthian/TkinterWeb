import sys

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk


DEFAULTSTYLE = """
/* Display types for non-table items. */
  ADDRESS, BLOCKQUOTE, BODY, DD, DIV, DL, DT, FIELDSET, 
  FRAME, H1, H2, H3, H4, H5, H6, NOFRAMES, 
  OL, P, UL, APPLET, CENTER, DIR, HR, MENU, PRE, FORM
                { display: block }

HEAD, SCRIPT, TITLE { display: none }
BODY {
  margin:8px;
}

/* Rules for unordered-lists */
LI                   { display: list-item }
UL[type="square"]>LI { list-style-type : square } 
UL[type="disc"]>LI   { list-style-type : disc   } 
UL[type="circle"]>LI { list-style-type : circle } 
LI[type="circle"]    { list-style-type : circle }
LI[type="square"]    { list-style-type : square }
LI[type="disc"]      { list-style-type : disc   }

OL, UL, DIR, MENU, DD  { padding-left: 40px ; margin-left: 1em }

OL[type]         { list-style-type : tcl(::tkhtml::ol_liststyletype) }

NOBR {
  white-space: nowrap;
}

/* Map the 'align' attribute to the 'float' property. Todo: This should
 * only be done for images, tables etc. "align" can mean different things
 * for different elements.
 */
TABLE[align="left"]       { float:left } 
TABLE[align="right"]      { 
    float:right; 
    text-align: inherit;
}
TABLE[align="center"]     { 
    margin-left:auto;
    margin-right:auto;
    text-align:inherit;
}
IMG[align="left"]         { float:left }
IMG[align="right"]        { float:right }

/* If the 'align' attribute was not mapped to float by the rules above, map
 * it to 'text-align'. The rules above take precedence because of their
 * higher specificity. 
 *
 * Also the <center> tag means to center align things.
 */
[align="right"]              { text-align: -tkhtml-right }
[align="left"]               { text-align: -tkhtml-left  }
CENTER, [align="center"]     { text-align: -tkhtml-center }

/* Rules for unordered-lists */
/* Todo! */

TD, TH {
  padding: 1px;
  border-bottom-color: grey60;
  border-right-color: grey60;
  border-top-color: grey25;
  border-left-color: grey25;
}

/* For a horizontal line, use a table with no content. We use a table
 * instead of a block because tables are laid out around floating boxes, 
 * whereas regular blocks are not.
 */
/*
HR { 
  display: table; 
  border-top: 1px solid grey45;
  background: grey80;
  height: 1px;
  width: 100%;
  text-align: center;
  margin: 0.5em 0;
}
*/

HR {
  display: block;
  border-top:    1px solid grey45;
  border-bottom: 1px solid grey80;
  margin: 0.5em auto 0.5em auto;
}

/* Basic table tag rules. */
TABLE { 
  display: table;
  border-spacing: 2px;

  border-bottom-color: grey25;
  border-right-color: grey25;
  border-top-color: grey60;
  border-left-color: grey60;

  /* <table> elements do not inherit text-align by default. Strictly
   * speaking, this rule should not be used with documents that
   * use the "strict" DTD. Or something.
   */
  text-align: left;
}

TR              { display: table-row }
THEAD           { display: table-header-group }
TBODY           { display: table-row-group }
TFOOT           { display: table-footer-group }
COL             { display: table-column }
COLGROUP        { display: table-column-group }
TD, TH          { display: table-cell }
CAPTION         { display: table-caption }
TH              { font-weight: bolder; text-align: center }
CAPTION         { text-align: center }

H1              { font-size: 2em; margin: .67em 0 }
H2              { font-size: 1.5em; margin: .83em 0 }
H3              { font-size: 1.17em; margin: 1em 0 }
H4, P,
BLOCKQUOTE, UL,
FIELDSET, 
OL, DL, DIR,
MENU            { margin-top: 1.0em; margin-bottom: 1.0em }
H5              { font-size: .83em; line-height: 1.17em; margin: 1.67em 0 }
H6              { font-size: .67em; margin: 2.33em 0 }
H1, H2, H3, H4,
H5, H6, B,
STRONG          { font-weight: bolder }
BLOCKQUOTE      { margin-left: 40px; margin-right: 40px }
I, CITE, EM,
VAR, ADDRESS    { font-style: italic }
PRE, TT, CODE,
KBD, SAMP       { font-family: courier }
BIG             { font-size: 1.17em }
SMALL, SUB, SUP { font-size: .83em }
SUB             { vertical-align: sub }
SUP             { vertical-align: super }
S, STRIKE, DEL  { text-decoration: line-through }
OL              { list-style-type: decimal }
OL UL, UL OL,
UL UL, OL OL    { margin-top: 0; margin-bottom: 0 }
U, INS          { text-decoration: underline }
ABBR, ACRONYM   { font-variant: small-caps; letter-spacing: 0.1em }

/* Formatting for <pre> etc. */
PRE, PLAINTEXT, XMP { 
  display: block;
  white-space: pre;
  margin: 1em 0;
  font-family: courier;
}

/* Display properties for hyperlinks */
:link    { color: darkblue; text-decoration: underline ; cursor: pointer }
:visited { color: purple; text-decoration: underline ; cursor: pointer }

/* Deal with the "nowrap" HTML attribute on table cells. */
TD[nowrap] ,     TH[nowrap]     { white-space: nowrap; }
TD[nowrap="0"] , TH[nowrap="0"] { white-space: normal; }

BR { 
    display: block;
}
/* BR:before       { content: "\A" } */

/*
 * Default decorations for form items. 
 */
INPUT[type="hidden"] { display: none }
INPUT[type] { border: none }
INPUT, INPUT[type="file"], INPUT[type="text"], INPUT[type="password"], 
TEXTAREA, SELECT { 
  border: 1px solid;
  border-color: #6eb9ff;
  background-color: white;
  line-height: normal;
}

INPUT[type="image"][src] { -tkhtml-replacement-image: attr(src) }

/*
 * Default style for buttons created using <input> elements.
 */
INPUT[type="submit"],INPUT[type="button"] {
  /*display: -tkhtml-inline-button;*/
  border: 0px solid;
  background-color: #d9d9d9;
  color: #000000;
  /* padding: 3px 10px 1px 10px; */
  padding: 0px;
  white-space: nowrap;
  color:               tcl(::tkhtml::if_disabled #666666 #000000);
}
INPUT[type="submit"]:after,INPUT[type="button"]:after {
  content: attr(value);
  position: relative;
}

INPUT[type="submit"]:hover:active,INPUT[type="button"]:hover:active {
  border-top-color:    tcl(::tkhtml::if_disabled #ffffff #828282);
  border-left-color:   tcl(::tkhtml::if_disabled #ffffff #828282);
  border-right-color:  tcl(::tkhtml::if_disabled #828282 #ffffff);
  border-bottom-color: tcl(::tkhtml::if_disabled #828282 #ffffff);
}

INPUT[size] { width: tcl(::tkhtml::inputsize_to_css) }

BUTTON {
  white-space:nowrap;
  border: 0px solid;
  background-color: #d9d9d9;
}

/* Handle "cols" and "rows" on a <textarea> element. By default, use
 * a fixed width font in <textarea> elements.
 */
TEXTAREA[cols] { width: tcl(::tkhtml::textarea_width) }
TEXTAREA[rows] { height: tcl(::tkhtml::textarea_height) }
TEXTAREA {
  font-family: fixed;
}

FRAMESET {
  display: none;
}

/* Default size for <IFRAME> elements */
IFRAME {
  width: 300px;
  height: 200px;
}


/*
 *************************************************************************
 * Below this point are stylesheet rules for mapping presentational 
 * attributes of Html to CSS property values. Strictly speaking, this 
 * shouldn't be specified here (in the UA stylesheet), but it doesn't matter
 * in practice. See CSS 2.1 spec for more details.
 */

/* 'color' */
[color]              { color: attr(color) }
body a[href]:link    { color: attr(link x body) }
body a[href]:visited { color: attr(vlink x body) }

/* 'width', 'height', 'background-color' and 'font-size' */
[width]            { width:            attr(width l) }
[height]           { height:           attr(height l) }
basefont[size]     { font-size:        attr(size) }
font[size]         { font-size:        tcl(::tkhtml::size_to_fontsize) }
[bgcolor]          { background-color: attr(bgcolor) }

BR[clear]          { clear: attr(clear) }
BR[clear="all"]    { clear: both; }

/* Standard html <img> tags - replace the node with the image at url $src */
IMG[src]              { -tkhtml-replacement-image: attr(src) }
IMG                   { -tkhtml-replacement-image: "" }

/*
 * Properties of table cells (th, td):
 *
 *     'border-width'
 *     'border-style'
 *     'padding'
 *     'border-spacing'
 */
TABLE[border], TABLE[border] TD, TABLE[border] TH {
    border-top-width:     attr(border l table);
    border-right-width:   attr(border l table);
    border-bottom-width:  attr(border l table);
    border-left-width:    attr(border l table);

    border-top-style:     attr(border x table solid);
    border-right-style:   attr(border x table solid);
    border-bottom-style:  attr(border x table solid);
    border-left-style:    attr(border x table solid);
}
TABLE[border=""], TABLE[border=""] td, TABLE[border=""] th {
    border-top-width:     attr(border x table solid);
    border-right-width:   attr(border x table solid);
    border-bottom-width:  attr(border x table solid);
    border-left-width:    attr(border x table solid);
}
TABLE[cellpadding] td, TABLE[cellpadding] th {
    padding-top:    attr(cellpadding l table);
    padding-right:  attr(cellpadding l table);
    padding-bottom: attr(cellpadding l table);
    padding-left:   attr(cellpadding l table);
}
TABLE[cellspacing], table[cellspacing] {
    border-spacing: attr(cellspacing l);
}

/* Map the valign attribute to the 'vertical-align' property for table 
 * cells. The default value is "middle", or use the actual value of 
 * valign if it is defined.
 */
TD,TH                        {vertical-align: middle}
TR[valign]>TD, TR[valign]>TH {vertical-align: attr(valign x tr)}
TR>TD[valign], TR>TH[valign] {vertical-align: attr(valign)}


/* Support the "text" attribute on the <body> tag */
body[text]       {color: attr(text)}

/* Allow background images to be specified using the "background" attribute.
 * According to HTML 4.01 this is only allowed for <body> elements, but
 * many websites use it arbitrarily.
 */
[background] { background-image: attr(background) }

/* The vspace and hspace attributes map to margins for elements of type
 * <IMG>, <OBJECT> and <APPLET> only. Note that this attribute is
 * deprecated in HTML 4.01.
 */
IMG[vspace], OBJECT[vspace], APPLET[vspace] {
    margin-top: attr(vspace l);
    margin-bottom: attr(vspace l);
}
IMG[hspace], OBJECT[hspace], APPLET[hspace] {
    margin-left: attr(hspace l);
    margin-right: attr(hspace l);
}

/* marginheight and marginwidth attributes on <BODY> */
BODY[marginheight] {
  margin-top: attr(marginheight l);
  margin-bottom: attr(marginheight l);
}
BODY[marginwidth] {
  margin-left: attr(marginwidth l);
  margin-right: attr(marginwidth l);
}

SPAN[spancontent]:after {
  content: attr(spancontent);
}

A:active {
    color:red;
    cursor:pointer;
}
"""


class _AutoScrollbar(ttk.Scrollbar):
    "Scrollbar that hides itself when not needed"
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        ttk.Scrollbar.set(self, lo, hi)
        
    def pack(self, **kw):
        raise tk.TclError("cannot use pack with this widget")
    
    def place(self, **kw):
        raise tk.TclError("cannot use place with this widget")


class _ScrolledText(tk.Frame):
    "Text widget with a scrollbar."
    def __init__(self, parent, **kwargs):

        tk.Frame.__init__(self, parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tbox = tbox = tk.Text(self, **kwargs)
        tbox.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        
        vsb = _AutoScrollbar(self, command=tbox.yview)
        vsb.grid(row=0, column=1, sticky='nsew')
        tbox['yscrollcommand'] = vsb.set

    def configure(self, *args, **kwargs):
        self.tbox.configure(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.tbox.get(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.tbox.delete(*args, **kwargs)


def notifier(main, sub, cap=True):
    "Notifications printer."
    try:
        sys.stderr.write(("UserNotification: "+str(main))+"\n")
        sub = str(sub)
        if cap:
            if len(sub) > 200:
                sub = sub[:200] + "..."
        sys.stdout.write(str(sub)+"\n\n")
    except Exception:
        "sys.stderr.write doesn't work in .pyw files."
        "Since .pyw files have no console, we can simply not bother printing messages."
