import * as path from "path";
import * as dataset from "./data.json";

/**
 * Returns the number of times a value in the array is larger than the value of the previous index.
 */
export const sonarSweep = (measurements: number[]): number => {
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

export default () => {
  console.log("Day 1. Sonar Sweep");
  console.log(
    "Challenge: count the number of times a depth measurement increases from the previous measurement."
  );

  console.log("Answer: ", sonarSweep(dataset.data));
};
