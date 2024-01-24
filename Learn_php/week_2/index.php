<?php

  $problem_one = 15.2 + 14.7 + (10.5 + 10.5); 

  echo (int) $problem_one, "\n"; // => 50
  echo gettype((integer) $problem_one), "\n"; // => Integer

  echo "\n== Problem 2 ==\n";

  $problem_tow = 100;

  echo gettype($problem_tow), "\n";
  echo var_dump( $problem_tow); // returns new line 
  echo is_int($problem_tow), "\n";


  echo "\n== Problem 3 ==\n";

  // Needed Output
  // Hello "Elzero" \\ """ We Love "$$PHP"
  echo "Hello, \"Elzero\" \\\\ \"\"\" We Love \"\$\$PHP\" \n";
  
