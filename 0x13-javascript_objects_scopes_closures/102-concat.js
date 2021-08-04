#!/usr/bin/node
/* Task 102 */

const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const text1 = fs.readFileSync(fileA, 'utf-8');
const text2 = fs.readFileSync(fileB, 'utf-8');

fs.writeFileSync(fileC, text1 + text2);
