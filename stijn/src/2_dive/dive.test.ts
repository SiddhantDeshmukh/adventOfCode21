import { divePartOne, divePartTwo, Course } from "./dive";

describe("Day 2: Dive", () => {
  describe("Part One: what do you get if you multiply your final horizontal position by your final depth?", () => {
    it("returns the expected multiplied depth and horizontal position", () => {
      const course: Course = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
      ];

      expect(divePartOne(course)).toEqual(150);
    });

    it("throws an error when it receives an invalid course", () => {
      // @ts-ignore We're simulating an invalid course which can for instance occur when parsing a json.
      const course: Course = ["forward banana"];
      expect(() => divePartOne(course)).toThrow();

      // @ts-ignore We're simulating an invalid course which can for instance occur when parsing a json.
      expect(() => divePartOne(["banana 3"])).toThrow();
    });
  });

  describe("Part Two: what do you get if you multiply your final horizontal position by your final depth?", () => {
    it("returns the expected multiplied depth and horizontal position", () => {
      const course: Course = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
      ];

      expect(divePartTwo(course)).toEqual(900);
    });

    it("throws an error when it receives an invalid course", () => {
      // @ts-ignore We're simulating an invalid course which can for instance occur when parsing a json.
      expect(() => divePartTwo(["forward banana"])).toThrow();

      // @ts-ignore We're simulating an invalid course which can for instance occur when parsing a json.
      expect(() => divePartTwo(["banana 3"])).toThrow();
    });
  });
});
