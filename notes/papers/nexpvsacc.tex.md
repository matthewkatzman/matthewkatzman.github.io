# $\textbf{NEXP}\not\subseteq\textbf{ACC}$ - Ryan Williams

## Main Ideas

This is one of the most successful results thus far derived from exploiting the connections between faster $\texttt{SAT}$ algorithms and stronger circuit lower bounds.  Using ideas similar to the [Karp-Lipton Theorems](https://matthewkatzman.github.io/notes/background/karpLipton.html), Williams shows that the existence of a $2^{n-\omega(\log n)} algorithm solving $\texttt{ACC-SAT}$ implies that $\textbf{NEXP}\not\subseteq\textbf{ACC}$.  In order to show this, he utilizes the nondeterministic time hierarchy theorem to show that the $\textbf{NEXP}-complete problem $\texttt{SUCCINCT-3SAT}\not\in\textbf{NTIME}\left(2^{n-\omega(\log n)}\right)$.  Then, assuming that $\textbf{NEXP}\subset\textbf{ACC}$, he is able to construct a $O\left(2^{n-n^\epsilon}\right)$ algorithm for \texttt{SUCCINCT-3SAT}, contradicting the hierarchy and completing the proof.

