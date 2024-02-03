<?php
/* 
  Replace ? With Arithmetic Operators
  echo 10 ? 20 ? 15 ? 3 ? 190 ? 10 ? 400; // 0
  */
echo "==== Problem 1 ====";
echo "<br>";
echo 10 * 20 + 15 % 3 + 190 + 10 - 400; // 0
echo "<br>";


echo "==== Problem 2 ====";
echo "<br>";
/* 
  $a = "10";

  Needed Ouput
  10
  "integer"
  10
  "integer"
  10
  "integer"

  For The People Who Love Searching
  10
  "integer"
  10
  "integer"
 */

$a = "10";

echo (integer) $a;
echo "<br>";
echo var_dump((integer) $a);
echo "<br>";
echo intval($a);
echo "<br>";
echo +$a;
echo "<br>";
echo -(-$a);
echo "<br>";


echo "==== Problem 3 ====";
echo "<br>";

$a = 10;
$b = 20;

// Needed Output
// -1

echo "hello wold!!\n";
echo $b > $a || false;


echo "==== Problem 4 ====";
echo "<br>";


$a = 10;
$b = 20;
$c = 15;

var_dump($a < $b); // True
var_dump($c >= $a); // True
var_dump($a <= $b); // True
var_dump($a != $b); // True
var_dump($a != $c); // True
var_dump($a !== $c); // True
var_dump(gettype($a) === gettype($b)); // True
var_dump(gettype($a) === gettype($b)); // True
var_dump(gettype((float) $a) !== gettype($b)); // True



echo "==== Problem 5 ====";
echo "<br>";

$points = 10;

$points++;
$points++;
$points++;


echo $points; // 13
echo "<br>";

$points--;
$points--;
$points--;
$points--;
$points--;

echo $points; // 8;
echo "<br>";

echo "==== Problem 6 ====";
echo "<br>";

$a = "Elzero";
$b = "Web";
$c = "School";

// Method One
$d = $a . ' ' . $b . ' ' . $c;

// Method Two
$d = "$a $b $c";

// Method Three
$d = "{$a} {$b} {$c}";

// Method Four
$d = $a . " ";
$d .= $b . " ";
$d .= $c;

echo $d; // Elzero Web School



echo "==== Problem 7 ====";
echo "<br>";

$a = 10;
$b = 20;

echo $a + $b * $a + $b + $a * $a * $a; // 10000

echo "==== Problem 8 ====";
echo "<br>";

unset($b);
// Code 1
$a = @$b or die("This Is A Custom Error");

// Code 2
$f = @file("Not_A_File") or die("This Is Not A Valid File Name"); 

// Code 3
@(include("Not_A_File")) or die("This Is Not A Valid PHP File Name");