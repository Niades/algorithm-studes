/**
* @param {character[]} s
* @return {void} Do not return anything, modify s in-place instead.
*/
var reverseString = function(s) {
  console.log("Initial s = ", s);
  let buffer;
  const MAX_I_VALUE = Math.ceil(s.length / 2);
  for(let i = 0; i < MAX_I_VALUE; i++) {
    buffer = s[s.length - i - 1];      
    s[s.length - i - 1] = s[i];
    s[i] = buffer;
  }
  return s;
};