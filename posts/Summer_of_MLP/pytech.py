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



