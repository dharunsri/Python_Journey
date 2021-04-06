# break
# it just break a loop or a block
n = int(input("Enter value: "))
for i in range(1,n+1):
    if n>10:
        print("Range is high")
        break
    print(i)

# continue
# it just skip the corresponding condtion or block

for j in range(1,21):
    if j%3==0 or j%5==0:
        continue                 #it skips the number divisible by 3 and 5
    print(j)

# pass
# when block no need to be empty we will use pass. it just pass the block and do other works

for a in ['s','e','l','e','n','a']:
    if a== 'a' or 'e' or 'i' or 'o' or 'u':
        pass                                    # nothing it do just pass a block
    print(a)
