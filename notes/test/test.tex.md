# In Search of an Easy Witness: Exponential Time vs. Probabilistic Polynomial Time

## Russell Impagliazzo, Valentine Kabanets, Avi Wigderson

### Main Ideas

#### $\textbf{NEXP}\subset\textbf{P/poly}\Leftrightarrow\textbf{NEXP}=\textbf{MA}$

In other words, derandomization of $\textbf{MA}$ is equivalent to the existence of a hard function in $\textbf{NEXP}$.  The idea here is as follows:

($\Rightarrow$) If this is not true, then the Easy Witness Lemma does not hold.  Thus this direction is basically the proof of the Easy Witness Lemma.

($\Leftarrow$) This is a standard application of hard functions yielding derandomizations, but assuming $\textbf{NEXP}=\textbf{MA}=\textbf{EXP}$, significantly derandomizing $\textbf{MA}$ gives a faster deterministic simulation of $\textbf{EXP}$, contradicting the time hierarchy theorem.

#### Hardness vs Randomness

The $\Leftarrow$ direction of the above result is the contrapositive of a very standard idea - if $\textbf{NEXP}$ is hard then there is a way to derandomize $\textbf{MA}$ to some extent.

The other direction presents the new concept.  That is, this is the only way that $\textbf{MA}$ can be derandomized.  In other words, the existence of a hard function in $\textbf{NEXP}$ is *required*, otherwise $\textbf{MA} is just as hard as $\textbf{NEXP}$ and adding nondeterminism to $\textbf{BPP}$ or randomness to $\textbf{NP}$ (both) adds a huge amount of computational power.
