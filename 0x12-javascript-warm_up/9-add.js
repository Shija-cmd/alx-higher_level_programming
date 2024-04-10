#!/usr/bin/node
function add (p, q) {
  return p + q;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
