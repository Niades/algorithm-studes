/**
* @param {number[]} nums
* @return {number[]}
*/
var sortedSquares = function(nums) {
  console.log({nums});
  const result = [];
  for(let i = 0; i < nums.length; i++) {
    const squared = nums[i] * nums[i];
    if(result.length === 0) {
      result.push(squared);
      continue;
    }
    if(squared < result[0]) {
      result.unshift(squared);
      continue;
    } else if(squared > result[result.length -1]) {
      result.push(squared);
      continue;
    } else {
      let idx = -1;
      const queue = [[[...result], 0]];
      while(queue.length > 0) {   
        const [arr, offset] = queue.pop();
        if(arr.length === 0) {
          idx = -1;
          break;
        } else if(arr.length === 1 ) {
          const item = arr[0];
          if(squared > item) {
            idx = 1 + offset;
            break;
          }
        }
        const middleIdx = Math.floor(arr.length / 2);
        const middle = arr[middleIdx];
        const before = arr[middleIdx - 1];
        const after = arr[middleIdx + 1];
        if(middle === squared ||
          (squared > before &&
            squared < arr[middle - 1])) {
              idx = middleIdx + offset;
        } else if(squared > arr[middleIdx + 1] || !arr[middleIdx + 1]) {
          queue.push([arr.slice(middleIdx + 1), middleIdx]);
          continue;
        } else if(squared < after || !after) {
          queue.push([arr.slice(0, middleIdx), middleIdx]);    
          continue;    
        }
      }
      result.splice(idx, 0, squared);
      console.log({squared}, " set to ", idx);
    }
  };
  return result;
};