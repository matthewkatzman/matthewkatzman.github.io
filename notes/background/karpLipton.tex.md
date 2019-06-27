# Karp Lipton Theorems

## $\textbf{NP}\subset\textbf{P/poly}\Rightarrow\textbf{PH}=\boldsymbol{\Sigma_2^\textbf{P}}$

Proof: This is shown by proving $\boldsymbol{\Pi_2^\textbf{P}}=\boldsymbol{\Sigma_2^\textbf{P}}$, implying a collapse of the polynomial hierarchy to the second level.  Assume that $\textbf{NP}\subset\textbf{P/poly}$ and take some language $L\in\boldsymbol{\Pi_2^\textbf{P}}$.  There exists some polynomial-time relation $R$ such that $$x\in L\Leftrightarrow\forall^\textbf{P}y\exists^\textbf{P}zR(x,y,z)$$.
