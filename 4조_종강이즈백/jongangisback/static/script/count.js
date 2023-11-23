let $soju = document.querySelector("#soju");
let $beer = document.querySelector("#beer");
let $mak = document.querySelector("#mak");

let $sojuQuantity = document.querySelector("#soju-quantity");
let $beerQuantity = document.querySelector("#beer-quantity");
let $makQuantity = document.querySelector("#mak-quantity");

let $sojuMinus = document.querySelector("#soju-minus");
let $sojuPlus = document.querySelector("#soju-plus");
let $beerMinus = document.querySelector("#beer-minus");
let $beerPlus = document.querySelector("#beer-plus");
let $makMinus = document.querySelector("#mak-minus");
let $makPlus = document.querySelector("#mak-plus");

$sojuMinus.addEventListener("click", function () {
  if ($sojuQuantity.value > 0) {
    $sojuQuantity.value--;
  }
});
$sojuPlus.addEventListener("click", function () {
  $sojuQuantity.value++;
});
$beerMinus.addEventListener("click", function () {
  if ($beerQuantity.value > 0) {
    $beerQuantity.value--;
  }
});
$beerPlus.addEventListener("click", function () {
  $beerQuantity.value++;
});
$makMinus.addEventListener("click", function () {
  if ($makQuantity.value > 0) {
    $makQuantity.value--;
  }
});
$makPlus.addEventListener("click", function () {
  $makQuantity.value++;
});
