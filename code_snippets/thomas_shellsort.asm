; ******************************
;  Shell Sort algorithm

; Initialize staging variables
mov eax, 1            ; Set h = 1

; Find value of h
notLengthOne:
    cmp eax, dword[len]     ; Check if h < len
    jge isLengthOne         ; Jump if h >= len
    imul eax, eax, 3        ; h = h * 3
    inc eax                 ; h = (h * 3) + 1
    jmp notLengthOne        ; Loop back to check condition

isLengthOne:

; Shell Sort algorithm
outerLoop:
    cmp eax, 1              ; Check if h > 0
    jle endShellSort        ; Jump out of the loop if h <= 0
    dec eax                 ; Decrement h
    mov ebx, eax            ; Copy h to ebx (ebx will be our gap)
    shl ebx, 2              ; Multiply ebx by 4 (to use it as index offset)

    mov ecx, 0              ; Set i = 0

    ; Insertion sort with gap = h
    insertionSort:
        cmp ecx, dword[len]    ; Check if i < len
        jge nextOuterLoop      ; Jump out of the loop if i >= len
        
        mov edx, ecx            ; Copy i to edx
        mov edi, [lst + edx * 4]   ; Copy lst[i] to edi
        
        ; Shift elements with gap = h
        innerLoop:
            cmp edx, eax        ; Check if i >= h
            jl innerLoopEnd     ; Jump out of the loop if i < h
            
            sub edx, eax        ; edx = edx - h
            mov esi, [lst + edx * 4]   ; Copy lst[i - h] to esi
            cmp esi, edi        ; Compare lst[i - h] with lst[i]
            jle innerLoopEnd    ; Jump out of the loop if lst[i - h] <= lst[i]
            
            mov [lst + edx * 4 + ebx], esi ; Swap lst[i - h] and lst[i]
            jmp innerLoop       ; Continue inner loop
            
        innerLoopEnd:
            mov [lst + edx * 4 + ebx], edi ; Place lst[i] in its correct position
            inc ecx             ; Increment i
            jmp insertionSort   ; Continue insertion sort
            
    nextOuterLoop:
        jmp outerLoop       ; Continue with the next iteration of outer loop

endShellSort:

; Reset registers
xor rax, rax
xor rbx, rbx
xor rcx, rcx
xor rdx, rdx
xor rsi, rsi
xor rdi, rdi
