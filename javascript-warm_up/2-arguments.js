#!/usr/bin/node

if (process.argv.slice(20)) {
    console.log('No argument');
}
else if (process.argv.slice(4)) {
    console.log('Arguments found');
}
else {
    console.log('Argument found');
}
