; *****************************************************************
;  Name: Thomas Bryant
;  NSHE ID: 2000193948
;  Section: 1001
;  Assignment: 7
;  Description:	Sort a list of number using the shell sort
;		algorithm.  Also finds the minimum, median, 
;		maximum, and average of the list.

; -----
; Shell Sort

;	h = 1;
;       while ( (h*3+1) < a.length) {
;	    h = 3 * h + 1;
;	}

;       while( h > 0 ) {
;           for (i = h-1; i < a.length; i++) {
;               tmp = a[i];
;               j = i;
;               for( j = i; (j >= h) && (a[j-h] > B); j -= h) {
;                   a[j] = a[j-h];
;               }
;               a[j] = tmp;
;           }
;           h = h / 3;
;       }

; =====================================================================
;  Macro to convert integer to septenary value in ASCII format.
;  Reads <integer>, converts to ASCII/septenary string including
;	NULL into <string>

;  Note, the macro is calling using RSI, so the macro itself should
;	 NOT use the RSI register until is saved elsewhere.

;  Arguments:
;	%1 -> <integer>, value
;	%2 -> <string>, string address

;  Macro usgae
;	int2aSept	<integer-value>, <string-address>

;  Example usage:
;	int2aSept	dword [diamsArrays+rsi*4], tempString

;  For example, to get value into a local register:
;		mov	eax, %1

%macro	int2aSept	2

push rax
push rbx
push rcx
push rsi
push rdi
push r8

mov eax, %1								; 1st param into digit eval
mov ebx, 7								; int2sept
mov rcx, STR_LENGTH						; index address for array
mov rsi, FALSE							; symbol placement bool
mov rdi, STR_LENGTH						; for NULL char cmp
mov r8d, %1								; 1st param pos or neg chkr

dec rcx									; dec rcx to 11 to prevent oos
dec rdi									; dec rdi to 11 for NULL cmp

%%mGetSeptVal:							; index loop counter label
	cmp rcx, rdi						; checks if @ last index
	jne %%mNullChar						; cmp to add NULL char
		mov byte[%2+rcx], 0				; adds NULL char
		loop %%mGetSeptVal				; loops back to ctr label
	%%mNullChar:						; null char label
	cmp eax, 0							; checks of all digits done
	je %%mDiamSeptSum					; will jump after digits done
		cdq								; extends signed value
		idiv ebx						; divides by seven
		cmp edx, 0						; checks if edx is negative
		jge %%mRemPos					; if so, itll force abs value
			neg edx						; make neg edx into pos
		%%mRemPos:						; check for neg rem label
		add dl, 0x30					; adds in the 0 ASCII value
		mov byte[%2+rcx], dl			; moves ASCII char into array
		loop %%mGetSeptVal				; loops back for next eval
	%%mDiamSeptSum:						; digit eval cndtn label
	cmp rsi, TRUE						; checks if symbol was placed
	je %%mSymbolAdd						; skips if +/- already done
		cmp r8d, 0						; checks if param 1 pos/neg
		jl %%mIsMinus					; jumps if param 1 neg
			mov byte[%2+rcx], 0x2B		; adds a + to array
		%%mIsMinus:						; neg eval condition label
		cmp r8d, 0						; checks if param 1 pos/neg
		jge %%mIsPlus					; jumps if param 1 pos
			mov byte[%2+rcx], 0x2D		; adds a - to array
		%%mIsPlus:						; neg eval condition label
		mov rsi, TRUE					; sets symbool bool TRUE
		loop %%mGetSeptVal				; loops back for next eval
	%%mSymbolAdd:						; symbol condition label
	mov byte[%2+rcx], 0x20				; adding white spaces
	loop %%mGetSeptVal					; loops back until rcx is 0

mov byte[%2], 0x20						; adds the final space

push r8
push rdi
push rsi
push rcx
push rbx
push rax

%endmacro


