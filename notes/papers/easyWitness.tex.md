# In Search of an Easy Witness: Exponential Time vs. Probabilistic Polynomial Time

## Russell Impagliazzo, Valentine Kabanets, Avi Wigderson

### Main Ideas

#### $\textbf{NEXP}\subset\textbf{P/poly}\Leftrightarrow\textbf{NEXP}=\textbf{MA}$

In other words, derandomization of $\textbf{MA}$ is equivalent to the existence of a hard function in $\textbf{NEXP}$.  The idea here is as follows:

$\Rightarrow$

#### The Easy Witness Lemma

The central idea of this technique is the ability to verify language membership from a heavily reduced search space.  The paper investigates the difference between the traditional concept of verifiers and verifiers for which certificates are the truth tables of functions with small circuits (in other words, verifiers with easy witnesses of membership).  The paper discusses the consequences of equality or inequality of these two notions.

A big takeaway from this paper is as follows: if $\textbf{NEXP}\subset\textbf{P/poly}$, then for every $L\in\textbf{NEXP}$ we can associate with any (correct) verifier a polynomial $p(n)$ such that for every $x\in L$ at least one accepted certificate can be compressed and represented as the truth table of circuit of size at most $p(n)$.  In other words, no matter the verifier, every $x\in L$ has an "easy witness" that $x$ is in $L$.

The basic idea is that 

### Overview

#### The Main Result

**Theorem:** $\textbf{NEXP}\subset\textbf{P/poly}\Leftrightarrow\textbf{NEXP}=\textbf{MA}$

*Proof:* First we show ($\Rightarrow$).  Assume that $\textbf{NEXP}\subset\textbf{P/poly}$.  We show:

(1) $\textbf{NEXP}=\textbf{EXP}$.

If $\textbf{NEXP}$ has easy witnesses (even considering circuits with oracle $\texttt{SAT}$ gates), then the witness search space is reduced to the point that one can iterate over and evaluate all candidate certificates in exponential time.  This would imply $\textbf{NEXP}=\textbf{EXP}$.  So assume, for the sake of contradiction, that $\textbf{NEXP}\neq\textbf{EXP}$.  Then there is a problem in $\text{NEXP}$ for which easy witnesses do not exist infinitely often.

Assume, for the sake of contradiction, that $\textbf{NEXP}\neq\textbf{EXP}$.  

The main concept used here is the nondeterministic generation of hard functions.  
