// -- Directions 
// Given an integer, return an integer that is the reverse
// ordering of numbers 

// -- Examples 
// reverseInt(15) === 51
// reverseInt(981) === 189
// reverseInt(500) === 5
// reverseInt(-15) === -51
// reverseInt(-98) === -9

function reverseInt(n) {
    const reverse = n.toString().split('').reverse().join('');
    return parseInt(reverse) * Math.sign(n);
}

console.log(reverseInt(15)); 
console.log(reverseInt(-123));  
console.log(reverseInt(0));  
