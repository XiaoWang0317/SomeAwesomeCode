$$minJ(W, b, x)$$

$$s.t.||W||_1-C<=0$$

$$L(W, \lambda)=J(W)+\lambda(||W||_1-C)$$

$$\min_{W} \max_{\lambda}L(W, \lambda)$$

$$s.t. \lambda >= 0$$



$$s.t.||W||_2-C<=0$$

$$L(W, \lambda)=J(W)+\lambda(||W||_2-C)$$

$$\min_{W} \max_{\lambda}L(W, \lambda)$$

$$s.t. \lambda >= 0$$

$$L(W, \lambda)=J(W)+\lambda||W||_2-\lambda C$$

$$L'(W, \lambda)=L(W, \lambda)+\lambda C$$

$$=J(W)+\lambda||W||_2$$

$$\dfrac{dW}{dL(W, \lambda)}=\dfrac{dW}{dL'(W, \lambda)}$$

