# Find the password that decodes the cipher and find the sum of the ASCII values in the decoded text
cipher = ""
for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            s = ""
            su = 0
            for i, v in enumerate(cipher):
                o = 0
                if i % 3 == 2: s += chr((o := v ^ a))
                if i % 3 == 1: s += chr((o := v ^ b))
                if i % 3 == 0: s += chr((o := v ^ c))
                su += o
                if s[-1] not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890[]()+:\";',./ ": 
                    su = -1
                    break
           if su != -1: print(su, s)
