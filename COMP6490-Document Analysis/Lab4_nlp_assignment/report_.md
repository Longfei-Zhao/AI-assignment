# NLP Written Report
  
  
Longfei ZHao, u5976992
  
## Q2.
  
<img src="https://latex.codecogs.com/gif.latex?count(am)%20=%203"/>
<img src="https://latex.codecogs.com/gif.latex?count(am,%20Sam)%20=%202"/>
<img src="https://latex.codecogs.com/gif.latex?|&#x5C;{x:count(am,%20x)%20&gt;%200&#x5C;}|%20=%202"/>
Assume <img src="https://latex.codecogs.com/gif.latex?N(w_i)%20=%20|&#x5C;{x:count(x,%20w_i)%20&gt;%200&#x5C;}|"/> and <img src="https://latex.codecogs.com/gif.latex?d=%200.75"/>. Hence,
<img src="https://latex.codecogs.com/gif.latex?N("/>\<s><img src="https://latex.codecogs.com/gif.latex?)=0"/>
<img src="https://latex.codecogs.com/gif.latex?N("/>\</s><img src="https://latex.codecogs.com/gif.latex?)=2"/>
<img src="https://latex.codecogs.com/gif.latex?N(I)=2"/>
<img src="https://latex.codecogs.com/gif.latex?N(am)=1"/>
<img src="https://latex.codecogs.com/gif.latex?N(Sam)=3"/>
<img src="https://latex.codecogs.com/gif.latex?N(do)=1"/>
<img src="https://latex.codecogs.com/gif.latex?N(not)=1"/>
<img src="https://latex.codecogs.com/gif.latex?N(like)=1"/>
<img src="https://latex.codecogs.com/gif.latex?N(green)=1"/>
<img src="https://latex.codecogs.com/gif.latex?N(apples)=1"/>
<img src="https://latex.codecogs.com/gif.latex?N(and)=1"/>
<img src="https://latex.codecogs.com/gif.latex?&#x5C;Rightarrow&#x5C;sum_{w_i}%20N(w_i)=%2014"/>
<img src="https://latex.codecogs.com/gif.latex?&#x5C;Rightarrow&#x5C;lambda(am)%20=%20&#x5C;frac{d}{count(am)}|&#x5C;{x:count(am,%20x)%20&gt;%200&#x5C;}|%20=%20&#x5C;frac{0.75}{3}%20*%202%20=%200.5"/>
<img src="https://latex.codecogs.com/gif.latex?&#x5C;Rightarrow%20P_{kn}(Sam)%20=%20&#x5C;frac{N(Sam)}{&#x5C;sum_{w_i}%20N(w_i)}%20=%20&#x5C;frac{3}{14}"/>
<img src="https://latex.codecogs.com/gif.latex?&#x5C;Rightarrow%20P_{kn}(Sam%20|%20am)%20=%20&#x5C;frac{&#x5C;max(count(am,%20Sam)%20-%20d,%200)}{count(am)}%20+%20&#x5C;lambda(am)P_{kn}(Sam)=&#x5C;frac{1.25}{3}%20+%200.5%20*%20&#x5C;frac{3}{14}=0.5238"/>
## Q3. Context-Free Grammars
  
<img src="https://latex.codecogs.com/gif.latex?P&#x5C;!R&#x5C;!P&#x5C;$%20&#x5C;rightarrow%20%20my&#x5C;%20|&#x5C;%20his&#x5C;%20|&#x5C;%20her&#x5C;%20|&#x5C;%20its"/>
<img src="https://latex.codecogs.com/gif.latex?&#x5C;sout{P&#x5C;!N&#x5C;!P%20&#x5C;rightarrow%20nounEndWithS&#x27;}%20&#x5C;quad%20P&#x5C;!N&#x5C;!P%20&#x5C;rightarrow%20nounEndWithS&#x27;&#x5C;%20|&#x5C;%20%20nounEndWith&#x27;S"/>
<img src="https://latex.codecogs.com/gif.latex?Nominal%20&#x5C;rightarrow%20P&#x5C;!N&#x5C;!P"/>
<img src="https://latex.codecogs.com/gif.latex?&#x5C;sout{Det%20&#x5C;%20N&#x5C;!ominal%20&#x5C;rightarrow%20Det%20&#x5C;%20N&#x5C;!oun}%20&#x5C;quad%20N&#x5C;!ominal%20&#x5C;rightarrow%20Det%20&#x5C;%20N&#x5C;!ominal"/>
<img src="https://latex.codecogs.com/gif.latex?N&#x5C;!ominal%20&#x5C;rightarrow%20P&#x5C;!R&#x5C;!P&#x5C;$%20&#x5C;%20N&#x5C;!ominal"/>
<img src="https://latex.codecogs.com/gif.latex?N&#x5C;!ominal%20&#x5C;rightarrow%20N&#x5C;!ominal%20&#x5C;%20N&#x5C;!oun"/>
<img src="https://latex.codecogs.com/gif.latex?N&#x5C;!ominal%20&#x5C;rightarrow%20N&#x5C;!oun"/>
## Q4. Word Embeddings
  
