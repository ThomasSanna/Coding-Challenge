# Smallest Missing Positive Integer

### This function takes an array of numbers as input and returns the smallest positive integer that does not appear in the array. For example, if the array is [3, 4, -1, 1], the function should return 2, because 2 is the smallest positive integer that does not appear in the array.


## Usage

```javascript
const arr = [3, 4, -1, 1];
const smallestMissing = smallestMissingPositiveInteger(arr);
console.log(smallestMissing); // Output: 2
```

## Function signature

```javascript
function smallestMissingPositiveInteger(arr: number[]): number
```

### The function takes an array of numbers as input and returns a number.