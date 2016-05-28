rm -f input.cd output.lpt

# wine autocoder.exe -bV -o input.cd helloworld.s
# Autocoder-Linux-2.3 -o input.cd helloworld.s
python fib.py
cp fib.cd input.cd

i1401 <<EOT
attach cdr input.cd
attach lpt output.lpt
boot cdr
EOT
echo
echo "    .    1    .    2    .    3    .    4    .    5    .    6    .    7    .    8"
cat output.lpt
wc -l output.lpt
