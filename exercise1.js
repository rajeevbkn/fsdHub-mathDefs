/* Programme to find sum of multiples of 3 and 5 from an array of numbers */
mA = [1, 2, 3, 4, 5 ,6, 7, 8 ,9];
var i;
var sum3 = 0;
var sum5 = 0;
for(i=0; i < mA.length + 1; i++) {
  if (i % 3 === 0) {
    sum3 += i;
  } else if (i % 5 === 0) {
    sum5 += i;
  } else {
    /*console.log(i + ' is not a multiple of 3 or 5.');*/
  }
}
console.log('In the given array [' + mA + '], the sum of multiples of 3 is ' + sum3 + ' and the sum of multiples of 5 is ' + sum5);
