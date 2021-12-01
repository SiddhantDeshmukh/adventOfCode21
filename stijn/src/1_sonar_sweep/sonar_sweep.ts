import * as dataset from "./data.json";

/**
 * Returns the number of times a value in the array is larger than the value of the previous index.
 */
export const sonarSweepPartOne = (measurements: number[]): number => {
  if (measurements.length <= 1) return 0;
  let measurementIncreases = 0;

  for (let i = 1; i < measurements.length; i++) {
    const previousMeasurement = measurements[i - 1];
    const currentMeasurement = measurements[i];

    if (currentMeasurement > previousMeasurement) {
      measurementIncreases += 1;
    }
  }

  return measurementIncreases;
};

/**
 * Returns the amount of times the sum of the numbers in a 3-index sliding window are higher than
 * the previous window.
 */
export const sonarSweepPartTwo = (measurements: number[]): number => {
  if (measurements.length < 4) return 0;
  let measurementIncreases = 0;

  for (let i = 1; i < measurements.length - 2; i++) {
    const previousMeasurement =
      measurements[i - 1] + measurements[i] + measurements[i + 1];
    const currentMeasurement =
      measurements[i] + measurements[i + 1] + measurements[i + 2];

    if (currentMeasurement > previousMeasurement) {
      measurementIncreases += 1;
    }
  }

  return measurementIncreases;
};

export default () => {
  console.log("Day 1. Sonar Sweep");
  console.log("");

  console.log(
    "Challenge 1: count the number of times a depth measurement increases from the previous measurement."
  );
  console.log("Answer: ", sonarSweepPartOne(dataset.data));
  console.log("");
  console.log(
    "Challenge 2: count the number of times the sum of measurements in this sliding window increases from the previous sum."
  );
  console.log("Answer: ", sonarSweepPartTwo(dataset.data));
  console.log("");
  console.log("");
};
