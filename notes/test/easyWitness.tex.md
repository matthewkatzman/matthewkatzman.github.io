# In Search of an Easy Witness: Exponential Time vs. Probabilistic Polynomial Time

## Russell Impagliazzo, Valentine Kabanets, Avi Wigderson

### Main Ideas

#### $\textbf{NEXP}\subset\textbf{P/poly}\Leftrightarrow\textbf{NEXP}=\textbf{MA}$

In other words, derandomization of $\textbf{MA}$ is equivalent to the existence of a hard function in $\textbf{NEXP}$.  The idea here is as follows:

($\Rightarrow$) If this is not true, then the Easy Witness Lemma does not hold.  Thus this direction is basically the proof of the Easy Witness Lemma.

($\Leftarrow$) This is a standard application of hard functions yielding derandomizations, but assuming $\textbf{NEXP}=\textbf{MA}=\textbf{EXP}$, significantly derandomizing $\textbf{MA}$ gives a faster deterministic simulation of $\textbf{EXP}$, contradicting the time hierarchy theorem.

#### Hardness vs Randomness

The $\Leftarrow$ direction of the above result is the contrapositive of a very standard idea - if $\textbf{NEXP}$ is hard then there is a way to derandomize $\textbf{MA}$ to some extent.

The other direction presents the new concept.  That is, this is the only way that $\textbf{MA}$ can be derandomized.  In other words, the existence of a hard function in $\textbf{NEXP}$ is *required*, otherwise $\textbf{MA}$ is just as hard as $\textbf{NEXP}$ and adding nondeterminism to $\textbf{BPP}$ or randomness to $\textbf{NP}$ (both) adds a huge amount of computational power.

#### The Easy Witness Lemma

The central idea of this technique is the ability to verify language membership from a heavily reduced search space.  The paper investigates the difference between the traditional concept of verifiers and verifiers for which certificates are the truth tables of functions with small circuits (in other words, verifiers with easy witnesses of membership).  The paper discusses the consequences of equality or inequality of these two notions.

A big takeaway from this paper is as follows: if $\textbf{NEXP}\subset\textbf{P/poly}$, then for every $L\in\textbf{NEXP}$ we can associate with any (correct) verifier a polynomial $p(n)$ such that for every $x\in L$ at least one accepted certificate can be compressed and represented as the truth table of circuit of size at most $p(n)$.  In other words, no matter the verifier, every $x\in L$ has an "easy witness" that $x$ is in $L$.

\[BFNW93\] tells us that if $\textbf{EXP}$ has small circuits (which it must if $\textbf{NEXP}$ has small circuits), then it collapses to $\textbf{MA}$.  From here, the basic idea is that, in the absence of easy witnesses, one can nondeterministically generate a hard function, which gives weak derandomization results for Arthur-Merlin.  This, in turn, gives slightly more efficient algorithms for $\textbf{EXP}$ with advice, which can be turned into fixed polynomial-sized circuits for $\textbf{EXP}$.  Quick diagonalization shows that such circuits do not exist, so the Easy Witness Lemma holds.

### Overview

#### The Main Result

**Theorem:** $\textbf{NEXP}\subset\textbf{P/poly}\Rightarrow\textbf{NEXP}=\textbf{MA}$.

**Lemma 1:** $\textbf{NEXP}\subset\textbf{P/poly}\Rightarrow\textbf{NEXP}=\textbf{EXP}$.

*Proof:* First we show ($\Rightarrow$).  Assume that 

(1) $\textbf{NEXP}\subset\textbf{P/poly}$.

and, for the sake of contradiction, assume that

(2) $\textbf{NEXP}\neq\textbf{EXP}$.

If $\textbf{NEXP}$ has easy witnesses (even considering circuits with oracle $\texttt{SAT}$ gates), then the witness search space is reduced to the point that one can iterate over and evaluate all candidate certificates in exponential time.  This would imply $\textbf{NEXP}=\textbf{EXP}$.  So by (2), there is a problem $L$ in $\text{NEXP}$ for which easy witnesses do not exist infinitely often.

Using this fact, we create the following $2^{O(n)}$-time Turing Machine $M$ given $n+1$ bits of advice.  On input lengths which do not have easy witnesses, there is at least one specific input $z\in L$ for which the certificate is hard.  Provide the string $1z$ as advice in this case.  For all other input lengths, provide $0^{n+1}$.  One can output $0^{2^n}$ and accept in this case.  Otherwise, on input of length $n$, nondeterministically guess a certificate showing $x\in L$ which, by assumption, does not have small circuits, and verify normally before providing the guessed certificate as output.  $M$ nondeterministically generates the truth table of an infinitely-often hard function for circuits with oracles for $\texttt{SAT}$.

Klivans and Melkebeek \[KM99\] showed that this ability to generate a *hard* function gives the weak *derandomization* result

(3) $\textbf{AM}\subseteq\textnormal{i.o.}-\textbf{NTIME}\left[2^{n^\epsilon}\right]/(n+1)^\epsilon$.

Now, Babai, Fortnow, Nisan, and Wigderson \[BFNW93\] show that, (1) gives us $\textbf{EXP}=\textbf{AM}=\textbf{MA}$, and combining this with (3) gives us 

(4) $\textbf{EXP}\subseteq\textnormal{i.o.}-\textbf{NTIME}\left[2^n\right]/(n+1)$.