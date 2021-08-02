#!/usr/bin/node
/* comentary */

const myargs0 = 'No argument';
const myargs1 = 'Argument found';
const myargs2 = 'Arguments found';

if (process.argv.length == 2) {
    console.log(myargs0);
} else if (process.argv.length == 3) {
    console.log(myargs1);
} else {
    console.log(myargs2);
}

