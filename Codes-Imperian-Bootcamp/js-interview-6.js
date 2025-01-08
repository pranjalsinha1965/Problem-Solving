// --- Directions 
// write a function that accepts a string. The string should
// capitalize the first letter of each word in the string then 
// return the capitalized string. 
// ---Example 
// capitalize('this is mukhtar from coding money') --> 'This is Mukhtar From Cding Money'
// capitalize('what is titlecase ? ') --> 'What is Titlecase ?'
// capitlaize('titles of books, movies, songs, plays and other works') --> 'Titles Of Books, Movies, Songs, Plays and Other Works'

function capitalize(str) {
    const words = str.split(' ');
    const result = [];

    for (let word of words) {
        // Capitalize the first letter and concatenate with the rest of the word
        result.push(word[0].toUpperCase() + word.slice(1));
    }

    return result.join(' ');
}

console.log(capitalize('this is muktar from coding money'));
// Output: 'This Is Muktar From Coding Money'
