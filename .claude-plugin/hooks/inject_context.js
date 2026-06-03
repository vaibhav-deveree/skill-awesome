const fs = require('fs');
const path = require('path');

// Determine the path to the engineering-principles SKILL.md
const skillPath = path.join(__dirname, '..', '..', 'skills', 'engineering-principles', 'SKILL.md');

if (fs.existsSync(skillPath)) {
    console.log("--- ZERO ASSIST AI ENGINEERING FRAMEWORK CONTEXT ---");
    console.log("You are operating under the following engineering principles, constraints, and PR workflows:");
    console.log(fs.readFileSync(skillPath, 'utf8'));
    console.log("--------------------------------------------------");
} else {
    console.log("Warning: skill-awesome engineering principles file not found.");
}
