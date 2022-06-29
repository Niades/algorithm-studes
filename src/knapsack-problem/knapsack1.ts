interface Item {
  profit: number,
  weight: number,
  value: number,
};

// O(n)

function solveKnapsack(profits: number[], weights: number[], capacity: number): number {
  const knapsack: Item[] = [];
  profits.forEach((profit, i) => {
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
  let result = 0,
      currentCapacity = 0;
  knapsack.forEach((item: Item, i: number) => {
    if(currentCapacity > capacity) {
      return false;
    }
    if(currentCapacity + item.weight <= capacity) {
      currentCapacity += item.weight;
      result += item.profit;
    }
    return true;
  });
  return result;
}


var profits = [1, 1, 4, 5];
var weights = [1, 2, 9, 2];
console.log(`Total knapsack profit: ---> ${solveKnapsack(profits, weights, 2)} === 5`);
console.log(`Total knapsack profit: ---> ${solveKnapsack(profits, weights, 9)} === 7`);