; =====================================================================
;  Simple macro to display a string to the console.
;  Count characters (excluding NULL).
;  Display string starting at address <stringAddr>

;  Macro usage:
;	printString  <stringAddr>

;  Arguments:
;	%1 -> <stringAddr>, string address

%macro	printString	1
	push	rax							; save altered registers (cautionary)
	push	rdi
	push	rsi
	push	rdx
	push	rcx

	lea	rdi, [%1]						; get address
	mov	rdx, 0							; character count
%%countLoop:
	cmp	byte [rdi], NULL
	je	%%countLoopDone
	inc	rdi
	inc	rdx
	jmp	%%countLoop
%%countLoopDone:

	mov	rax, SYS_write					; system call for write (SYS_write)
	mov	rdi, STDOUT						; standard output
	lea	rsi, [%1]						; address of the string
	syscall								; call the kernel

	pop	rcx								; restore regs to original values
	pop	rdx
	pop	rsi
	pop	rdi
	pop	rax
%endmacro

; =====================================================================
;  Data Declarations.

section	.data

; -----
;  Define constants.

TRUE		equ	1
FALSE		equ	0

EXIT_SUCCESS	equ	0					; Successful operation

STDIN		equ	0						; standard input
STDOUT		equ	1						; standard output
STDERR		equ	2						; standard error

SYS_read	equ	0						; sys call code for read
SYS_write	equ	1						; sys call code for write
SYS_open	equ	2						; sys call code for file open
SYS_close	equ	3						; sys call code for file close
SYS_fork	equ	57						; sys call code for fork
SYS_exit	equ	60						; sys call code for terminate
SYS_creat	equ	85						; sys call code for file open/create
SYS_time	equ	201						; sys call code for get time

LF		equ	10
NULL	equ	0
ESC		equ	27

; -----
;  Provided data

lst	dd	1113, 1232, 2146, 1376, 5120, 2356,  164, 4565,  155, 3157
	dd	 759,  326,  171,  147, 5628, 7527, 7569,  177, 6785, 3514
	dd	1001,  128, 1133, 1105,  327,  101,  115, 1108,    1,  115
	dd	1227, 1226, 5129,  117,  107,  105,  109,  999,  150,  414
	dd	 107, 6103,  245, 6440, 1465, 2311,  254, 4528, 1913, 6722
	dd	1149,  126, 5671, 4647,  628,  327, 2390,  177, 8275,  614
	dd	3121,  415,  615,  122, 7217,    1,  410, 1129,  812, 2134
	dd	 221, 2234,  151,  432,  114, 1629,  114,  522, 2413,  131
	dd	5639,  126, 1162,  441,  127,  877,  199,  679, 1101, 3414
	dd	2101,  133, 1133, 2450,  532, 8619,  115, 1618, 9999,  115
	dd	 219, 3116,  612,  217,  127, 6787, 4569,  679,  675, 4314
	dd	1104,  825, 1184, 2143, 1176,  134, 4626,  100, 4566,  346
	dd	1214, 6786,  617,  183,  512, 7881, 8320, 3467,  559, 1190
	dd	 103,  112,    1, 2186,  191,   86,  134, 1125, 5675,  476
	dd	5527, 1344, 1130, 2172,  224, 7525,  100,    1,  100, 1134   
	dd	 181,  155, 1145,  132,  167,  185,  150,  149,  182,  434
	dd	 581,  625, 6315,    1,  617,  855, 6737,  129, 4512,    1
	dd	 177,  164,  160, 1172,  184,  175,  166, 6762,  158, 4572
	dd	6561,  283, 1133, 1150,  135, 5631, 8185,  178, 1197,  185
	dd	 649, 6366, 1162,  167,  167,  177,  169, 1177,  175, 1169

len	dd	200

min	dd	0
med	dd	0
max	dd	0
sum	dd	0
avg	dd	0


; -----
;  Misc. data definitions (if any).

h		dd	0
i		dd	0
j		dd	0
tmp		dd	0


; -----
;  Provided string definitions.

