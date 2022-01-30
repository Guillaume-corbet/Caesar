##
## EPITECH PROJECT, 2021
## caesar
## File description:
## Makefile
##

all:
	cp src/hex_to_base64.py challenge01
	cp src/fixed_xor.py challenge02
	cp src/single_byte_xor_cipher.py challenge03
	cp src/detect_single_byte_xor.py challenge04
	cp src/implement_repeating_key_xor.py challenge05
	cp src/break_repeating_key_xor.py challenge06
	cp src/error_handling.py challenge07
	cp src/error_handling.py challenge08
	cp src/error_handling.py challenge09
	cp src/error_handling.py challenge10
	cp src/error_handling.py challenge11
	cp src/error_handling.py challenge12
	cp src/error_handling.py challenge13
	cp src/error_handling.py challenge14
	chmod +x challenge01 challenge02 challenge03 challenge04 challenge05 challenge06 challenge07 challenge08 challenge09 challenge10 challenge11 challenge12 challenge13 challenge14


clean: fclean

fclean:
	rm challenge01
	rm challenge02
	rm challenge03
	rm challenge04
	rm challenge05
	rm challenge06
	rm challenge07
	rm challenge08
	rm challenge09
	rm challenge10
	rm challenge11
	rm challenge12
	rm challenge13
	rm challenge14

re: fclean all

.PHONY: all clean fclean re