interface Item {
  profit: number,
  weight: number,
  value: number,
};

// O(n) (not confirmed, my estimate)
// Algorithm: Top-down DP
/*
  The approach here is just something that popped into my head.
  I have no idea what kind of pattern of algorithm is applicable (if
  applicable to this).

  Let me try to figure it out.

  I have written some comments in the code. It seems like I apply DP
  patterns here. Top-down DP.

*/


function solveKnapsack(profits: number[], weights: number[], capacity: number): number {
  // Main problem optimal result
  const knapsack: Item[] = [];
  // Subproblems
  profits.forEach((profit, i) => {
    // Subproblem
    const weight = weights[i];
    const value = profit / weight;
    const item: Item = {
      profit,
      weight,
      value,
    };
    if(knapsack.length === 0) {
      knapsack.push(item);
    } else if(knapsack[0].value >= value) {
      knapsack.push(item);
    } else {
      knapsack.unshift(item);
    }
  });
  // Collecting all the subproblem optimal results
  // to calculate optimal result
  let result = 0,
      currentCapacity = 0;
  knapsack.forEach((item: Item) => {
    if(currentCapacity > capacity) {
      return false;
    }
    if(currentCapacity + item.weight <= capacity) {
      currentCapacity += item.weight;
      result += item.profit;
    }
    return true;
  });
  // Returning solution to the top problem
  return result;
}


var profits = [1, 1, 4, 5];
var weights = [1, 2, 9, 2];
console.log(`Total knapsack profit: ---> ${solveKnapsack(profits, weights, 2)} === 5`);
console.log(`Total knapsack profit: ---> ${solveKnapsack(profits, weights, 9)} === 7`);