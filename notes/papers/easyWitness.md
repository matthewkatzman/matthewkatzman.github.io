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

#### The Main Result

**Theorem:** <img src="/notes/papers/tex/b560ff2705f21960f31f0200a056e607.svg?invert_in_darkmode&sanitize=true" align=middle width=268.58288655pt height=24.65753399999998pt/>

**Lemma 1:** <img src="/notes/papers/tex/7f79b4f287a32cefcea2d5bb0245b209.svg?invert_in_darkmode&sanitize=true" align=middle width=275.9800956pt height=24.65753399999998pt/>.

*Proof:* First we show (<img src="/notes/papers/tex/777d001ea1ec5971b67bb546ed760f97.svg?invert_in_darkmode&sanitize=true" align=middle width=16.43840384999999pt height=14.15524440000002pt/>).  Assume that 

(1) <img src="/notes/papers/tex/77fc0a70b06f5a122e80d7a9dd446aa7.svg?invert_in_darkmode&sanitize=true" align=middle width=134.69101634999998pt height=24.65753399999998pt/>.

and, for the sake of contradiction, assume that

(2) <img src="/notes/papers/tex/8de03f1ff93f09bbe377652be283542a.svg?invert_in_darkmode&sanitize=true" align=middle width=115.98105419999997pt height=22.831056599999986pt/>.

If <img src="/notes/papers/tex/3262497f78af8a499e76e85f7bdb9422.svg?invert_in_darkmode&sanitize=true" align=middle width=54.42894764999999pt height=22.55708729999998pt/> has easy witnesses (even considering circuits with oracle <img src="/notes/papers/tex/95d4aeb7638140fd70ba48c1d0a76c2d.svg?invert_in_darkmode&sanitize=true" align=middle width=25.890204449999988pt height=20.09134050000002pt/> gates), then the witness search space is reduced to the point that one can iterate over and evaluate all candidate certificates in exponential time.  This would imply <img src="/notes/papers/tex/d5b0955968ea3cad6274f10a34ac8d12.svg?invert_in_darkmode&sanitize=true" align=middle width=115.98105419999997pt height=22.55708729999998pt/>.  So by (2), there is a problem <img src="/notes/papers/tex/ddcb483302ed36a59286424aa5e0be17.svg?invert_in_darkmode&sanitize=true" align=middle width=11.18724254999999pt height=22.465723500000017pt/> in <img src="/notes/papers/tex/8d6516164fea0dbeb5f2d6a973eeefd9.svg?invert_in_darkmode&sanitize=true" align=middle width=47.032081799999986pt height=22.465723500000017pt/> for which easy witnesses do not exist infinitely often.

Using this fact, we create the following <img src="/notes/papers/tex/d68ffd33fdb660a33b5f4f61ed55160b.svg?invert_in_darkmode&sanitize=true" align=middle width=36.97176944999999pt height=29.190975000000005pt/>-time Turing Machine <img src="/notes/papers/tex/fb97d38bcc19230b0acd442e17db879c.svg?invert_in_darkmode&sanitize=true" align=middle width=17.73973739999999pt height=22.465723500000017pt/> given <img src="/notes/papers/tex/3f18d8f60c110e865571bba5ba67dcc6.svg?invert_in_darkmode&sanitize=true" align=middle width=38.17727759999999pt height=21.18721440000001pt/> bits of advice.  On input lengths which do not have easy witnesses, there is at least one specific input <img src="/notes/papers/tex/36e95cdc0bd5ff0a4db1e282cb0402b8.svg?invert_in_darkmode&sanitize=true" align=middle width=39.645998699999986pt height=22.465723500000017pt/> for which the certificate is hard.  Provide the string <img src="/notes/papers/tex/d0a62868544bbe8b43be9c0e7beb17cf.svg?invert_in_darkmode&sanitize=true" align=middle width=16.58683124999999pt height=21.18721440000001pt/> as advice in this case.  For all other input lengths, provide <img src="/notes/papers/tex/3de7c9704c3fdf394d3bbbd915894994.svg?invert_in_darkmode&sanitize=true" align=middle width=32.98915289999999pt height=26.76175259999998pt/>.  One can output <img src="/notes/papers/tex/5254e6ee076b978d5eb10b36ba83cffc.svg?invert_in_darkmode&sanitize=true" align=middle width=22.011217799999987pt height=28.92981300000002pt/> and accept in this case.  Otherwise, on input of length <img src="/notes/papers/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, nondeterministically guess a certificate showing <img src="/notes/papers/tex/60cd4b11237e4bc3ddd5d01c0853f07d.svg?invert_in_darkmode&sanitize=true" align=middle width=40.67336789999999pt height=22.465723500000017pt/> which, by assumption, does not have small circuits, and verify normally before providing the guessed certificate as output.  <img src="/notes/papers/tex/fb97d38bcc19230b0acd442e17db879c.svg?invert_in_darkmode&sanitize=true" align=middle width=17.73973739999999pt height=22.465723500000017pt/> nondeterministically generates the truth table of an infinitely-often hard function for circuits with oracles for <img src="/notes/papers/tex/95d4aeb7638140fd70ba48c1d0a76c2d.svg?invert_in_darkmode&sanitize=true" align=middle width=25.890204449999988pt height=20.09134050000002pt/>.

Klivans and Melkebeek \[KM99\] showed that this ability to generate a *hard* function gives the weak *derandomization* result

(3) <img src="/notes/papers/tex/4e86b8b0cd20852ec4ac817fc5b6f8c4.svg?invert_in_darkmode&sanitize=true" align=middle width=268.5137961pt height=28.92981300000002pt/>.

Now, Babai, Fortnow, Nisan, and Wigderson \[BFNW93\] show that, (1) gives us <img src="/notes/papers/tex/e9338db5ed13d5096e92191a285dca77.svg?invert_in_darkmode&sanitize=true" align=middle width=147.94430309999998pt height=22.55708729999998pt/>, and combining this with (3) gives us 

(4) <img src="/notes/papers/tex/be53750c133866a4de423fe99b05656c.svg?invert_in_darkmode&sanitize=true" align=middle width=270.43209105pt height=28.92981300000002pt/>.

