Return [Home](https://matthewkatzman.github.io/notes/notes.html)

# Karp Lipton Theorems

## $\textbf{NP}\subset\textbf{P/poly}\Rightarrow\textbf{PH}=\boldsymbol{\Sigma_2^\textbf{P}}$

Proof Sketch: This is shown by proving $\boldsymbol{\Pi_2^\textbf{P}}\subseteq\boldsymbol{\Sigma_2^\textbf{P}}$, implying a collapse of the polynomial hierarchy to the second level.  We take the statement "$x$ is in $L$ if and only if *for every* $y$ of polynomial length *there exists some* $z$ of polynomial length such that $(x,y,z)$ satisfies some polynomial relationship.  We want to use our assumptions and the properties of $\texttt{SAT}$ to turn that into the statement "$x$ is in $L$ if and only if *there exists some* circuit family $\left\{C_n\right\}$ that correctly calculates $\texttt{SAT}$ *on every* instance of length $n$ and accepts $x$.

Proof: Assume that $\textbf{NP}\subset\textbf{P/poly}$ and take some language $L\in\boldsymbol{\Pi_2^\textbf{P}}$.  There exists some polynomial-time relation $R$ such that

$x\in L\Leftrightarrow\forall^\textbf{P}y\exists^\textbf{P}zR(x,y,z)$.

Considering just the existential piece, we note that

$\exists^\textbf{P}zR(x,y,z)$ is just an instance of $\texttt{SAT}$.

Thus we can rewrite

$x\in L\Leftrightarrow\forall^\textbf{P}y\texttt{SAT}(f(x,y))$

where $f(x,y)$ is a boolean formula of polynomial-length.

Now, because $\textbf{NP}\subset\textbf{P/poly}$, we know that $\texttt{SAT}$ has polynomial-sized circuits.  Here we rely on the downward self-reducability of $\texttt{SAT}$.  Using the search-decision reduction, we can construct, from a circuit family $\left\{C_n\right\}$ computing $\texttt{SAT}$, a circuit family $\left\{C_n'\right\}$ computing satisfying assignments to $\texttt{SAT}$, which exists *if and only if* $f(x,y)$ was satisfiable, and can then be verified in polynomial time with verifier $V$.  So, since we require the existence of such a satisfying assignment for every $y$ (of bounded length), we see

$x\in L\Leftrightarrow\exists^\textbf{P}\left\{C_n'\right\}\_{n\leq|f(x,y)}\forall^\textbf{P}yV(C'(f(x,y)))=1$.

Thus $L\in\boldsymbol{\Sigma_2^\textbf{P}}$, so $\boldsymbol{\Pi_2^\textbf{P}}\subseteq\boldsymbol{\Sigma_2^\textbf{P}}$, and $\textbf{PH}=\boldsymbol{\Sigma_2^\textbf{P}}$ as we desired.