STR_LENGTH	equ	12						; chars in string, with NULL

newLine		db	LF, NULL

hdr		db	"---------------------------"
		db	"---------------------------"
		db	LF, ESC, "[1m", "CS 218 - Assignment #7", ESC, "[0m"
		db	LF, "Shell Sort", LF, LF, NULL

hdrMin		db	"Minimum:  ", NULL
hdrMed		db	"Median:   ", NULL
hdrMax		db	"Maximum:  ", NULL
hdrSum		db	"Sum:      ", NULL
hdrAve		db	"Average:  ", NULL

; ---------------------------------------------

section .bss

tmpString	resb	STR_LENGTH

; ---------------------------------------------

section	.text
global	_start
_start:

; ******************************
;  Shell Sort.
;  Find sum and compute the average.
;  Get/save min and max.
;  Find median.

;	YOUR CODE GOES HERE

; --------
; staging variables for first loop
mov dword[h], 1							; set h = 1
mov eax, dword[h]						; set eax to h
mov ebx, 3								; set ebx to 3 for dividing

; --------
; first loop to find value of h
notLengthOne:							; h < len loop label
imul ebx								; h = h * 3 for nxt cmp
inc eax									; h = (h * 3) + 1 nxt cmp
cmp eax, dword[len]						; checks if h < len
jge isLengthOne							; loops while h < len
	mov eax, dword[h]					; moves h back into eax
	imul ebx							; h = h * 3
	inc eax								; h = (h * 3) + 1
	mov dword[h], eax					; saves eax into h
	jmp notLengthOne					; looping back to h < len
isLengthOne:							; h < len end cndtn label

; --------
; triple loop shell sort. Kawabunga dude!
halfShell:								; outer while loop label
mov eax, dword[h]						; move var h into eax
cmp eax, NULL							; check if h > 0
jle turtlePower							; jump out of outer while
dec eax									; sets h - 1 for i
mov dword[i], eax						; makes i = h - 1
	outerShell:							; mid for loop label
	mov eax, dword[i]					; moves i into eax for cmp
	cmp eax, dword[len]					; checks if i < length
	jge endOuterShell					; end condition mid for
	mov esi, dword[i]					; sets index ptr esi = i
	mov eax, dword[lst+rsi*4]			; sets lst[i] into eax
	mov dword[tmp], eax					; tmp = lst[i]
	mov dword[j], esi					; j = i
		innerShell:						; inner for loop label
			mov esi, dword[j]			; set eax to j for cmp
			cmp esi, dword[h]			; check for j >= h
			jge innerConOne				; jump if j < h
				jmp endInnerShell		; for left && false
			innerConOne:				; && condition one label
			sub esi, dword[h]			; sets esi to j - h
			mov eax, dword[lst+rsi*4]	; sets eax to lst[j-h]
			cmp eax, dword[tmp]			; checks lst[j-h] > tmp
			jg innerConTwo				; jump if lst[j-h] <= tmp
				jmp endInnerShell		; for right && false
			innerConTwo:				; && condition two label
			mov edi, dword[j]			; sets edi to index j
			mov dword[lst+rdi*4], eax	; lst[j] = lst[j-h]
			sub edi, dword[h]			; get j - h
			mov dword[j], edi			; set j = j - h
			jmp innerShell				; looping back into inner for
		endInnerShell:					; inner for exit label
	mov esi, dword[j]					; set ptr to j
	mov eax, dword[tmp]					; set eax to lst[tmp]
	mov dword[lst+rsi*4], eax			; set lst[j] = lst[tmp]
	inc dword[i]						; i = i + 1
	jmp outerShell						; looping back into mid for
	endOuterShell:						; mid for exit label
mov eax, dword[h]						; moves h back into eax
mov ebx, 3								; moves 3 into ebx for div
cdq										; for signed division
idiv ebx								; sets h / 3 for h
mov dword[h], eax						; makes h = h / 3
jmp halfShell							; loops back into outer while
turtlePower:							; outer while end label

