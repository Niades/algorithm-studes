/**
* @param {number[]} nums
* @return {void} Do not return anything, modify nums in-place instead.
*/
var moveZeroes = function(nums) {
  const zeroIdc = [];
  for(let i = 0; i < nums.length; i++) {
    if(nums[i] === 0) {
      zeroIdc.push(i);
    }
  }
  console.log({nums, zeroIdc});
  for(let j = 0; j < zeroIdc.length; j++) {
    const zeroIdx = zeroIdc[j] - j;
    nums.splice(zeroIdx, 1);
    console.log({nums, zeroIdx});
    nums.push(0);
  }
  return nums;
};