#!/usr/bin/node

let i = 2;

while (i < process.argv.length) {
  console.log(process.argv[i]);
  i++;
}
