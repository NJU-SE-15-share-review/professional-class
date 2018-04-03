## author calabash_boy
nasm -f elf64 $1 -o temp.o
ld temp.o -o runable
rm temp.o
./runable
rm runable
