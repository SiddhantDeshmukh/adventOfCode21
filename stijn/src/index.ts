import "regenerator-runtime/runtime.js";
import sonarSweepChallenge from "./1_sonar_sweep/sonar_sweep";
import diveChallenge from "./2_dive/dive";

const run = async () => {
  console.log("=== Advent of Code 2021 ===");
  console.log("");
  sonarSweepChallenge();
  console.log(
    "-----------------------------------------------------------------------------------------------------------------------------"
  );
  console.log("");
  diveChallenge();
};

run();
