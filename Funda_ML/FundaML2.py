import numpy as np 

''' Lam viec voi ma tran '''

# 2.0 Mang nhieu chieu
''' Trong Numpy nguoi ta thuong dung mang numpy hai chieu de the hien mot ma tran. Mang
hai chieu co the coi la mot mang cua cac mang mot chieu. Ma tran co the duoc coi la mang
cua cac vector hang - moi vector hang duoc bieu dien bang mot mang numpy mot chieu
'''

''' Den doan xoan nao roi day, axis ?? '''

''' Vi du neu mot mang numpy hai chieu a mo ta ma tran 2 chieu, no se co dang [[1, 2], p3, 4]
. Mang [[1, 2], [3, 4]] co hai phan tu, moi phan tu la mot hang cua ma tran.
Theo quy uoc cua Numpy, chung ta can di tu cac mang ngoai cung roi cac mang trong:
    - Mang lon nhat la [[1, 2], [3, 4]] duoc coi la mang ung voi axiz = 0. Trong mang
    nay thanh phan thu nhat la [1, 2], thanh phan thu hai la [3, 4].
    - Hai mang lon thu hai la [1, 2] vaf [3, 4] duoc coi la cac mang ung voi axis = 1.
***CHU Y: 
        1. Mot mang numpy hoan toan co the co nhieu hon hai chieu. KHi do ta van du tu
        cap ngoac vuong ngoai cung vao toi trong cung, axis cung di tu 0, 1, ... theo thu
        tu do.
        2. Moi mang con phai co so phan tu bang nhau, the hien cho moi hang cua ma tran 
        phai co so chieu nhu nhau, khong co hang nao tho ra thut vao.
        3. Khi lam viec voi cac thu vien cho Machinel Learning, moi diem du lieu thuong
        duoc coi la mot mang mot chieu. Tap hop cac diem du lieu thuong duoc luu trong mot
        ma tran - tuc mang cua cac mang 1 chieu. Trong ma tran nay, moi hang tuong ung voi 
        mot diem du lieu.
    Viec nay hoi nguoc voi cach xay dung toan hoc cua cac thuat toan, noi ma moi diem du
    lieu thuong duoc coi la mot vector cot - tuc moi cot cua ma tran la mot diem du lieu
    . Khi doc cac tai lieu va lam viec voi cac thu vien, can chu y.
'''

#2.1    Khoi tao mot ma tran

A = np.array([[1, 2], [3, 4]])
print(A)
B = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float)
print(type(B[0][0]))

''' Exam 1 '''
C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(C)

#2.2    Ma tran don vi va ma tran duong cheo
#2.2.1  Ma tran don vi
''' Su dung ham np.eye() '''
print(np.eye(3))

''' Ham np.eye() cung duoc dung de tao cac ma tran toan 1 o mot duong cheo phu nao do
cac thanh phan con lai bang 0 
'''
print(np.eye(4, k = -1))

''' k = 1 se tuong ung voi duong cheo phu ngay tren duong cheo chinh, k = -1 tuong ung 
duong cheo phu ngay duoi duong cheo chinh
'''

#2.2.2  Ma tran duong cheo

''' De khai bao mot ma tran duong heo, hoac muon trich xuat duong cheo cua mot ma tran,
ta dung ham np.diag
'''
print(np.diag([1, 2, 5]))
a = np.diag(np.diag([1, 2, 5]))
print(a)

''' - Neu dau vao la mot mang mot chiue, tra ve mot mang hai chieu the hien ma tran co
    duong cheo la cac phan tu thuoc mang do.
    - Neu dau vao la mot mang hai chieu (co the khong vuong), tra ve mot mang mot chieu
    chua cac gia tri o hang thu i, cot thu i voi 0 <= i <= min(m, n).
    Duong chep phu cua mot ma tran cung cho the duoc lay boi ham nay bang cach chi ra 
    gia tri k
'''

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.diag(b, k=1))

#2.3    Kich thuoc cua ma tran
print(A.shape)
C = np.random.random((3, 2, 4))     # Create a random matrix 
print(C)
print(C.shape)

#2.4 Truy cap vao tung phan tu cua ma tran
#2.4.1.1 Cach 1: Giong nhu list

print(C[1][1][0])

#2.4.1.2 Cach 2: Giong nhu Matlab
print(C[1, 1, 0])

#2.4. 2 Truy cap vao hang/cot

''' De truy cap vao hangf co chi so i cua mot ma tran A, ta chi can dung A[i], hoac A[i, :] hoac A[i][:]
'''
print(A)
print(A[1])                         # Lay ra hang co chi so la 1
print(A[:, 1])                      # Lay ra cot co chi so la 1 
''' ***CHU Y: Trong Numpy, ket qua tra ve cua mot cot hay hang deu la mang mot chieu,
            khong phair laf mot vector cot nhu trong Matlab. Tuy nhien, khi lay mot ma tran
            nhan voi no, no van duojc coi la mot vector cot.
            Neu su dung A[:][1] thi van lay ra vector hang, chu khong phai la vector cot
            Co su khac biet can ban giua A va A[:], se duoc de cap sau.
'''

#2.5    Truy cap vao nhieu phan tu cua ma tran
#2.5.1  Nhieu phan tu cung 1 hang
print(B[0, 1:])
D = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(D)
print(D[1, np.arange(0, D.shape[1], 2)])

#2.5.2  Nhieu phan tu cung mot cot
print(D[np.arange(1, D.shape[0]), 1])   

#2.5.3 Nhieu hang, nhieu cot
print(D[1:3][:, [0,3]])
print(D[[1, 2]][:, [0, 3]])

#2.4.5 Cac cap toa do
''' Xet cau lenh duoi day '''
print(D[[1, 2], [0, 3]])
''' Cau lenh nay se tra ve mot mang mot chieu gom cac phan tu A[1][0] va A[2][3], tuc
[1, 2] va [0, 3] la list cac toa do theo moi chieu. Hai list nay phai co dp dai bang nhau
hoac 1 list co do dai bang 1. KHi mot list co do dai bang 1, no se duoc cap voi moi phan 
tu cua list con lai. Vi du: '''
print(D[[1, 2], [0]])