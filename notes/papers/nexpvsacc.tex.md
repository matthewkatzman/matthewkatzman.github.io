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

### Guess the circuits in $\textbf{ACC}$

This algorithm is correct, but what if $x\not\in\textbf{ACC}$?  What if $W_x\not\in\textbf{ACC}$?  An improved algorithm for $\texttt{ACC-SAT}$ only helps if we have an $\textbf{ACC}$ circuit to run it on.  There is still hope, however.  Because we are assuming throughout this process that $\textbf{NEXP}\subset\textbf{ACC}$, in particular we have $\textbf{P}\subset\textbf{ACC}$.  Consider the problem given inputs $C,y$ where $C$ encodes a circuit, is $C(y)=1$?  This problem is clearly in $\textbf{P}$, and thus in $\textbf{ACC}$.  So there is an $\textbf{ACC}$ taking input $(x,y)$ and outputting $(x,y)$ (resp. taking input $\left(W_x,y\right)$ and outputting $W_x(y)$), so fixing the input bits corresponding to $x$ (resp. $W_x$), this circuit is an $\textbf{ACC}$ circuit equivalent to $x$ (resp. $W_x$).  Of course, since this is a circuit family, we need to be able to generate these circuits at runtime.  So we just guess an $\textbf{ACC}$ easy witness $W_x'$ (this changes nothing) and an $\textbf{ACC}$ circuit $x'$ equivalent to $x$ (this will need to be verified somehow).  Then we construct $D$, which is now an $\textbf{ACC}$ circuit, run our $\texttt{ACC-SAT}$ algorithm on $\neg D$, and accept if the output is $0$.

### Guess and verify the circuits in $\textbf{ACC}$

