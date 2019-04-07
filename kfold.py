from sklearn.model_selection import KFold
cv = KFold(10000, shuffle=True)
print(cv)