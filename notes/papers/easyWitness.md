# In Search of an Easy Witness: Exponential Time vs. Probabilistic Polynomial Time

## Russell Impagliazzo, Valentine Kabanets, Avi Wigderson

### Main Ideas

#### <img src="/notes/papers/tex/b560ff2705f21960f31f0200a056e607.svg?invert_in_darkmode&sanitize=true" align=middle width=268.58288655pt height=24.65753399999998pt/>

In other words, derandomization of <img src="/notes/papers/tex/ba007d1b3734900f1caf239e9617b838.svg?invert_in_darkmode&sanitize=true" align=middle width=32.23728584999999pt height=22.55708729999998pt/> is equivalent to the existence of a hard function in <img src="/notes/papers/tex/3262497f78af8a499e76e85f7bdb9422.svg?invert_in_darkmode&sanitize=true" align=middle width=54.42894764999999pt height=22.55708729999998pt/>.  The idea here is as follows:

<img src="/notes/papers/tex/777d001ea1ec5971b67bb546ed760f97.svg?invert_in_darkmode&sanitize=true" align=middle width=16.43840384999999pt height=14.15524440000002pt/>

#### The Easy Witness Lemma

The central idea of this technique is the ability to verify language membership from a heavily reduced search space.  The paper investigates the difference between the traditional concept of verifiers and verifiers for which certificates are the truth tables of functions with small circuits (in other words, verifiers with easy witnesses of membership).  The paper discusses the consequences of equality or inequality of these two notions.

A big takeaway from this paper is as follows: if <img src="/notes/papers/tex/77fc0a70b06f5a122e80d7a9dd446aa7.svg?invert_in_darkmode&sanitize=true" align=middle width=134.69101634999998pt height=24.65753399999998pt/>, then for every <img src="/notes/papers/tex/192ad4ff2d53a3ec021edaa9374abad4.svg?invert_in_darkmode&sanitize=true" align=middle width=85.70732774999999pt height=22.55708729999998pt/> we can associate with any (correct) verifier a polynomial <img src="/notes/papers/tex/c62c4d1f4cea69da63734be038d89dea.svg?invert_in_darkmode&sanitize=true" align=middle width=30.92287604999999pt height=24.65753399999998pt/> such that for every <img src="/notes/papers/tex/60cd4b11237e4bc3ddd5d01c0853f07d.svg?invert_in_darkmode&sanitize=true" align=middle width=40.67336789999999pt height=22.465723500000017pt/> at least one accepted certificate can be compressed and represented as the truth table of circuit of size at most <img src="/notes/papers/tex/c62c4d1f4cea69da63734be038d89dea.svg?invert_in_darkmode&sanitize=true" align=middle width=30.92287604999999pt height=24.65753399999998pt/>.  In other words, no matter the verifier, every <img src="/notes/papers/tex/60cd4b11237e4bc3ddd5d01c0853f07d.svg?invert_in_darkmode&sanitize=true" align=middle width=40.67336789999999pt height=22.465723500000017pt/> has an "easy witness" that <img src="/notes/papers/tex/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/> is in <img src="/notes/papers/tex/ddcb483302ed36a59286424aa5e0be17.svg?invert_in_darkmode&sanitize=true" align=middle width=11.18724254999999pt height=22.465723500000017pt/>.

The basic idea is that 

### Overview

The main concept used here is the nondeterministic generation of hard functions.  
