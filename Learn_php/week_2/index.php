<?php

$problem_one = 15.2 + 14.7 + (10.5 + 10.5);

echo (int) $problem_one, "\n"; // => 50
echo gettype((integer) $problem_one), "\n"; // => Integer

echo "\n== Problem 2 ==\n";

$problem_tow = 100;

echo gettype($problem_tow), "\n";
echo var_dump($problem_tow); // returns new line 
echo is_int($problem_tow), "\n";


echo "\n== Problem 3 ==\n";

// Needed Output
// Hello "Elzero" \\ """ We Love "$$PHP"
echo "Hello, \"Elzero\" \\\\ \"\"\" We Love \"\$\$PHP\" \n";



echo "\n== Problem 4 ==\n";

// Needed Output
/* 
    We
    Love
    Elzero
    Web
    School
 */
echo "We \nLove \nElzero \nWeb \nSchool\n";


echo "\n== Problem 5 ==\n";
/* 
  Needed Output
  Hello "'Elzero'"
  We Love $Programming$
  Languages Specially "PHP" 
 */

echo <<<'problem5'
    Hello "'Elzero'"
    We Love $Programming$
    Languages Specially "PHP" 
    
   problem5;

echo "\n== Problem 6 ==\n";

$something = "Programming";

echo <<<"code"
      Hello \PHP\
      We Love $something
      \n
    code;

// [1] Fix The Error
// [2] Remove 2 Characters To Get The Output

// Needed Output
// Hello \PHP\ We Love Programming

echo "\n== Problem 7 ==\n";
/* 
  Needed Output
  1
  integer 
*/

echo (boolean) "Hello PHP\n", "\n";
echo "<br>\n";
echo gettype((int) "Hello PHP"), "\n";


echo "\n== Problem 8 ==\n";

/* 
  Needed Outuput: 
  Array
(
[FrontEnd] => Array
(
  [0] => HTML
  [1] => CSS
  [JS] => Array
    (
      [Vuejs] => Array
        (
          [2] => v2
          [3] => v3
        )

      [0] => Reactjs
      [1] => Svelte
    )
)

[BackEnd] => Array
(
  [0] => PHP
  [1] => MySQL
  [2] => Security
)

[0] => Git
[1] => Github
[Testing] => Array
(
  [0] => Unit Testing
  [1] => End To End
  [2] => Integration
)
)
 */
$my_first_array = [
  "FrontEnd" => [
    "HTML",
    "CSS",
    "JS" => [
      "Vuejs" => [
        2 => "v2",
        3 => "v3"
      ],
      0 => "Reactjs",
      1 => "Svelte",
    ]
  ],
  "BackEnd" => [
    0 => "PHP",
    1 => "MySQL",
    2 => "Security",
  ],
  0 => "Git",
  1 => "Github",
  "Testing" => [
    0 => "Unit Testing",
    1 => "End To End",
    2 => "Integration"
  ],
];

echo "<pre>";
  echo print_r($my_first_array);
echo "</pre>";