We can consider an unseen word as it's subwords or character n-grams. We could train a ngram model which takes letters as tokens(Bojanowski, Grave, Joulin, & Mikolov, 2016). Therefore, we will get the frequence and word embeddings of all "syllables". Then, an unseen word can be splitted properly to a set of syllables. Hence, we use easily combine those syllables to get the word embedding.
## Q5. Transition-based Dependency Parsing
  
Assume <img src="https://latex.codecogs.com/gif.latex?&#x5C;langle%20v_i|S,%20v_j|I,%20A&#x5C;rangle"/>
The reason why <img src="https://latex.codecogs.com/gif.latex?Left&#x5C;text{-}Arc(LA)"/> needs to remove the topmost element from the stack is that avoid creating a cycle in the graph. For example, if we keep <img src="https://latex.codecogs.com/gif.latex?v_i"/> in <img src="https://latex.codecogs.com/gif.latex?S"/>, there is a chance that adding an arc <img src="https://latex.codecogs.com/gif.latex?v_i%20&#x5C;rightarrow%20v_j"/> to <img src="https://latex.codecogs.com/gif.latex?A"/> in the later operation. <img src="https://latex.codecogs.com/gif.latex?v_j%20&#x5C;rightarrow%20v_i"/> is alread in <img src="https://latex.codecogs.com/gif.latex?A"/>. Therefore, there is a cycle (Nivre, 2003).
The reason for <img src="https://latex.codecogs.com/gif.latex?Right&#x5C;text{-}Arc(RA)"/> is also to prevent to create a cycle. <img src="https://latex.codecogs.com/gif.latex?v_j"/> should be reduced before <img src="https://latex.codecogs.com/gif.latex?v_i"/>, otherwise arc linking these nodes might be added (Nivre, 2003).
The space complexity is also <img src="https://latex.codecogs.com/gif.latex?O(n)"/>, the reason is as follow. For <img src="https://latex.codecogs.com/gif.latex?Reduce(R)"/> and <img src="https://latex.codecogs.com/gif.latex?Shift(S)"/>, they won't increase the space. For <img src="https://latex.codecogs.com/gif.latex?LA"/> and <img src="https://latex.codecogs.com/gif.latex?RA"/>, the space will increase 1. It can be easily seen that <img src="https://latex.codecogs.com/gif.latex?T_{RA}%20+%20T_{S}%20=%20n,%20T_{LA}%20+%20T_{R}%20&#x5C;leq%20n"/> (<img src="https://latex.codecogs.com/gif.latex?T_i"/> means the time of <img src="https://latex.codecogs.com/gif.latex?i"/> operation). Hence, <img src="https://latex.codecogs.com/gif.latex?T_{RA}%20+%20T_{LA}%20&#x5C;leq%202n"/> and the initial data space complexity is <img src="https://latex.codecogs.com/gif.latex?O(n)"/>. As a result, the space complexity is <img src="https://latex.codecogs.com/gif.latex?O(n)"/>
### Reference
  
Bojanowski, P., Grave, E., Joulin, A., & Mikolov, T. (2016). Enriching word vectors with subword information. arXiv preprint arXiv:1607.04606.
Nivre, J. (2003). An efficient algorithm for projective dependency parsing. In Proceedings of the 8th International Workshop on Parsing Technologies (IWPT.
  