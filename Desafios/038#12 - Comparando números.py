n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro valor'))
if n1>n2:
    print('O \033[34mPRIMEIRO\033[37m valor é maior')
elif n2>n1:
    print('O \033[34mSEGUNDO\033[37m valor é maior')
elif n1==n2:
    print('Os dois valores são \033[34mIGUAIS\033[37m')
