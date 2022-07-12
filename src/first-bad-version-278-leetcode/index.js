/**
* Definition for isBadVersion()
* 
* @param {integer} version number
* @return {boolean} whether the version is bad
*/
const isBadVersion = function(version) {
  if(version >= 4) {
    return true;
  }
  return false;
};
  
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
      return binarySearchMod(n, isBadVersion)
    };
  };
  
  function binarySearchMod(n, isBadVersion) {
    if(n === 1) {
      return n;
    }
    let left = 0, right = n - 1;
    const totalLength = right - left;
    while(left < right) {
      console.log("* Iteration starting, left = ", left, ", right = ", right);
      const length = right - left;
      const middleIdx = Math.floor(length / 2);
      const middleValue = left + middleIdx + 1;
      const middleValueBad = isBadVersion(middleValue);
      console.log({ length, middleIdx, middleValue, middleValueBad });
      if(length === 0) {
        return -1;
      }
      if(middleValueBad) {
        console.log("before isBadVersion", isBadVersion(middleValue - 1))
        if(length >= 2 && isBadVersion(middleValue - 1)) {
          console.log("Found bad version, but continuing.")
        } else {
          return left - 1;
        }
      }
      if (middleValue > n) {
        console.log("Going right")
        left = totalLength - middleIdx + 1;
        right = 
        console.log("* Iteration end ", {left, right});
      } else if (middleValue < n) {
        console.log("Going left")
        left = Math.max(totalLength - length - middleIdx + 1, 0);
        right = totalLength - middleIdx;
        console.log("* Iteration end ", {left, right});
      }
    }
    return left;
  }

  console.log("result = ", solution(isBadVersion)(5));