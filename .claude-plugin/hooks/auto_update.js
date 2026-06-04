const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

// Determine the path to the plugin root
const pluginRoot = path.join(__dirname, '..', '..');
const timestampFile = path.join(pluginRoot, '.claude-plugin', 'last_update.txt');
const ONE_DAY = 24 * 60 * 60 * 1000; // 24 hours in milliseconds

let shouldUpdate = false;

// Check if we have updated recently
if (fs.existsSync(timestampFile)) {
    try {
        const lastUpdate = parseInt(fs.readFileSync(timestampFile, 'utf8'), 10);
        if (Date.now() - lastUpdate > ONE_DAY) {
            shouldUpdate = true;
        }
    } catch (e) {
        // If file is corrupted, force an update
        shouldUpdate = true;
    }
} else {
    shouldUpdate = true;
}

if (shouldUpdate) {
    try {
        // Write the new timestamp to prevent spamming updates
        fs.writeFileSync(timestampFile, Date.now().toString());

        // Spawn a detached background process to silently run the marketplace update
        const child = spawn('claude', ['plugins', 'marketplace', 'update', 'vaibhav-deveree/skill-awesome'], {
            detached: true,
            stdio: 'ignore', // Completely silent, does not block the terminal
            windowsHide: true // Hide terminal window on Windows
        });

        // Unref the child process so the parent (Claude Code) can exit independently of it
        child.unref();
    } catch (e) {
        // Fail silently so we don't disrupt the user's workflow
    }
}
