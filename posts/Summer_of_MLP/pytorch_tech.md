### Leaf Tensors in Pytorch 


The `requires_grad` attribute does not  control whether the actual `grad` attribute of the tensor is populated or not.

This depends on the attribute `is_leaf`.

All tensors that have `requires_grad` set to false will be leaf tensors by convention.

> The rule is, if a tensor has been made by a user and has `requires_grad=True` during the initializaion, then it is a
> leaf tensor. If it has been operated on, then it loses it's `leaf` status. If the tensor has no gradient required,
> then by convention it is a leaf tensor. It is only a non leaf tensor, if it is a byproduct of an operation on leaf
> tensors.

The word `operation` in the above line is ambiguous.
`_requires_grad_()` and `detach()` aren't operations, they return new tensors each time you call them.



Try applying it here[^ans]

<pre class=code>
import torch

bio = []

bio.append(torch.randn(10, requires_grad=True).cuda())
bio.append(torch.randn(10, requires_grad=True))
bio.append(torch.randn(10).cuda())
bio.append(torch.randn(10) + 2)
bio.append(torch.randn(10))
bio.append(torch.randn(10).requires_grad_())
bio.append(torch.randn(10).requires_grad_().cuda())

state = [tensor.is_leaf for tensor in bio]

print(state)
</pre>


Will tensors created from Dataloaders and Datasets be leaf tensors or not?

> Yes, they don't store gradients usually.

Will the weights obtained from a pretrained model be leaf tensors or not?

> Yes, they are


[^ans]: False, True, True, True, True, True, False


## Transfer Learning with Pytorch

- [Resource](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
The blog asserts that the correct approch to doing this is not to use the `create_feature_extractor` function, but
instead just modify the final layer of the initialized `nn.Module`

- [Resource](https://pytorch.org/docs/master/notes/autograd.html)
This is a detailed document on autograd mechanics

