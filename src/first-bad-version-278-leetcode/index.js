/**
* Definition for isBadVersion()
* 
* @param {integer} version number
* @return {boolean} whether the version is bad
* isBadVersion = function(version) {
*     ...
* };
*/

/**
* @param {function} isBadVersion()
* @return {function}
*/
var solution = function(isBadVersion) {
  /**
  * @param {integer} n Total versions
  * @return {integer} The first bad version
  */
  return function(n) {
    const hayStack = Array.from(Array(n), (_, i) => i + 1);
    return binarySearchMod(n, hayStack, isBadVersion)
  };
};

function binarySearchMod(n, haystack, isBadVersion) {
  if(haystack.length === 0) {
    return -1;
  }
  if(n === 1) {
    return n;
  }
  const middleIdx = Math.floor(haystack.length / 2);
  const middleValue = haystack[middleIdx];
  const middleValueBad = isBadVersion(middleValue);
  console.log({ middleIdx, middleValue, middleValueBad });
  if(isBadVersion(middleValue)) {
    console.log("before isBadVersion", isBadVersion(middleValue - 1))
    if(haystack.length >= 2 && isBadVersion(middleValue - 1)) {
      console.log("Found bad version, but continuing.")
    } else {
      return middleValue;
    }
  }
  if (middleValueBad) {
    console.log("Going left")
    const leftHaystack =  haystack.slice(
      0, 
      haystack.length - middleIdx
      )
      //console.log({leftHaystack})
      return binarySearchMod(n, leftHaystack, isBadVersion, n);
    } else if (!middleValueBad) {
      console.log("Going right")
      const rightHaystack = haystack.slice(middleIdx + 1, haystack.length)
      //console.log({rightHaystack})
      return binarySearchMod(n, rightHaystack, isBadVersion)
    }
  }