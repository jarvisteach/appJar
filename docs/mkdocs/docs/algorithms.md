#Algorithms  
----  
Below are some helpful comparisons between different ways of acheiving the same result, starting from design, move on to high-level language, into low-level language and finally machine code.  

This guide was originally intended to help with LMC implementation, but is also useful for general python deisgn/coding.  

##Comparison  
Topic | FlowChart | PseudoCode | Python | Assembler | Machine Code
- | - | - | - | - | -
Assigning a variable | ![Assignment](img/algorithms/1_a_eq_5.png) | a &#8592; 5 | a=5 | a DAT 5 | 
Input | ![Input](img/algorithms/2_a_eq_inp.png) | a &#8592; USERINPUT | a=input() | INP<br>STA a | 901<br>3xx
Output | ![Output](img/algorithms/3_prt_a.png) | a &#8592; 5 | a=5 | LDA a<br>OUT  | 5xx<br>902 
Subtraction | ![Subtraction](img/algorithms/5_a_eq_b_mi_c.png) | a &#8592; b - c | a=b-c | LDA b<br>SUB c<br>STA a | 5xx<br>2xx<br>3xx
Selection:<br>Greater than | ![Selection-GT](img/algorithms/6_a_gt_b.png) | IF a &gt; b THEN<br>&emsp;funcA()<br>ELSE<br>&emsp;funcB()<br>ENDIF | a &gt; b:<br>&emsp;funcA()<br>else:<br>&emsp;funcB() | LDA b<br>SUB a<br>BRP funcA<br>BRA funB | 5xx<br>2xx<br>8xx<br>6xx 
Selection:<br>Less than | ![Selection-LT](img/algorithms/7_a_lt_b.png) | IF a &lt; b THEN<br>&emsp;funcA()<br>ELSE<br>&emsp;funcB()<br>ENDIF | a &lt; b:<br>&emsp;funcA()<br>else:<br>&emsp;funcB() | LDA a<br>SUB b<br>BRP funcB<br>BRA funcA | 5xx<br>2xx<br>8xx<br>6xx
Selection:<br>Equal to | ![Selection-EQ](img/algorithms/8_a_eq_b.png) | IF a = b THEN<br>&emsp;funcA()<br>ELSE<br>&emsp;funcB()<br>ENDIF | if a == b:<br>&emsp;funcA()<br>else:<br>&emsp;funcB() | LDA a<br>SUB b<br>BRZ funcA<br>BRA funcB | 5xx<br>2xx<br>7xx<br>6xx
Selection:<br>Not equal to | ![Selection-NEQ](img/algorithms/9_a_ne_b.png) | IF a &#8800; b THEN<br>&emsp;funcA()<br>ELSE<br>&emsp;funcB()<br>ENDIF | if a &#8800; b:<br>&emsp;funcA()<br>else:<br>&emsp;funcB() | LDA a<br>SUB b<br>BRZ funcB<br>BRA funcA | 5xx<br>2xx<br>7xx<br>6xx
Iteration:<br>While loop | ![Iteration-WHILE](img/algorithms/10_while_a_ne_b.png) | WHILE a &#8800; b<br>&emsp;OUTPUT b<br>&emsp;a &#8592; USERINPUT<br>ENDWHILE | while a != b:<br>&emsp;print(b)<br>&emsp;a = input() | while LDA a<br>&emsp;&emsp;SUB b<br>&emsp;&emsp;BRZ endwhile<br>&emsp;&emsp;LDA b<br>&emsp;&emsp;OUT<br>&emsp;&emsp;INPU<br>&emsp;&emsp;STA a<br>&emsp;&emsp;BRA while<br>endwhile HLT<br>a DAT 0<br>b DAT 5| 5xx<br>2xx<br>7xx<br>5xx<br>902<br>901<br>3xx<br>6xx<br>000
Iteration:<br>For loop (count-up) | ![Iteration-FOR_UP](img/algorithms/11_for_up.png) | FOR i &#8592; 0 TO 9<br>&emsp;OUTPUT i<br>ENDFOR | for i in range(10):<br>&emsp;print(i) | for LDA i<br>&emsp;&emsp;OUT<br>&emsp;&emsp;ADD one<br>&emsp;&emsp;STA i<br>&emsp;&emsp;SUB ten<br>&emsp;&emsp;BRZ endfor<br>&emsp;&emsp;BRA for<br>endfor HLT<br>i DAT 0<br>one DAT 1<br>ten DAT 10 | 5xx<br>902<br>1xx<br>3xx<br>2xx<br>7xx<br>6xx<br>000
Iteration:<br>For loop (count-down) | ![Iteration-FOR_DOWN](img/algorithms/12_for_dn.png) | FOR 1 &#8592; 10 TO 1<br>&emsp;OUTPUT i<br>ENDFOR | for i in range(10, 0, -1):<br>&emsp;print(i) | for LDA i<br>&emsp;&emsp;OUT<br>&emsp;&emsp;SUB one<br>&emsp;&emsp;STA i<br>&emsp;&emsp;BRZ endfor<br>&emsp;&emsp;BRA for<br>endfor HLT<br>1 DAT 10<br>one DAT 1 | 5xx<br>902<br>2xx<br>3xx<br>7xx<br>6xx<br>000

##Links  
Some useful links for both LMC & Pseudocode.  

1. [Online LMC](http://www.gcsecomputing.org.uk/lmc/index.html)
2. [LMC Explanation](http://www.yorku.ca/sychen/research/LMC/)
3. [PseudoCode CheatSheet](/cheatSheets/PseudoCode%20CheatSheet.pdf)
4. [PseudoWars](http://pseudowar.appjar.info)
5. [AQA PseudoCode Guidelines](http://filestore.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF)

##LMC Instructions  
Simple explanations for the various LMC commands.  

Instructions | Mneumonic | Machine Code | Explanation
- | - | - | - 
Add | **ADD** | 1xx | Adds the contents of memory xx to the **ACCUMULATOR**.
Subtract | **SUB** | 2xx | Subtracts the contents of memory xx from the **ACCUMULATOR**.
Store | **STA** | 3xx | Copies the contents of the **ACCUMULATOR** to memory xx.
Load | **LDA** | 5xx | Copies the contents of memory xx to the **ACCUMULATOR**.
Branch ALWAYS | **BRA** | 6xx | Always set the program counter to xx. The program continues from the instruction at memory xx.
Branch if ZERO | **BRZ** | 7xx | Set the program counter to xx only of the **ACCUMULATOR** is zero.
Branch if POSITIVE | **BRP** | 8xx | Set the program counter to xx only if the **ACCUMULATOR** is zero or positive (greater than zero).
Input | **INP** | 901 | Copy the contents of the **INBOX** to the **ACCUMULATOR**.
Output | **OUT** | 902 | Copy the contents of the **ACCUMULATOR** to the **OUTBOX**.
Define Variable | **DAT** | | Reserves this memory slot as a variable, settinmg its contents to the value specified.
Halt | **HLT** | 000 | Halts execution of the program.
