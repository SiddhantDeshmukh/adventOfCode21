import { sonarSweepPartOne, sonarSweepPartTwo } from "./sonar_sweep";

describe("Day 1: Sonar Sweep", () => {
  describe("Part One: count the number of times a depth measurement increases from the previous measurement.", () => {
    it("handles arrays with one or zero indices", () => {
      expect(sonarSweepPartOne([])).toEqual(0);
      expect(sonarSweepPartOne([100])).toEqual(0);
    });

    it("returns the correct number of increases", () => {
      const data = [10, 15, 20, 15, 20];
      expect(sonarSweepPartOne(data)).toEqual(3);
    });
  });

  describe("Part Two: count the number of times the sum of measurements in this sliding window increases from the previous sum", () => {
    it("handles arrays with less than 4 indices", () => {
      const data = [10, 20, 5];
      expect(sonarSweepPartTwo(data)).toEqual(0);
    });

    it("returns the correct number of increase", () => {
      const data = [199, 200, 208, 210, 220, 5, 100];
      expect(sonarSweepPartTwo(data)).toEqual(2);
    });
  });
});
