// -- Directions
// Given a string, return a new string with the reversed order of characters 
// -- Examples 
// reverse('hi') === 'ih'
// reverse('hello') === 'olleh'
// reverse('CodingMoney') === ''

function reverseFor(str) {
    let reversed = ''
    for (let i=0; i<str.length; i++)
    {
        reversed = str[i] + reversed
    }
    return reversed
}

console.log(reverseFor('Coding Ninjas'))

function reverseRecursive(str) {
    let reversed = ''
    for(let char of str)
    {
        reversed = char + reversed
    }
    return reversed
}
console.log(reverseRecursive('coding Ninjas'))

function reverseMethods(str)
{
    const strToArray = str.split('')
    strToArray.reverse()
    return strToArray.join('')
}
console.log(reverseMethods('coding Ninjas'))

