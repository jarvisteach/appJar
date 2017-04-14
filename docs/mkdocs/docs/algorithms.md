#Algorithms  
----  
Below are some comparisons of how to achieve the same thing in a flowchart, pseudocode & Python.  

This site was originally written using AQA suggested pseudocode, but will be updated to include OCR recommendations.  
It will aso be extended, to include a lot more examples.  

##Comparison  
Topic | FlowChart | PseudoCode | Python |
- | - | - | - 
Assigning a variable | ![Assignment](img/algorithms/1_a_eq_5.png) | a &#8592; 5 | a = 5 |
Input | ![Input](img/algorithms/2_a_eq_inp.png) | a &#8592; USERINPUT | a = input() |
Output | ![Output](img/algorithms/3_prt_a.png) | OUTPUT a | print(a) |
Subtraction | ![Subtraction](img/algorithms/5_a_eq_b_mi_c.png) | a &#8592; b - c | a = b - c |
Selection:<br>Greater than | ![Selection-GT](img/algorithms/6_a_gt_b.png) | IF a &gt; b THEN<br>&emsp;funcA()<br>ELSE<br>&emsp;funcB()<br>ENDIF | if a &gt; b:<br>&emsp;funcA()<br>else:<br>&emsp;funcB() |
Selection:<br>Less than | ![Selection-LT](img/algorithms/7_a_lt_b.png) | IF a &lt; b THEN<br>&emsp;funcA()<br>ELSE<br>&emsp;funcB()<br>ENDIF | if a &lt; b:<br>&emsp;funcA()<br>else:<br>&emsp;funcB() |
Selection:<br>Equal to | ![Selection-EQ](img/algorithms/8_a_eq_b.png) | IF a = b THEN<br>&emsp;funcA()<br>ELSE<br>&emsp;funcB()<br>ENDIF | if a == b:<br>&emsp;funcA()<br>else:<br>&emsp;funcB() |
Selection:<br>Not equal to | ![Selection-NEQ](img/algorithms/9_a_ne_b.png) | IF a &#8800; b THEN<br>&emsp;funcA()<br>ELSE<br>&emsp;funcB()<br>ENDIF | if a != b:<br>&emsp;funcA()<br>else:<br>&emsp;funcB() |
Iteration:<br>While loop | ![Iteration-WHILE](img/algorithms/10_while_a_ne_b.png) | WHILE a &#8800; b<br>&emsp;OUTPUT b<br>&emsp;a &#8592; USERINPUT<br>ENDWHILE | while a != b:<br>&emsp;print(b)<br>&emsp;a = input() |
Iteration:<br>For loop (count-up) | ![Iteration-FOR_UP](img/algorithms/11_for_up.png) | FOR i &#8592; 0 TO 9<br>&emsp;OUTPUT i<br>ENDFOR | for i in range(10):<br>&emsp;print(i) |
Iteration:<br>For loop (count-down) | ![Iteration-FOR_DOWN](img/algorithms/12_for_dn.png) | FOR i &#8592; 10 TO 1<br>&emsp;OUTPUT i<br>ENDFOR | for i in range(10, 0, -1):<br>&emsp;print(i) |

##Links  
Some useful Pseudocode links.  

1. [PseudoCode CheatSheet](/cheatSheets/PseudoCode%20CheatSheet.pdf)
2. [PseudoWars](http://pseudowar.appjar.info)
3. [AQA PseudoCode Guidelines](http://filestore.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF)
