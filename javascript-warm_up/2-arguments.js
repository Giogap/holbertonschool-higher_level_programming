#!/usr/bin/node

if (process.argv[3]) {
    console.log('Arguments found');
} 
else if (process.argv[1]) {
        console.log('Arguments found');
    }
else {
    console.log('No argument');
}
