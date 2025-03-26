import torch
torch.manual_seed(12345)
B,T,C = 2,4,3
x = torch.randn(B,T,C)
value_shape = x.shape
print(value_shape)
print("original=",x)

print("Generating bag of words...")

x_bag_of_words = torch.zeros((B,T,C))
for b in range(B):
    for t in range(T):
        xprev = x[b,:t+1]
        x_bag_of_words[b,t] = torch.mean(xprev, 0)

print("x_bag_of_words=",x_bag_of_words)


from torch.nn import functional as F
tril = torch.tril(torch.ones(T, T))
weights = torch.zeros((T,T))
weights = weights.masked_fill(tril == 0, float('-inf'))
weights = F.softmax(weights, dim=-1)
x_bag_of_words_optimal = weights @ x
print("x_bag_of_words_optimal=",x_bag_of_words_optimal)