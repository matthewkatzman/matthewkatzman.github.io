Return [Home](https://matthewkatzman.github.io/notes/notes.html)

# Karp Lipton Theorems

## $\textbf{NP}\subset\textbf{P/poly}\Rightarrow\textbf{PH}=\boldsymbol{\Sigma_2^\textbf{P}}$

Proof Sketch: This is shown by proving $\boldsymbol{\Pi_2^\textbf{P}}\subseteq\boldsymbol{\Sigma_2^\textbf{P}}$, implying a collapse of the polynomial hierarchy to the second level.  We take the statement "$x$ is in $L$ if and only if *for every* $y$ of polynomial length *there exists some* $z$ of polynomial length such that $(x,y,z)$ satisfies some polynomial relationship.  We want to use our assumptions and the properties of $\texttt{SAT}$ to turn that into the statement "$x$ is in $L$ if and only if *there exists some* circuit family $\left\{C_n\right\}$ that correctly calculates $\texttt{SAT}$ *on every* instance of length $n$ and accepts $x$.

*Proof:* Assume that $\textbf{NP}\subset\textbf{P/poly}$ and take some language $L\in\boldsymbol{\Pi_2^\textbf{P}}$.  There exists some polynomial-time relation $R$ such that

$x\in L\Leftrightarrow\forall^\textbf{P}y\exists^\textbf{P}zR(x,y,z)$.

Considering just the existential piece, we note that

$\exists^\textbf{P}zR(x,y,z)$ is just an instance of $\texttt{SAT}$.

Thus we can rewrite

$x\in L\Leftrightarrow\forall^\textbf{P}y\texttt{SAT}(f(x,y))$

where $f(x,y)$ is a boolean formula of polynomial-length.

Now, because $\textbf{NP}\subset\textbf{P/poly}$, we know that $\texttt{SAT}$ has polynomial-sized circuits.  Here we rely on the downward self-reducability of $\texttt{SAT}$.  Using the search-decision reduction, we can construct, from a circuit family $\left\{C_n\right\}$ computing $\texttt{SAT}$, a circuit family $\left\{C_n'\right\}$ computing satisfying assignments to $\texttt{SAT}$, which exists *if and only if* $f(x,y)$ was satisfiable, and can then be verified in polynomial time with verifier $V$.  So, since we require the existence of such a satisfying assignment for every $y$ (of bounded length), we see

$x\in L\Leftrightarrow\exists^\textbf{P}\left\{C_n'\right\}\_{n\leq|f(x,y)}\forall^\textbf{P}yV(C'(f(x,y)))=1$.

Thus $L\in\boldsymbol{\Sigma_2^\textbf{P}}$, so $\boldsymbol{\Pi_2^\textbf{P}}\subseteq\boldsymbol{\Sigma_2^\textbf{P}}$, and $\textbf{PH}=\boldsymbol{\Sigma_2^\textbf{P}}$ as we desired.

## $\textbf{PSPACE}\subset\textbf{P/poly}\Rightarrow\textbf{PSPACE}=\textbf{MA}$

## $\textbf{EXP}\subset\textbf{P/poly}\Rightarrow\textbf{EXP}=\boldsymbol{\Sigma_2^\textbf{P}}$

*Proof:* (For simplicity we assume a $1$-tape Turing Machine model).  Assume that $\textbf{EXP}\subset\textbf{P/poly}$, and take any language $L\in\textbf{EXP}$.  The aim is to show that $L\in\boldsymbol{\Sigma_2^\textbf{P}}$.  Because $L\in\textbf{EXP}$, there is an exponential-time Turing Machine $M$ that solves $L$ (say it runs in time $f(n)$).  The key insight is that, from $M$, we can create an exponential-time Turing Machine $M'$ that takes input $(x,i,t)$ and decides whether or not the $i^\textnormal{th}$ position of the configuration of $M$ at timestep $t$ is a $1$ ($M'$ can simply simulate $M$ for $t=2^{\textnormal{poly}(n)}$ timesteps).  So $M'$ solves a language $L'\in\textbf{EXP}$, and thus there is a circuit $C\in\textbf{P/poly}$ (by the initial assumption) that solves $L'$.

From here, the argument follows along the same lines as Cook-Levin.  Because computation is local, verifying correctness of $C(x,i,t)$ requires checking a constant number of other bits (it depends on the encoding, but one must check the the state, head location, and bits $i-1$, $i$, and $i+1$ at time $t-1$) to ensure that the circuit correctly encodes a given step of the computation of $M$.  Furthermore, if $t=f(|n|)$, then a verifier is also required to ensure that the state encoded is accepting.  Calling the verifier that carries out this computation $V$ (which we note runs in polynomial time in the size of $C$ (and encoding $i$ and $t$ in binary so that they are polynomial in length), we can say

$x\in L\Leftrightarrow\exists^\textbf{P} C\forall i,t\leq f(|x|)V(C,x,i,t)=1$.

Because all of these predicates are polynomial in length and $V$ runs in polynomial time, this gives us $\textbf{EXP}=\boldsymbol{\Sigma_2^\textbf{P}}$, so $\textbf{EXP}\subset\textbf{P/poly}\Rightarrow\textbf{EXP}=\boldsymbol{\Sigma_2^\textbf{P}}$ as we desired.
