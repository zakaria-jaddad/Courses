<!DOCTYPE html>
<html lang="en">
<?php
$name = "Elzero Courses";
?>

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="<?php echo $name; ?>">
  <title>Welcome To
    <?php echo $name; ?>
  </title>
</head>

<body>
  <h1>
    <?php echo $name; ?>
  </h1>
  <p>Here In
    <?php echo $name; ?> We Provide Front-End And Back-End Courses
  </p>
  <hr>
  <div>
    <?php echo $name; ?> Is The What You Need.
  </div>
  <footer>All Right Reserved To
    <?php echo $name; ?>
  </footer>
</body>

</html>


<?php
echo "<br>";
echo "==== Problem 2 ====";
echo "<br>";

$name = "elzero";
$$name = "Web";

echo "This is: {$$name}";
echo "<br>";
echo "This is: $elzero";
echo "<br>";
echo "This is: ", $$name;
echo "<br>";
echo "This is: ", $elzero;
echo "<br>";
echo <<<"Elzero_Web"
  This is: {$$name}
  <br>
  This is: $elzero
Elzero_Web;
echo "<br>";
?>

<?php
echo "<br>";
echo "==== Problem 3 ====";
echo "<br>";

$a = 200;
$b = &$a;
$a = 100;

echo $b; // 100
echo "<br>";


?>

<?php
echo "<br>";
echo "==== Problem 4 ====";
echo "<br>";

echo __DIR__;
echo "<br>";
echo $_SERVER["HTTP_HOST"];
echo "<br>";
echo $_SERVER["HTTP_SEC_CH_UA_PLATFORM"];
echo "<br>";

echo "<br>";
?>

/*
  10 Words Here
  break
  clone
  use 
  __dir__
  __file__
  empty()
  final 
  foreach
  switch
*/

<?php
echo "<br>";
echo "==== Problem 4 ====";
echo "<br>";


echo "<br>";
echo __LINE__;
echo "<br>";
echo __FILE__;
echo "<br>";
echo __DIR__;
echo "<br>";