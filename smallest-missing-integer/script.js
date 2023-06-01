// Challenge 1 : write a function that takes an array of numbers as input and returns the smallest positive integer 
// that does not appear in the array. For example, if the array is [3, 4, -1, 1], the function should return 2, 
// because 2 is the smallest positive integer that does not appear in the array.

function smallestMissingPositiveInteger(arr) {
  const maxNum = Math.max(...arr);
  for (let i = 1; i <= maxNum + 1; i++) {
    if (!arr.includes(i)) {
      return i;
    }
  }
}