; --------
; reset used registers
mov rax, 0
mov rbx, 0
mov rsi, 0
mov rdi, 0

; --------
; finding minimum value
	mov ecx, dword[len]					; array size for loop
	sub ecx, 1							; to not move out of scope
	mov rsi, 1							; left ctr to move up list
	mov eax, dword[lst]					; moves first value into eax

findSmalls:								; find smallest val loop label
	cmp eax, dword[lst+rsi*4]			; cmp current small to nxt
	jl stillSmall						; jump if still small
		mov eax, dword[lst+rsi*4]		; make new small if no jump
	stillSmall:							; still small label
	inc rsi								; increasing ctr
	loop findSmalls						; loop repeat
mov dword[min], eax						; saves minimum value

; --------
; finding maximum value
	mov ecx, dword[len]					; list length for loop
	sub ecx, 1							; to not move out of scope
	mov rsi, 1							; left ctr to move up list
	mov eax, dword[lst]					; moves first value into eax

findBiggie:								; find largest val loop label
	cmp eax, dword[lst+rsi*4]			; cmp current largest to nxt
	jg stillBig							; jump if still big
		mov eax, dword[lst+rsi*4]		; make new big if no jump
	stillBig:							; still big label
	inc rsi								; increasing ctr
	loop findBiggie						; loop repeat
mov dword[max], eax						; saves maximum value

; --------
; getting array sum with a loop
mov ecx, dword[len]						; setting ecx loop ctr
sub ecx, 1								; so not to go out of scope
mov rsi, 1								; setting rsi next lst value
mov eax, dword[lst]						; adding first array value
sumLoop:								; loop Sum label
	add eax, dword[lst+rsi*4]			; adding next array value
	inc rsi								; moving rsi to next value
	loop sumLoop						; looping to sumLoop
mov dword[sum], eax						; saving sum to variable

; --------
; getting list average
mov eax, dword[sum]						; load array sum in eax
cdq										; sets eax to 64-bit register
idiv dword[len]							; dividing eax by array size
mov dword[avg], eax						; saves array average

; --------
; getting array median value
mov eax, dword[len]						; set to find middle value(s)
mov ebx, 2								; sets ebx to 2
cdq										; sets eax to 64-bit register
idiv ebx								; dividing by 2
dec eax									; offset by 1 to not go oos
mov r8d, eax							; moves (lwr)mid index to r9d
cmp edx, 0								; check for remainder
jne isOdd								; jump if lst idx is odd
mov r9d, eax							; set upper mid index to r9d
inc r9d									; inc r9d to upper mid index
mov eax, dword[lst+r8*4]				; adds upper mid array value
add eax, dword[lst+r9*4]				; adds upper mid array value
mov ebx, 2								; sets ebx to est size 4
cdq										; sets eax to 64-bit register
idiv ebx								; dividing eax by 4
mov dword[med], eax						; saves volumes est. median
jmp isEven								; jumps to end if even
isOdd:									; odd value label
mov eax, dword[lst+r8*4]				; adds middle array value
mov dword[med], eax						; saves volumes est. median
isEven:

; ******************************
;  Display results to screen in septenary.

	printString	hdr

	printString	hdrMin
	int2aSept	dword [min], tmpString
	printString	tmpString
	printString	newLine

	printString	hdrMed
	int2aSept	dword [med], tmpString
	printString	tmpString
	printString	newLine

	printString	hdrMax
	int2aSept	dword [max], tmpString
	printString	tmpString
	printString	newLine

	printString	hdrSum
	int2aSept	dword [sum], tmpString
	printString	tmpString
	printString	newLine

	printString	hdrAve
	int2aSept	dword [avg], tmpString
	printString	tmpString
	printString	newLine
	printString	newLine

; ******************************
;  Done, terminate program.

last:
	mov	rax, SYS_exit
	mov	rdi, EXIT_SUCCESS
	syscall

