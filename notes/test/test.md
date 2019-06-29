# In Search of an Easy Witness: Exponential Time vs. Probabilistic Polynomial Time

## Russell Impagliazzo, Valentine Kabanets, Avi Wigderson

### Main Ideas

#### <img src="/notes/test/tex/b560ff2705f21960f31f0200a056e607.svg?invert_in_darkmode&sanitize=true" align=middle width=268.58288655pt height=24.65753399999998pt/>

In other words, derandomization of <img src="/notes/test/tex/ba007d1b3734900f1caf239e9617b838.svg?invert_in_darkmode&sanitize=true" align=middle width=32.23728584999999pt height=22.55708729999998pt/> is equivalent to the existence of a hard function in <img src="/notes/test/tex/3262497f78af8a499e76e85f7bdb9422.svg?invert_in_darkmode&sanitize=true" align=middle width=54.42894764999999pt height=22.55708729999998pt/>.  The idea here is as follows:

(<img src="/notes/test/tex/777d001ea1ec5971b67bb546ed760f97.svg?invert_in_darkmode&sanitize=true" align=middle width=16.43840384999999pt height=14.15524440000002pt/>) If this is not true, then the Easy Witness Lemma does not hold.  Thus this direction is basically the proof of the Easy Witness Lemma.

(<img src="/notes/test/tex/bd9e3b94a2cd2f370d50ece113f7b316.svg?invert_in_darkmode&sanitize=true" align=middle width=16.43840384999999pt height=14.15524440000002pt/>) This is a standard application of hard functions yielding derandomizations, but assuming <img src="/notes/test/tex/525986dc5b84a8968c8c8655d1e89fb7.svg?invert_in_darkmode&sanitize=true" align=middle width=170.1359583pt height=22.55708729999998pt/>, significantly derandomizing <img src="/notes/test/tex/ba007d1b3734900f1caf239e9617b838.svg?invert_in_darkmode&sanitize=true" align=middle width=32.23728584999999pt height=22.55708729999998pt/> gives a faster deterministic simulation of <img src="/notes/test/tex/0fa7e1e4059a89859c4afd74d72979f5.svg?invert_in_darkmode&sanitize=true" align=middle width=39.634494899999986pt height=22.55708729999998pt/>, contradicting the time hierarchy theorem.

#### Hardness vs Randomness

The <img src="/notes/test/tex/bd9e3b94a2cd2f370d50ece113f7b316.svg?invert_in_darkmode&sanitize=true" align=middle width=16.43840384999999pt height=14.15524440000002pt/> direction of the above result is the contrapositive of a very standard idea - if <img src="/notes/test/tex/3262497f78af8a499e76e85f7bdb9422.svg?invert_in_darkmode&sanitize=true" align=middle width=54.42894764999999pt height=22.55708729999998pt/> is hard then there is a way to derandomize <img src="/notes/test/tex/ba007d1b3734900f1caf239e9617b838.svg?invert_in_darkmode&sanitize=true" align=middle width=32.23728584999999pt height=22.55708729999998pt/> to some extent.

The other direction presents the new concept.  That is, this is the only way that <img src="/notes/test/tex/ba007d1b3734900f1caf239e9617b838.svg?invert_in_darkmode&sanitize=true" align=middle width=32.23728584999999pt height=22.55708729999998pt/> can be derandomized.  In other words, the existence of a hard function in <img src="/notes/test/tex/3262497f78af8a499e76e85f7bdb9422.svg?invert_in_darkmode&sanitize=true" align=middle width=54.42894764999999pt height=22.55708729999998pt/> is *required*, otherwise <img src="/notes/test/tex/2a19b26ae3a3b9027ea964833b0bfb1f.svg?invert_in_darkmode&sanitize=true" align=middle width=143.74670144999996pt height=22.831056599999986pt/>\textbf{NEXP}<img src="/notes/test/tex/8827099d7a3e6e1631c53e92a0ffb0cc.svg?invert_in_darkmode&sanitize=true" align=middle width=213.91778924999994pt height=22.831056599999986pt/>\textbf{BPP}<img src="/notes/test/tex/9669642f91edfd5cb7d9480b22a155ca.svg?invert_in_darkmode&sanitize=true" align=middle width=120.06322844999998pt height=22.831056599999986pt/>\textbf{NP}$ (both) adds a huge amount of computational power.
