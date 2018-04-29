global _start

section .text
_start:
mov word[l],0
mov word[r],0
mov word[now],0
mov eax,0

_loop1:
mov byte[ans1+eax],0
add eax,1
CMP eax,128
JL _loop1
mov eax,0
_loop2:
mov byte[ans2+eax],0
add eax,1
CMP eax,128
JL _loop2

mov byte[ans2],1

_read1:
mov eax,3
mov ebx,0
mov ecx,input
mov edx,1
int 80h
sub byte[input],30h
movzx ax,byte[input]
CMP ax,0
JL _read2
CMP ax,9
JG _read2
mov ax,word[l]
mov bl,10
mul bl
movzx bx,byte[input]
add ax,bx
mov word[l],ax
JMP _read1

_read2:
mov eax,3
mov ebx,0
mov ecx,input
mov edx,1
int 80h
sub byte[input],30h
movzx ax,byte[input]
CMP ax,0
JL _calc
CMP ax,9
JG _calc
mov ax,word[r]
mov bl,10
mul bl
movzx bx,byte[input]
add ax,bx
mov word[r],ax
JMP _read2

_calc:
add word[now],1
mov word[i],0
mov byte[carry],0
_loop3:
movzx edx,word[i]
movzx ax,byte[ans1+edx]
movzx bx,byte[ans2+edx]
add ax,bx
movzx bx,byte[carry]
mov byte[carry],0
add ax,bx
mov bl,0ah
div bl
CMP al,0
JE __else
mov byte[carry],1
__else:
movzx edx,word[i]
mov byte[tempans+edx],ah
add byte[i],1
mov ax,word[i]
CMP ax,128
JL _loop3

;1->2
mov ecx,0
_loop4:
mov al,byte[ans1+ecx]
mov byte[ans2+ecx],al
add ecx,1
CMP ecx,128
JL _loop4
;temp->1
mov ecx,0
_loop5:
mov al,byte[tempans+ecx]
mov byte[ans1+ecx],al
add ecx,1
CMP ecx,128
JL _loop5

;in_range?
mov ax,word[now]
mov bx,word[r]
CMP ax,bx
JG _exit
mov bx,word[l]
CMP ax,bx
JL _calc

;print
mov ax,word[now]
mov bl,4
div bl
CMP ah,0
JE _set0
CMP ah,1
JE _set1
CMP ah,2
JE _set2
CMP ah,3
JE _set3

_set0:
mov eax,4
mov ebx,1
mov ecx,color_red
mov edx,color_red.len
int 80h
JMP _print
_set1:
mov eax,4
mov ebx,1
mov ecx,color_blue
mov edx,color_blue.len
int 80h
JMP _print
_set2:
mov eax,4
mov ebx,1
mov ecx,color_yellow
mov edx,color_yellow.len
int 80h
JMP _print
_set3:
mov eax,4
mov ebx,1
mov ecx,color_green
mov edx,color_green.len
int 80h
JMP _print

_print:
mov eax,0
mov ebx,126
_loop6:
mov cl,byte[ans1+eax]
add cl,30h
mov byte[buffer+ebx],cl
add eax,1
sub ebx,1
CMP ebx,0
JNE _loop6
mov byte[buffer+127],10
mov byte[buffer+128],00h
mov edx,0
_loop7:
add edx,1
mov al,byte[buffer+edx]
CMP al,30h
JE _loop7
mov ebx,1
mov ecx,buffer
add ecx,edx
mov eax,128
sub eax,edx
mov edx,eax
mov eax,4
;mov edx,128
int 80h
JMP _calc
_exit:
mov eax,1
int 80h

section .bss
input: resb 1
l: resw 1
r: resw 1
ans1: resb 129
ans2: resb 129
tempans: resb 129
buffer: resb 129
now: resw 1
i: resw 1
carry: resb 1

section .data
color_red: db 1Bh, '[31;1m',0
.len equ $-color_red
color_blue: db 1Bh, '[34;1m',0
.len equ $-color_blue
color_green: db 1Bh,'[32;1m',0
.len equ $-color_green
color_yellow:db 1Bh,'[33;1m',0
.len equ $-color_yellow

