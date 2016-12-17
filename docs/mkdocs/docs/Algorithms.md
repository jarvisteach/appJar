#Algorithms
----

##Links

1. [Online LMC](http://www.gcsecomputing.org.uk/lmc/index.html)
2. [LMC Explanation](http://www.yorku.ca/sychen/research/LMC/)
3. [PseudoCode CheatSheet](/cheatSheets/PseudoCode%20CheatSheet.pdf)
4. [PseudoWars](http://pseudowar.appjar.info)
5. [AQA PseudoCode Guidelines](http://filestore.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF)

##LMC

Instructions | Mneumonic | Machine Code | Explanation
------------ | --------- | ------------ | ----------- 
Add | <span style="color:#ff000;">ADD</span> | 1xx | Adds the contents of memory xx to the **ACCUMULATOR**.
Subtract | <span style="color:#ff0000;">SUB</span> | 2xx | Subtracts the contents of memory xx from the **ACCUMULATOR**.
Store | <span style="color:#a535ae;">STA</span> | 3xx | Copies the contents of the **ACCUMULATOR** to memory xx.
Load | <span style="color:#a535ae;">LDA</span> | 5xx | Copies the contents of memory xx to the **ACCUMULATOR**.
Branch ALWAYS | <span style="color:#00ff00;">BRA</span> | 6xx | Always set the program counter to xx. The program continues from the instruction at memory xx.
Branch if ZERO | <span style="color:#00ff00;">BRZ</span> | 7xx | Set the program counter to xx only of the **ACCUMULATOR** is zero.
Branch if POSITIVE | <span style="color:#00ff00;">BRP</span> | 8xx | Set the program counter to xx only if the **ACCUMULATOR** is zero or positive (greater than zero).
Input | <span style="color:#0000ff;">INP</span> | 901 | Copy the contents of the **INBOX** to the **ACCUMULATOR**.
Output | <span style="color:#0000ff;">OUT</span> | 902 | Copy the contents of the **ACCUMULATOR** to the **OUTBOX**.
Define Variable | **DAT** | | Reserves this memory slot as a variable, settinmg its contents to the value specified.
Halt | **HLT** | 000 | Halts execution of the program.

##Details

Topic | FlowChart | PseudoCode | Python | Machine Code | Assembler
----- | --------- | ---------- | ------ | ------------ | ---------
Assigning a variable | ![Assignment](img/algorithms/1_a_eq_5.png) | a &#8592; 5 | a=5 | a DAT 5 | 
Input | ![Input](img/algorithms/2_a_eq_inp.png) | a &#8592; USERINPUT | a=input() | INP<br>STA a | 901<br>3xx
Output | ![Assignment](img/algorithms/3_prt_a.png) | a &#8592; 5 | a=5 | LDA a<br>OUT  | 5xx<br>902 
Addition | ![Assignment](img/algorithms/4_a_eq_b_pl_c.png) | a &#8592; b + c | a=b+c | LDA b<br>ADD c<br>STA a | 5xx<br>1xx<br>3xx 
Subtraction | ![Assignment](img/algorithms/5_a_eq_b_mi_c.png) | a &#8592; b - c | a=b-c | LDA b<br>SUB c<br>STA a | 5xx<br>2xx<br>3xx
Selection:<br>Greater than | ![Assignment](img/algorithms/6_a_gt_b.png) | a &gt; b THEN<br>funcA()<br>ELSE<br>funcB() | a &gt; b:<br>funcA()<br>else:<br>funcB() | LDA b<br>SUB a<br>BRP funcA<br>BRA funB | 5xx<br>2xx<br>8xx<br>6xx 
Selection:<br>Less than | ![Assignment](img/algorithms/.png) | a &#8592; 5 | a=5 | a DAT 5 | 
Selection:<br>Equal to | ![Assignment](img/algorithms/.png) | a &#8592; 5 | a=5 | a DAT 5 | 
Selection:<br>Not equal to | ![Assignment](img/algorithms/.png) | a &#8592; 5 | a=5 | a DAT 5 | 
Iteration:<br>While loop | ![Assignment](img/algorithms/.png) | a &#8592; 5 | a=5 | a DAT 5 | 
Iteration:<br>For loop (count-up) | ![Assignment](img/algorithms/.png) | a &#8592; 5 | a=5 | a DAT 5 | 
Iteration:<br>For loop (count-down) | ![Assignment](img/algorithms/.png) | a &#8592; 5 | a=5 | a DAT 5 | 

<table>

        <tr>
            <td valign="top">Selection: Less Than</td>
            <td valign="top">&nbsp;<img alt="7_a_lt_b.png" src="/img/algorithms/7_a_lt_b.png" style="margin:5px;width:180px;"></td>
            <td valign="top"><span style="color:#0000ff;">IF</span> a &lt; b <span style="color:#0000ff;">THEN</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcA()<br><span style="color:#0000ff;">ELSE</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcB()<br><span style="color:#0000ff;">ENDIF</span></td>
            <td valign="top"><pre style="background:#ffffff;color:#000000;"><span style="color:#ff5600;">if</span> a &lt; b<span style="color:#ff5600;">:</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcA()<span style="color:#ff5600;"><br>else</span><span style="color:#ff5600;">:</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcB()</pre></td>
            <td valign="top"><span style="color:#a535ae;">LDA</span> a<br><span style="color:#ff0000;">SUB</span> b<br><span style="color:#00ff00;">BRP</span> funcB<br><span style="color:#00ff00;">BRA</span> funcA</td>
            <td valign="top">5xx<br>2xx<br>8xx<br>6xx</td>
        </tr>

        <tr>
        <td valign="top">Selection: Equal To</td>
        <td valign="top">&nbsp;<img alt="8_a_eq_b.png" src="/img/algorithms/8_a_eq_b.png" style="margin:5px;width:188px;"></td>
        <td valign="top"><span style="color:#0000ff;">IF</span> a = b <span style="color:#0000ff;">THEN</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcA()<br><span style="color:#0000ff;">ELSE</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcB()<br><span style="color:#0000ff;">ENDIF</span></td>
        <td valign="top"><pre style="background:#ffffff;color:#000000;"><span style="color:#ff5600;">if</span> a == b<span style="color:#ff5600;">:</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcA()<br><span style="color:#ff5600;">else</span><span style="color:#ff5600;">:</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcB()</pre></td>
        <td valign="top"><span style="color:#a535ae;">LDA</span> a<br><span style="color:#ff0000;">SUB</span> b<br><span style="color:#00ff00;">BRZ</span> funcA<br><span style="color:#00ff00;">BRA</span> funcB</td>
        <td valign="top">5xx<br>2xx<br>7xx<br>6xx</td>
        </tr>

        <tr>
            <td nowrap valign="top">Selection: Not Equal To</td>
            <td valign="top">&nbsp;<img alt="9_a_ne_b.png" src="/img/algorithms/9_a_ne_b.png" style="margin:5px;width:183px;"></td>
            <td valign="top"><span style="color:#0000ff;">IF</span> a &#8800; b <span style="color:#0000ff;">THEN</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcA()<br><span style="color:#0000ff;">ELSE</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcB()<br><span style="color:#0000ff;">ENDIF</span></td>
            <td valign="top"><pre style="background:#ffffff;color:#000000;"><span style="color:#ff5600;">if</span> a <span style="color:#ff5600;">!</span><span style="color:#ff5600;">=</span> b<span style="color:#ff5600;">:</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcA()<span style="color:#ff5600;"><br>else</span><span style="color:#ff5600;">:</span><br>&nbsp;&nbsp;&nbsp;&nbsp;funcB()</pre></td>
            <td valign="top"><span style="color:#a535ae;">LDA</span> a<br><span style="color:#ff0000;">SUB</span> b<br><span style="color:#00ff00;">BRZ</span> funcB<br><span style="color:#00ff00;">BRA</span> funcA</td>
            <td valign="top">5xx<br>2xx<br>7xx<br>6xx</td>
        </tr>

        <tr>
            <td valign="top">Iteration: While Loop</td>
            <td valign="top">&nbsp;<img alt="10_while_a_ne_b.png" src="/img/algorithms/10_while_a_ne_b.png" style="margin:5px;width:200px;height:133px;"></td>
            <td nowrap valign="top"><span style="color:#0000ff;">WHILE</span> a &#8800; b<br>&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">OUTPUT</span> b<br>&nbsp;&nbsp;&nbsp;&nbsp;a &#8592; <span style="color:#0000ff;">USERINPUT</span><br><span style="color:#0000ff;">ENDWHILE</span></td>
            <td valign="top"><pre style="background:#ffffff;color:#000000;"><span style="color:#ff5600;">while</span> a !<span style="color:#ff5600;">=</span> b:<br><span style="color:#a535ae;">&nbsp;&nbsp;&nbsp;&nbsp;print</span>(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;a <span style="color:#ff5600;">=</span> input()</pre></td>
            <td valign="top">
                <table border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr><td>while</td><td><span style="color:#a535ae;">LDA</span>&nbsp;</td><td>a</td></tr>
                        <tr><td></td><td><span style="color:#ff0000;">SUB</span></td><td>b</td></tr>
                        <tr><td></td><td><span style="color:#00ff00;">BRZ</span></td><td>endwhile</td></tr>
                        <tr><td></td><td><span style="color:#a535ae;">LDA</span></td><td>b</td></tr>
                        <tr><td></td><td><span style="color:#0000ff;">OUT</span></td><td></td></tr>
                        <tr><td></td><td><span style="color:#0000ff;">INP</span></td><td></td></tr>
                        <tr><td></td><td><span style="color:#a535ae;">STA</span></td><td>a</td></tr>
                        <tr><td></td><td><span style="color:#00ff00;">BRA</span></td><td>while</td></tr>
                        <tr><td>endwhile&nbsp;</td><td><strong>HLT</strong></td><td></td></tr>
                        <tr><td>a</td><td>DAT</td><td>0</td></tr>
                        <tr><td>b</td><td>DAT</td><td>5</td></tr>
                    </tbody>
                </table>
            </td>

            <td valign="top">5xx<br>2xx<br>7xx<br>5xx<br>902<br>901<br>3xx<br>6xx<br>000</td>

        </tr>
        
        <tr>
            <td valign="top">Iteration: For Loop (count-up)</td>
            <td valign="top">&nbsp;<img alt="11_for_up.png" src="/img/algorithms/11_for_up.png" style="margin:5px;width:200px;height:188px;"></td>
            <td valign="top"><span style="color:#0000ff;">FOR</span> i &#8592; 0 TO 9<br>&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">OUTPUT</span> i<br><span style="color:#0000ff;">ENDFOR</span></td>
            <td valign="top"><pre style="background:#ffffff;color:#000000;"><span style="color:#ff5600;">for</span> i <span style="color:#ff5600;">in</span> range(10):<br><span style="color:#a535ae;">&nbsp;&nbsp;&nbsp;&nbsp;print</span>(i)</pre></td>
            <td valign="top">
                <table border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr>
                            <td>for&nbsp;</td>
                            <td><span style="color:#a535ae;">LDA</span>&nbsp;</td>
                            <td>i</td>
                        </tr>
                        <tr>
                            <td>&nbsp;</td>
                            <td><span style="color:#0000ff;">OUT</span></td>
                            <td>&nbsp;</td>
                        </tr>
                        <tr>
                            <td>&nbsp;</td>
                            <td><span style="color:#ff0000;">ADD</span></td>
                            <td>one</td>
                        </tr>
                        <tr>
                            <td>&nbsp;</td>
                            <td><span style="color:#a535ae;">STA</span></td>
                            <td>i</td>
                        </tr>
                        <tr>
                            <td>&nbsp;</td>
                            <td><span style="color:#ff0000;">SUB</span></td>
                            <td>ten</td>
                        </tr>
                        <tr>
                            <td>&nbsp;</td>
                            <td><span style="color:#00ff00;">BRZ</span></td>
                            <td>endfor</td>
                        </tr>
                        <tr>
                            <td>&nbsp;</td>
                            <td><span style="color:#00ff00;">BRA</span></td>
                            <td>for</td>
                        </tr>
                        <tr>
                            <td>endfor&nbsp;</td>
                            <td><strong>HLT</strong></td>
                            <td>&nbsp;</td>
                        </tr>
                        <tr>
                            <td>i</td>
                            <td>DAT</td>
                            <td>0</td>
                        </tr>
                        <tr>
                            <td>one</td>
                            <td>DAT</td>
                            <td>1</td>
                        </tr>
                        <tr>
                            <td>ten</td>
                            <td>DAT</td>
                            <td>10</td>
                        </tr>
                    </tbody>
                </table>
            </td>
            <td valign="top">5xx<br>902<br>1xx<br>3xx<br>2xx<br>7xx<br>6xx<br>000</td>
        </tr>

        <tr>
            <td valign="top">Iteration: For Loop (count-down)</td>
            <td valign="top">&nbsp;<img alt="12_for_dn.png" src="/img/algorithms/12_for_dn.png" style="margin:5px;width:200px;height:201px;"></td>
            <td valign="top"><span style="color:#0000ff;">FOR</span> i &#8592; 10 TO 1<br>&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">OUTPUT</span> i<br><span style="color:#0000ff;">ENDFOR</span></td>
            <td nowrap valign="top"><pre style="background:#ffffff;color:#000000;"><span style="color:#ff5600;">for</span> i <span style="color:#ff5600;">in</span> range(10, 0, -1):<br><span style="color:#a535ae;">&nbsp;&nbsp;&nbsp;&nbsp;print</span>(i)</pre></td>
            <td valign="top">
                <table border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr><td>for&nbsp;</td><td><span style="color:#a535ae;">LDA</span>&nbsp;</td><td>i</td></tr>
                        <tr><td>&nbsp;</td><td><span style="color:#0000ff;">OUT</span></td><td>&nbsp;</td></tr>
                        <tr><td>&nbsp;</td><td><span style="color:#ff0000;">SUB</span></td><td>one</td></tr>
                        <tr><td>&nbsp;</td><td><span style="color:#a535ae;">STA</span></td><td>i</td></tr>
                        <tr><td>&nbsp;</td><td><span style="color:#00ff00;">BRZ</span></td><td>endfor</td></tr>
                        <tr><td>&nbsp;</td><td><span style="color:#00ff00;">BRA</span></td><td>for</td></tr>
                        <tr><td>endfor&nbsp;</td><td><strong>HLT</strong></td><td>&nbsp;</td></tr>
                        <tr><td>i</td><td>DAT</td><td>10</td></tr><tr><td>one</td><td>DAT</td><td>1</td></tr>
                    </tbody>
                </table>
            </td>
        
            <td valign="top">
                <table border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr><td>00&nbsp;&nbsp;&nbsp;&nbsp;</td><td>5xx&nbsp;&nbsp;&nbsp;&nbsp;</td><td>507</td></tr>
                        <tr><td>01</td><td>902</td><td>902</td></tr><tr><td>02</td><td>2xx</td><td>208</td></tr>
                        <tr><td>03</td><td>3xx</td><td>307</td></tr><tr><td>04</td><td>7xx</td><td>706</td></tr>
                        <tr><td>05</td><td>6xx</td><td>600</td></tr><tr><td>06</td><td>000</td><td>000</td></tr>
                        <tr><td>07</td><td></td><td>10</td></tr><tr><td>08</td><td></td><td>1</td></tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>
