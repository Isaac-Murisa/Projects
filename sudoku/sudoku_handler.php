<?php
require('sudoku.php');

$sudoku = new sudoku();

$gen = $sudoku->generate();
echo json_encode($gen);

?>