// -- Directions 
// given a string, return true if the string is a palindrome
// or false if it is not Palindrome are strings that 
// form the same word if it is reversed

// -- Examples 
// palindrome("kayak") === true 
// palindrome("madam") === true 
// palindrome("codingmoney") === false 

function isPalindrome(str) {
    const reversed = str.split('').reverse().join('')
    return str === reversed
}

strings = "Coding Ninjas"
console.log(isPalindrome(strings))