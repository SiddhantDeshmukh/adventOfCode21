import { sonarSweep } from "./sonar_sweep";

describe("Day 1: Sonar Sweep", () => {
  it("handles arrays with one or zero indices", () => {
    expect(sonarSweep([])).toEqual(0);
    expect(sonarSweep([100])).toEqual(0);
  });

  it("returns the correct number of increases", () => {
    const data = [10, 15, 20, 15, 20];
    expect(sonarSweep(data)).toEqual(3);
  });
});
