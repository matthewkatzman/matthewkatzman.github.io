# $\textbf{NEXP}\not\subseteq\textbf{ACC}$ - Ryan Williams

## Main Ideas

This is one of the most successful results thus far derived from exploiting the connections between faster $\texttt{SAT}$ algorithms and stronger circuit lower bounds.  Using ideas similar to the [Karp-Lipton Theorems](https://matthewkatzman.github.io/notes/background/karpLipton.html), Williams shows that the existence of a $2^{n-\omega(\log n)}$ algorithm solving $\texttt{ACC-SAT}$ implies that $\textbf{NEXP}\not\subseteq\textbf{ACC}$.  In order to show this, he utilizes the nondeterministic time hierarchy theorem to show that the $\textbf{NEXP}$-complete problem $\texttt{SUCCINCT-3SAT}\not\in\textbf{NTIME}\left(2^{n-\omega(\log n)}\right)$ (this is the language comprised of circuits with truth tables encoding satisfiable $3$-CNFs).  Then, assuming that $\textbf{NEXP}\subset\textbf{ACC}$, he is able to construct a $O\left(2^{n-n^\epsilon}\right)$ algorithm for $\texttt{SUCCINCT-3SAT}$, contradicting the hierarchy and completing the proof.

This result is made up of two main parts:

1. Reducing solving $\texttt{SUCCINCT-3SAT}$ in $2^{n-\omega(\log n)}$ time to solving $\texttt{ACC-SAT}$ on circuits with $n$ inputs and $n^k$ size in $2^{n-\omega(\log n)}$ time.
2. Constructing an algorithm solving $\texttt{ACC-SAT}$ in $2^{n-\omega(\log n)}$ time.

## Reduction to $\textbf{ACC-SAT}$

### Guess a circuit to solve the problem

The basic idea is to nondeterministically guess a polynomial-sized circuit solving $\texttt{SUCCINCT-3SAT}$ and use the circuit to solve $\texttt{SUCCINCT-3SAT}$ on input circuit $x$ more efficiently.  It doesn't immediately help to guess a circuit for $\texttt{SUCCINCT-3SAT}$, as it would need to be verified, and an $\textbf{MIP}$ protocol does not help without access to randomness.

### Guess an easy witness circuit

Instead, Williams employs the [Easy Witness](https://matthewkatzman.github.io/notes/papers/easyWitness.html) technique to guess a circuit who's truth table encodes a satisfying assignment to the $3$-CNF $T(x)$.  It's still not clear, however, that this can be checked faster than exhasutively.

### Guess and verify the easy witness circuit

WLOG, we assume that $x(i)$ outputs the $i^\textnormal{th}$ clause of the $3$-CNF, and that our guessed witness circuit $W_x$ can encode the satisfying assignment on both the variables and their negations.  Then, feeding the three outputs of $x$ into distinct copies of $W_x$, we need at least one of these outputs to be $1$ for each clause, so we simply take an OR over these three copies to obtain a circuit $D$.  Note that $D$ is now the circuit that accepts if clause $i$ is satisfied by our guessed witness.  It is not enough for $D$ to be satisfiable, this tells us that a single clause of $T(x)$ is satisfied by our guess.  We need $\neg D$ to be unsatisfiable, in other words there is not a single clause that is not satisfied.  If this is the case we accept.

### Guess the witness circuits in $\textbf{ACC}$

This algorithm is correct, but what if $W_x\not\in\textbf{ACC}$?  An improved algorithm for $\texttt{ACC-SAT}$ only helps if we have an $\textbf{ACC}$ circuit to run it on.  There is still hope, however.  Because we are assuming throughout this process that $\textbf{NEXP}\subset\textbf{ACC}$, in particular we have $\textbf{P}\subset\textbf{ACC}$.  Consider the problem given inputs $C,y$ where $C$ encodes a circuit, is $C(y)=1$?  This problem is clearly in $\textbf{P}$, and thus in $\textbf{ACC}$.  So there is an $\textbf{ACC}$ taking input $\left(W_x,y\right)$ and outputting $W_x(y)$, so fixing the input bits corresponding to $W_x$, this circuit is an $\textbf{ACC}$ circuit equivalent to $W_x$.  Of course, since this is a circuit family, we need to be able to generate these circuits at runtime.  So we just guess an $\textbf{ACC}$ easy witness $W_x'$ instead.  Then we would like to construct $D$, run our $\texttt{ACC-SAT}$ algorithm on $\neg D$, and accept if the output is $0$.  But there's one more problem - we still don't know if $x\in\textbf{ACC}$, so $D$ is still not quite in $\textbf{ACC}$.

### Guess and verify an equivalent $\textbf{ACC}$ circuit

Modifying the above slightly, we can also decide the output of gate $j$ of circuit $x$ when run on input $i$ in polynomial time, so there is an $\textbf{ACC}$ circuit $C$ that does this on input $(x,i,j)$.  From the circuit $x$, given a gate $j$ we can determine its gate type (AND, OR, NOT, INPUT), and the two gates $j_1$ and $j_2$ that lead into it (WLOG we assume fan-in $2$).  Since this can be done in using a polynomially-sized CNF, there is an $\textbf{ACC}$ circuit $G_x$ that outputs $g,j_1,j_2$ on input $j$.  From here, we can run $C(x,i,\cdot)$ on $j$, $j_1$, and $j_2$.  These will output the values of $x$ at gates $j$, $j_1$, and $j_2$, and we can then verify with a constant-sized circuit $t$ that $g\left(C\left(x,i,j_1\right),C\left(x,i,j_2\right)\right)=C\left(x,i,j\right)$.  The circuit $t$ composed with three copies of $C$ composed with $G_x$ creates an $\textbf{ACC}$ circuit $E$ that, on input $(i,j)$, outputs $1$ if and only if $C$ is correct on input $i$ at gate $j$.  With a small additional check that $C$ correctly outputs the input gates, we create an $\textbf{ACC}$ circuit $E'$ such that $\neg E'$ is unsatisfiable if and only if $C$ is correct.  So, for our final algorithm, we have:

* Guess $\textbf{ACC}$ witness $W_x'$.
* Guess $\textbf{ACC}$ circuit $C$.
* Construct $\textbf{ACC}$ circuit $G_x$.
* Construct $\textbf{ACC}$ circuit $\neg E'$ using $C$ and $G_x$.
* If $\neg E'$ is satisfiable, *reject*.
* Fix inputs to create $\textbf{ACC}$ circuit $x'=\C\left(x,\cdot,j_s\right)$ with $j_s$ the output gate of $x$.
* Construct $\textbf{ACC}$ circuit $D$ using $x'$ and $W_x'$.
* *Accept* if and only if $\neg D$ is unsatisfiable.

So, since all of this can be constructed (or guessed) in polynomial time, if the $\texttt{ACC-SAT}$ algorithm runs in time $2^{n-\omega(\log n)}$, then so does the above nondeterministic algorithm solving $\texttt{SUCCINCT-3SAT}$.  This completes the proof that such an algorithm for $\texttt{ACC-SAT}$ gives $\textbf{NEXP}\not\subseteq\textbf{ACC}$.  All that remains is to show:

## $2^{n-\omega(\log n)}$ time algorithm for $\texttt{ACC-SAT}$
