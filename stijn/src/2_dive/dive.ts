import * as dataset from "./data.json";

export type SubmarineCommand = `${"up" | "down" | "forward"} ${number}`;
export type Course = SubmarineCommand[];

/**
 * Returns the product of the final depth and horizontal position.
 */
export const divePartOne = (course: Course): number => {
  const position = { depth: 0, horizontal: 0 };

  course.forEach((submarineCommand) => {
    const instruction = submarineCommand.match(/^(down|up|forward)/)?.[0];
    const distance = parseInt(submarineCommand.match(/([0-9])*$/)?.[0], 10);

    if (typeof instruction === "undefined") {
      throw new Error(
        `Invalid course "${submarineCommand}". Unable to parse the instruction.`
      );
    }

    if (isNaN(distance)) {
      throw new Error(
        `Invalid course "${submarineCommand}". Unable to parse the distance.`
      );
    }

    switch (instruction) {
      case "up": {
        position.depth -= distance;
        break;
      }
      case "down": {
        position.depth += distance;
        break;
      }
      case "forward": {
        position.horizontal += distance;
        break;
      }
    }
  });

  return position.depth * position.horizontal;
};

/**
 * Returns the product of the final depth and horizontal position.
 */
export const divePartTwo = (course: Course): number => {
  const position = { depth: 0, horizontal: 0, aim: 0 };

  course.forEach((submarineCommand) => {
    const instruction = submarineCommand.match(/^(down|up|forward)/)?.[0];
    const amount = parseInt(submarineCommand.match(/([0-9])*$/)?.[0], 10);

    if (typeof instruction === "undefined") {
      throw new Error(
        `Invalid course "${submarineCommand}". Unable to parse the instruction.`
      );
    }

    if (isNaN(amount)) {
      throw new Error(
        `Invalid course "${submarineCommand}". Unable to parse the amount.`
      );
    }

    switch (instruction) {
      case "up": {
        position.aim -= amount;
        break;
      }
      case "down": {
        position.aim += amount;
        break;
      }
      case "forward": {
        position.horizontal += amount;
        position.depth += position.aim * amount;
        break;
      }
    }
  });

  return position.depth * position.horizontal;
};

export default () => {
  console.log("Day 2. Dive");
  console.log("");

  console.log(
    "Challenge 1: what do you get if you multiply your final horizontal position by your final depth?"
  );

  console.log("Answer: ", divePartOne(dataset.data as Course));
  console.log("");
  console.log(
    "Challenge 2: what do you get if you multiply your final horizontal position by your final depth?"
  );
  console.log("Answer: ", divePartTwo(dataset.data as Course));
  console.log("");
};
