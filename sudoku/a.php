<html>
	<head>
        <title>Sudoku</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
		
		<style>
            table {
                border-collapse: collapse;
                width: 500px;
                height: 500px;   
            }
			colgroup {
				border: solid medium;
			}
            table, td, tr{
               border: 0.5px solid darkgray; 
               text-align: center;
               vertical-align: center;
            }
            tr:nth-child(3) {
				border-bottom: solid medium;
            }
            tr:nth-child(7) {
				border-top: solid medium;
            }
			td {
				align: center;
			}
            
        </style>
		
			
			<?php
			
				require('sudoku.php');

				$sudoku = new sudoku();

				$gen = $sudoku->generate();
			?>
				
		</script>
		
	</head>
	<body>
		<div id="s_container" align="center">
			
			<p id="zvangu"></p>
			
			<select id="levels">
                <option name="easy" value="e" selected="selected">Easy</option>
                <option name="hard" value="h">Hard</option>
            </select>
            <input type="button" name="gen" value="Generate" onclick="generate()">
            <p id="mee"></p>
            <table id="td_sudoku">
			
				<colgroup><col><col><col>
				<colgroup><col><col><col>
				<colgroup><col><col><col>
				
					<tr> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="1"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="2"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="3"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="4"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="5"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="6"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="7"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="8"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="9"></td> 
					</tr>
					<tr> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="10"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="11"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="12"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="13"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="14"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="15"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="16"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="17"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="18"></td> 
					</tr>
					<tr> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="19"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="20"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="21"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="22"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="23"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="24"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="25"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="26"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="27"></td> 
					</tr>
				
					<tr> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="28"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="29"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="30"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="31"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="32"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="33"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="34"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="35"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="36"></td> 
					</tr>
					<tr> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="37"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="38"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="39"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="40"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="41"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="42"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="43"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="44"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="45"></td> 
					</tr>
					<tr> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="46"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="47"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="48"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="49"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="50"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="51"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="52"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="53"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="54"></td> 
					</tr>
				
					<tr> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="55"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="56"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="57"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="58"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="59"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="60"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="61"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="62"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="63"></td> 
					</tr>
					<tr> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="64"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="65"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="66"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="67"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="68"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="69"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="70"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="71"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="72"></td> 
					</tr>
					<tr> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="73"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="74"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="75"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="76"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="77"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="78"></td>   
						<td><input class="w3-input w3-border-0" type="text" size="1" id="79"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="80"></td> 
						<td><input class="w3-input w3-border-0" type="text" size="1" id="81"></td> 
					</tr>
            </table></br>
			<input type="button" name="solu" value="Solve Soduku" onclick="solution()">
			<input type="button" name="newS" value="New Sudoku" onclick="window.location.reload()">
			<p id="output"></p>
			
			<script>
				var  z = <?php echo json_encode($gen); ?>;
				document.getElementById("zvangu").innerHTML = z;
				
				function generate(){
					
					var lev = document.getElementById("levels");
					display();
					level(lev);
					
				}
				
				function display() {
					var num = '1';
					for (i = 0; i < 9; i++) {
						for (j = 0; j < 9; j++) {
							document.getElementById(num).value = z[i][j];
							num++;
						}
					}
				}
				
				function level(a){
					var user_l = a.options[a.selectedIndex].value;
					if (user_l == "e"){
						easy();
					}
					else {
						hard();
					}
				}
				
				function easy(){
					var x = '1';
					
					for (i = 0; i < 57; i++) {
						x = Math.floor((Math.random() * 81) + 1);
						document.getElementById(x).value = "";
					}
				}
				
				function hard(){
					var x = '1';
					
					for (i = 0; i < 81; i++) {
						x = Math.floor((Math.random() * 81) + 1);
						document.getElementById(x).value = "";
					}
					
				}
				
				function solution(){
					display();
					var total = 0;
					var wrong = false;
					var m = '1';
					for (i = 0; i < 9; i++) {
						for (j = 0; j < 9; j++) {
							ans = document.getElementById(m).value;
							if (ans != z[i][j]) {
								wrong = true;
								total = total + 10;
							}
							else {
								total = total - 5;
							}
							m++;
						}
					}
					merits(wrong);
				}
				/*
				function merits(b){
					if (b===true) {
						document.getElementById("output").innerHTML = "Unsucceful but your score is: " + total;
					}
					else {
						document.getElementById("output").innerHTML = "Succeful!! congratulation. Your score is : " = total;
					}
				}
				*/
			</script>
			
		</div>
	<body>
</html> 