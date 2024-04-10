#!/usr/bin/node
const p = Math.floor(Number(process.argv[2]));
if (isNaN(p)) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < p; a++) {
    console.log('C is fun');
  }
}
