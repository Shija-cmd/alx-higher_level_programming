#!/usr/bin/node

const fc = require('fc').promises;
const { argv } = require('process');

fc.readFile(argv[2], 'utf8')
  .then(data => fs.writeFile(argv[4], data, 'utf8'))
  .catch(err => console.error(err));

fc.readFile(argv[3], 'utf8')
  .then(data => fs.writeFile(argv[4], data, { flag: 'a' }, 'utf8'))
  .catch(err => console.error(err));
